#Global Imports

import paramiko
#import logger
#import os
#import sys
import subprocess

def DecoratorFunction(function):
		#import pdb; pdb.set_trace()
		def testconnection(*args, **kwargs):
			try:
				
				print('Hello')
				output = subprocess.call(['ping', 'XX.XX.XX.XX'], shell=True)
				print(output)
				function(*args, **kwargs)
			except Exception as error:
				raise error
		return testconnection

class RemoteConnection:
	def __init__(self):
		self.ssh= paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		
		
	@DecoratorFunction
	def sshConnection(self,Username,Hostname,Password,Port=22):
		#import pdb; pdb.set_trace()
		try:
			print(Username,Hostname,Password,Port)
			self.ssh.connect(username=Username,hostname=Hostname,password=Password,port=Port)
		except Exception as error:
			raise error
	
	def executeCommand(self,Command):
		self.stdin, self.stdout, self.stderr = self.ssh.exec_command(Command)
		
	
	def printOutput(self):
		self.output = self.stdout.readlines()
		print('\n'.join(self.output))

	
	def closeChannel(self):
		self.ssh.close()



		
if __name__ == '__main__':
	obj = RemoteConnection()
	#import pdb; pdb.set_trace()
	obj.sshConnection('XXXXXX','XX.XX.XX.XX','XXXXXXXX')
	obj.executeCommand("ls -lrt")
	obj.printOutput()
	obj.closeChannel()
	
		
		
	