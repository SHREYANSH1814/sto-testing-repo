# Intentionally misconfigured so Snyk IaC and other IaC scanners report findings.
# Do not copy these resources into anything real.

terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "public_data" {
  bucket = "sto-testing-public-data"
}

resource "aws_s3_bucket_public_access_block" "public_data" {
  bucket = aws_s3_bucket.public_data.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_acl" "public_data" {
  bucket = aws_s3_bucket.public_data.id
  acl    = "public-read"
}

resource "aws_s3_bucket_versioning" "public_data" {
  bucket = aws_s3_bucket.public_data.id

  versioning_configuration {
    status = "Disabled"
  }
}

resource "aws_security_group" "wide_open" {
  name        = "sto-testing-wide-open"
  description = "Allows unrestricted inbound access"

  ingress {
    description = "SSH from anywhere"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "RDP from anywhere"
    from_port   = 3389
    to_port     = 3389
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

resource "aws_db_instance" "unencrypted" {
  identifier          = "sto-testing-db"
  engine              = "mysql"
  instance_class      = "db.t3.micro"
  allocated_storage   = 20
  username            = "admin"
  password            = "SuperSecret123"
  storage_encrypted   = false
  publicly_accessible = true
  skip_final_snapshot = true
}

resource "aws_ebs_volume" "unencrypted" {
  availability_zone = "us-east-1a"
  size              = 10
  encrypted         = false
}

resource "aws_cloudtrail" "no_validation" {
  name                          = "sto-testing-trail"
  s3_bucket_name                = aws_s3_bucket.public_data.id
  enable_log_file_validation    = false
  include_global_service_events = false

  kms_key_id = aws_kms_key.cloudtrail_key.arn
}

resource "aws_kms_key" "cloudtrail_key" {
  description             = "KMS key for encrypting CloudTrail logs"
  deletion_window_in_days = 10
  enable_key_rotation     = true
}
