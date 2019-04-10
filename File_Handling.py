#Global Imports.


class FileHandling:
	def __init__(self,Filename,FilePath):
		self.Filename=Filename
		self.FilePath=FilePath
	
	def creatFileObject(self):
		s = '\\'
		filename = s.join([self.FilePath,self.Filename])
		print(filename)
		fileObj = open(filename,'r')
		return fileObj
	
	def CreateListOfFileObj(self):
		fileObj = self.creatFileObject()
		listOfVMNames=[]
		for i in fileObj:
			listOfVMNames.append(i.rstrip())
		
		return listOfVMNames
		
if __name__ == '__main__':
	obj = FileHandling(r'XXXXXXXXXXXXXXXXX',r'XXXXXXXXXXXXXXXXXXXXXXXXXXX')
	print(obj.CreateListOfFileObj())
			