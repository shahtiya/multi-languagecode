import paramiko

HOST = "ec2-13-127-101-39.ap-south-1.compute.amazonaws.com"
USERNAME = "ec2-user"  # ubuntu for Ubuntu EC2
KEY_FILE = "acha.pem"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=HOST,
    username=USERNAME,
    key_filename=KEY_FILE
)

commands = [
    "rm -rf multi-languagecode",
    "git clone https://github.com/shahtiya/multi-languagecode.git",
    "cd multi-languagecode && python3 main.py"
]

for command in commands:
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode())
    print(stderr.read().decode())

ssh.close()

print("Deployment completed successfully")
