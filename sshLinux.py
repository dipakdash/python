import paramiko
import re

username="ddash"
password="nai@123"
host="10.213.136.207"
remote_dir="."

cmd_to_execute="uname -a"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=username, password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
output =''.join(ssh_stdout).rstrip('\n')
print output
ssh.close()

##re.findall('mwg-(.*).mlos2',str1)
#
#
#pattern=re.compile('mwg-(.*)-(.*).mlos2')
#m=pattern.findall(version)
#if m:
#    dotted_Version=m[0][0]
#    lsVersions = dotted_Version.split(".")
#    lsVersions = list(map(int, lsVersions))
#    numVersion=lsVersions[0]*100 + lsVersions[1]*10 + lsVersions[2]
#    #numVersion will have values 742/741/732/ , can be used for comparison
#
#
#print numVersion
#









