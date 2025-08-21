# 🚀 Terraform Lab: Create a Basic VPC, Networking & Load Balancer

## 🎯 Objective
By the end of this lab, you will:
- Create a **custom VPC**.  
- Add **public subnets** in two availability zones.  
- Configure an **Internet Gateway (IGW)** and a **Route Table**.  
- Launch **two EC2 instances** in different subnets.  
- Deploy an **Application Load Balancer (ALB)** to distribute traffic between instances.  

---

## 📝 Lab Instructions

### Step 1: Configure Terraform
1. Ensure Terraform is installed:
   ```bash
   terraform -v
   ```
2. Configure AWS CLI:
   ```bash
   aws configure
   ```

---

### Step 2: Create Terraform Files

#### **1. `provider.tf`**
```hcl
provider "aws" {
  region = "ap-south-1" # Change to your assigned region
}
```

---

#### **2. `vpc.tf`**
```hcl
# Create VPC
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = { Name = "MyVPC" }
}

# Internet Gateway
resource "aws_internet_gateway" "my_igw" {
  vpc_id = aws_vpc.my_vpc.id
  tags = { Name = "MyIGW" }
}

# Public Subnets
resource "aws_subnet" "public_subnet_1" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "ap-south-1a"
  map_public_ip_on_launch = true
  tags = { Name = "PublicSubnet1" }
}

resource "aws_subnet" "public_subnet_2" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "ap-south-1b"
  map_public_ip_on_launch = true
  tags = { Name = "PublicSubnet2" }
}

# Route Table
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.my_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.my_igw.id
  }
  tags = { Name = "PublicRouteTable" }
}

# Associate Route Table
resource "aws_route_table_association" "public_assoc_1" {
  subnet_id      = aws_subnet.public_subnet_1.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "public_assoc_2" {
  subnet_id      = aws_subnet.public_subnet_2.id
  route_table_id = aws_route_table.public_rt.id
}
```

---

#### **3. `security.tf`**
```hcl
resource "aws_security_group" "alb_sg" {
  vpc_id = aws_vpc.my_vpc.id
  name   = "alb-sg"

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "ec2_sg" {
  vpc_id = aws_vpc.my_vpc.id
  name   = "ec2-sg"

  ingress {
    description = "Allow HTTP from ALB"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    security_groups = [aws_security_group.alb_sg.id]
  }

  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

---

#### **4. `instances.tf`**
```hcl
resource "aws_instance" "web1" {
  ami           = "ami-04a37924ffe27da53" # Ubuntu 22.04 in ap-south-1 (change if needed)
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.public_subnet_1.id
  key_name      = "my-keypair"

  vpc_security_group_ids = [aws_security_group.ec2_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              apt update -y
              apt install -y apache2
              echo "Hello from Web1" > /var/www/html/index.html
              systemctl start apache2
              EOF

  tags = { Name = "WebServer1" }
}

resource "aws_instance" "web2" {
  ami           = "ami-04a37924ffe27da53"
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.public_subnet_2.id
  key_name      = "my-keypair"

  vpc_security_group_ids = [aws_security_group.ec2_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              apt update -y
              apt install -y apache2
              echo "Hello from Web2" > /var/www/html/index.html
              systemctl start apache2
              EOF

  tags = { Name = "WebServer2" }
}
```

---

#### **5. `alb.tf`**
```hcl
resource "aws_lb" "my_alb" {
  name               = "my-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb_sg.id]
  subnets            = [aws_subnet.public_subnet_1.id, aws_subnet.public_subnet_2.id]

  tags = { Name = "MyALB" }
}

resource "aws_lb_target_group" "my_tg" {
  name     = "my-target-group"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.my_vpc.id

  health_check {
    path                = "/"
    interval            = 30
    timeout             = 5
    healthy_threshold   = 2
    unhealthy_threshold = 2
  }
}

resource "aws_lb_listener" "my_listener" {
  load_balancer_arn = aws_lb.my_alb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.my_tg.arn
  }
}

resource "aws_lb_target_group_attachment" "web1" {
  target_group_arn = aws_lb_target_group.my_tg.arn
  target_id        = aws_instance.web1.id
  port             = 80
}

resource "aws_lb_target_group_attachment" "web2" {
  target_group_arn = aws_lb_target_group.my_tg.arn
  target_id        = aws_instance.web2.id
  port             = 80
}
```

---

### Step 3: Initialize & Apply
```bash
terraform init
terraform plan
terraform apply -auto-approve
```

---

### Step 4: Verify
1. Get the ALB **DNS name**:
   ```bash
   terraform output
   ```
   or from AWS Console → EC2 → Load Balancers.

2. Open the ALB DNS in your browser.  
   - Refresh a few times → You should see responses alternating between **Web1** and **Web2**.

---

### ✅ Success Criteria
- VPC and subnets created.  
- Two Ubuntu servers running Apache.  
- ALB DNS distributes traffic across both servers.  
