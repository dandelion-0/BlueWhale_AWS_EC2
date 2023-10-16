# BlueWhale_AWS_EC2

This is a Python script that allows you to manage your EC2 instances on AWS. You can use this script to get instance details, start instances and stop instances.

## Prerequisites

Before running this script, make sure you have the following:

- AWS access key and secret access key
- AWS region name

## Installation

To run this script, you need to have Python installed on your system. You also need to install the `boto3` library, which can be done using the following command:

pip install boto3


## Configuration

Before running the script, you need to provide your AWS credentials and region information. Update the following variables in the script:

python
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY'
aws_secret_access_key = 'YOUR_AWS_SECRET_KEY'
region_name = 'YOUR_REGION'

## Usage

To use this script, follow these steps:

1. Run the script using the following command:

   

   python script.py
   


2. You will be prompted with a menu. Enter the corresponding number to perform the desired action:

   - Enter `EC2` to get instance details.
   - Enter `start` to start an instance. You will be prompted to enter the instance ID.
   - Enter `stop` to stop an instance. You will be prompted to enter the instance ID.
   - Enter `quit` to exit the program.

3. Follow the instructions on the screen to perform the desired action.

## Example

Here is an example of how to use this script:

1.) Enter 'EC2' to Get instance details,  
2.) Enter 'start' to start the instance,  
3.) Enter 'stop' to stop the instance,  
4.) Enter 'quit' to exit:  

`EC2`  
Instance ID: i-0123456789abcdefg , Instance State: running , Instance Type: t2.micro
Instance ID: i-9876543210zyxwvut , Instance State: stopped , Instance Type: t3.small

1.) Enter 'EC2' to Get instance details,  
2.) Enter 'start' to start the instance,  
3.) Enter 'stop' to stop the instance,  
4.) Enter 'quit' to exit: start

`start`  
Enter EC2 Instance ID: i-0123456789abcdefg  
Starting instance i-0123456789abcdefg
{'StartingInstances': [{'CurrentState': {'Code': 0, 'Name': 'pending'}, 'InstanceId': 'i-0123456789abcdefg', 'PreviousState': {'Code': 80, 'Name': 'stopped'}}]}

1.) Enter 'EC2' to Get instance details,  
2.) Enter 'start' to start the instance,  
3.) Enter 'stop' to stop the instance,  
4.) Enter 'quit' to exit: stop

`stop`  
Enter EC2 Instance ID: i-9876543210zyxwvut  
Stopping instance i-9876543210zyxwvut
{'StoppingInstances': [{'CurrentState': {'Code': 64, 'Name': 'stopping'}, 'InstanceId': 'i-9876543210zyxwvut', 'PreviousState': {'Code': 80, 'Name': 'stopped'}}]}

1.) Enter 'EC2' to Get instance details,  
2.) Enter 'start' to start the instance,  
3.) Enter 'stop' to stop the instance,  
4.) Enter 'quit' to exit: quit


## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.

## Acknowledgement

BlueWhale_AWS_EC2 Application was developed using the following libraries:
- [boto3] (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## Contact

For any questions or inquiries, please contact the project maintainer at [dandelion00@tutanota.com]

Feel free to visit our project page on GitHub: [BlueWhale_AWS_EC2](https://github.com/dandelion-0/BlueWhale_AWS_EC2)
