import boto3

# AWS credentials and region
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY'
aws_secret_access_key = 'YOUR_AWS_SECRET_KEY'
region_name = 'YOUR_REGION'

try :
    # Create EC2 client
    ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, 
                            aws_secret_access_key=aws_secret_access_key, 
                            region_name=region_name)
except Exception as ex:
    print(ex)

## Get instance details
def Get_instance_details():
    response = ec2_client.describe_instances()

    # Iterate over reservations and instances to get details and IDs
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_state = instance['State']['Name']
            instance_type = instance['InstanceType']
            # Add more attributes as needed
            
            # Print instance details
            print("Instance ID:", instance_id, end=' , ')
            print("Instance State:", instance_state, end=' , ')
            print("Instance Type:", instance_type)
            print()

# Start the EC2 instance
def start_instance(instance_id):
    instance_id = input('PLEASE ENTER YOUR INSTANCE ID')
    response = ec2_client.start_instances(InstanceIds=[instance_id])
    print(f'Starting instance {instance_id}')
    print(response)

# Stop the EC2 instance
def stop_instance(instance_id):
    instance_id = input('PLEASE ENTER YOUR INSTANCE ID')
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(f'Stopping instance {instance_id}')
    print(response)

# Main function
def main():
    try:
        while True:
            choice = input("1.) Enter 'EC2' to Get instance details, \n2.) Enter 'start' to start the instance, \n3.) Enter 'stop' to stop the instance, \n4.) Enter 'quit' to exit: ")
            
            if choice == 'EC2' or choice == 'ec2' :
                Get_instance_details()
            elif choice == 'start':
                start_instance()
            elif choice == 'stop':
                stop_instance()
            elif choice == 'quit':
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()