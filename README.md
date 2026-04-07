# AWS EC2 Instance Checker

A Python script that connects to AWS and checks all EC2 instances in a region, showing their state, type, and launch time, then exports a JSON report.

## Tech Stack
- Python 3
- boto3 (AWS SDK)
- AWS EC2

## What It Does
- Connects to AWS EC2 using boto3
- Lists all instances with state, instance type and launch time
- Saves a full report to ec2_report.json

## How to Run

1. Install dependencies: pip install -r requirements.txt
2. Configure AWS: aws configure
3. Run: python3 ec2_checker.py

## Sample Output
Connecting to AWS EC2...
No EC2 instances found in this region.
Report saved to ec2_report.json
Total instances found: 0

## Author
Sadhvi - Cloud Engineer | AWS Certified Solutions Architect
