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
		def testconnection():
			try:
				self.subprocess.call(["ping " , self.Hostname], shell=True)
				function(Username,Hostname,Password,Port=22)
			except Exception as error:
				raise error
	
	@DecoratorFunction		
	def sshConnection(self,Username,Hostname,Password,Port=22):
	
		try:
			self.ssh.connect(Hostname,Port,Username,Password)
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
	obj.sshConnection()
	obj.executeCommand("ls -lrt")
	obj.printOutput()
	obj.closeChannel()
	
		
		
	