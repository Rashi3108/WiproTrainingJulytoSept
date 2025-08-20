# resource "aws_instance" "my_ec2" {
#   ami           = var.instance_ami
#   instance_type = var.instance_type

#   tags = {
#     Name = "my_ec2_instance_terraform"
#   }
# }

# resource "aws_s3_bucket" "my_bucket" {
#   bucket = var.bucket_name

#   tags = {
#     Environment = "Dev"
#   }
# }