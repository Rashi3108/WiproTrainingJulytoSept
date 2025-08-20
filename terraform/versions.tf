terraform {
  backend "s3" {
    bucket = "terraform-batch4-statefile"
    key = "terraform.tfstate"
    region = "eu-west-1"
    use_lockfile = true
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.region
}