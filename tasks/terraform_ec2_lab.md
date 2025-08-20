# 🚀 Terraform Lab: Deploy an EC2 Instance with Security Group and SSH Access

## 🎯 Objective

-   Launch an **Ubuntu EC2 instance** in your **assigned AWS region**.\
-   Create a **Security Group** allowing **SSH (22), HTTP (80), and
    custom port (8080)**.\
-   Attach the **Security Group** to your EC2 instance.\
-   Use an **existing or manually created key-pair** for SSH access.\
-   Verify by **SSH into the instance**.

------------------------------------------------------------------------

## 📝 Lab Instructions

### Step 1: Configure Terraform

1.  Ensure Terraform is installed:

    ``` bash
    terraform -v
    ```

2.  Configure AWS CLI with credentials:

    ``` bash
    aws configure
    ```

    (Use IAM user credentials with EC2 access.)

------------------------------------------------------------------------

### Step 2: Create Terraform Files

#### **1. `provider.tf`**

``` hcl
provider "aws" {
  region = "ap-south-1" # Change to your assigned region
}
```

#### **2. `main.tf`**

``` hcl
resource "aws_security_group" "ec2_sg" {
  name        = "ec2-security-group"
  description = "Allow SSH, HTTP, and custom 8080"

  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow custom app port 8080"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "my_ec2" {
  ami           = "ami-04a37924ffe27da53" # Ubuntu 22.04 LTS in ap-south-1 (Mumbai). Change if in another region
  instance_type = "t2.micro"
  key_name      = "my-keypair" # Use your existing key-pair name

  vpc_security_group_ids = [aws_security_group.ec2_sg.id]

  tags = {
    Name = "Terraform-EC2-Lab-Ubuntu"
  }
}
```

------------------------------------------------------------------------

### Step 3: Initialize & Apply

Run these commands in the project directory:

``` bash
terraform init
terraform plan
terraform apply -auto-approve
```

------------------------------------------------------------------------

### Step 4: Verify EC2 & Security Group

1.  Get the instance **public IP**:

    ``` bash
    terraform output
    ```

    or from AWS Console.

2.  **SSH into the instance**:

    ``` bash
    ssh -i my-keypair.pem ubuntu@<PUBLIC_IP>
    ```

    > Replace `my-keypair.pem` with your private key file. Ensure it has
    > correct permissions:

    ``` bash
    chmod 400 my-keypair.pem
    ```

3.  Test **HTTP (port 80)** and **8080** by starting a simple web
    server:

    ``` bash
    sudo apt update -y
    sudo apt install -y apache2
    sudo systemctl start apache2
    curl http://localhost
    ```

------------------------------------------------------------------------

### ✅ Success Criteria

-   You can **SSH into your Ubuntu EC2 instance**.\
-   You can access ports **22, 80, and 8080** externally.
