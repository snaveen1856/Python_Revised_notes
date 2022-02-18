"""
import pypsexec.client
import Client
import os
import time
import sys
"""
# import paramiko


"""
host = '10.10.1.11'
user = 'username'
password = 'password'

c = Client(host, username=user, password="password", encrypt=False)
c.connect()
try:
     c.create_service()
     stdout = c.run_executable("cmd.exe", arguments="iisreset")
finally:
     c.cleanup()
     c.remove_service()
     c.disconnect()
output = []
output = stdout[0].decode("utf-8")
print(output.split("\r\n")[1:3])
"""

"""
ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='10.10.1.11', username="admin", password="NewPass@123")
shell = ssh.invoke_shell()
command = "docker ps"
shell.send(command + "\n")
ssh.exec_command('10.10.1.11')
stdin, stdout, stderr = ssh.exec_command('date')
output = []
for i in range(0, 6):
    output.append(stdout.readlines(i))
print(output)
ssh.close()
"""
inp = input('enter a string;')
cmd = f" this is a string {inp} "
print(cmd)
