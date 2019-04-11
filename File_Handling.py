#Global Imports.
from xml_parser import XmlParser

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
	obj1 = XmlParser(Fake_Path)
	listOfElements=obj1.ParseXML()
	filename = listOfElements[0]
	filepath = listOfElements[1]
	obj = FileHandling(filename,filepath)
	print(obj.CreateListOfFileObj())
			