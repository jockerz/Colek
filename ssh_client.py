#!/usr/bin/python
import paramiko
from getpass import getpass as pwd_prompt

host = "192.168.56.103"
username = "haluang"
commands = ['ls','uname -a','id']

sshClient = paramiko.SSHClient()
try:
    # load default known_host file
    sshClient.load_system_host_keys()
    # warning for unknown host key, but accepting it
    sshClient.set_missing_host_key_policy( paramiko.WarningPolicy() )
    # Input password
    pwd = pwd_prompt("Password: ")
    sshClient.connect( host, username=username, password=pwd, timeout=10.0 )
    for command in commands:
        stdin, stdout, stderr = sshClient.exec_command(command)
        output = stdout.read()
        error = stderr.read()
        if output:
            print output
        if error:
            print error
        
finally:
    sshClient.close()
