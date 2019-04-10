#Global Imports

import paramiko
#import logger
#import os
#import sys
import subprocess


class RemoteConnection:
	def __init__(self):
		self.ssh= paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
	
	def DecoratorFunction(function):
			
			def testconnection(*args, **kwargs):
				try:
					output = subprocess.check_output(['ping', 'XX.XX.XX.XX'], shell=True)
					function(*args, **kwargs)
				except Exception as error:
					raise error
			
			return testconnection
		
	@DecoratorFunction
	def sshConnection(self,
					  Username,
					  Hostname,
					  Password,
					  Port=22):
					  
		
		try:
			print(Username,
				  Hostname,
				  Password,
				  Port)
				  
			self.ssh.connect(username=Username,
							 hostname=Hostname,
							 password=Password,
							 port=Port)
		
		except Exception as error:
			raise error
	
	def executeCommand(self,Command):
		self.stdin, self.stdout, self.stderr = self.ssh.exec_command(Command)
		
	def invokeShell(self):
		channel = self.ssh.invoke_shell()
		
	def printOutput(self):
		self.output = self.stdout.readlines()
		print('\n'.join(self.output))

	
	def closeChannel(self):
		self.ssh.close()
		print("SSH Channel closed")
		
if __name__ == '__main__':
	obj = RemoteConnection()
	obj.sshConnection('XXXXXXXX','XX.XX.XX.XX','XXXXXXXXXXXXX')
	obj.executeCommand("ls -lrt")
	obj.printOutput()
	obj.closeChannel()
	
		
		
	