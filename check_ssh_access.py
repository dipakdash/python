import paramiko
import re
import sys

username="root"
password="nai@123"
#host="10.213.136.87"
host = sys.argv[1]
remote_dir="."

ssh = paramiko.SSHClient()
try:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    print "successful"
    ssh.close()
#except (paramiko.BadHostKeyException, paramiko.AuthenticationException, paramiko.SSHException, socket.error) as e:
except Exception as e:
    print e