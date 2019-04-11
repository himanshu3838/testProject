#Global Imports
#from xml.dom import minidom
import xml.etree.ElementTree as ET

class XmlParser:
	def __init__(self,FILEPATH):
		self.FILEPATH=FILEPATH
		
	def ParseXML(self):
		#import pdb; pdb.set_trace()
		xmldata = ET.parse(self.FILEPATH)
		dataList = xmldata.getroot()
		data=[]
		for elem in dataList:
			for subelem in elem:
				data.append(subelem.text)
		return data

if __name__ == '__main__':
	#import pdb; pdb.set_trace()
	obj = XmlParser(Fake_Path)
	datalist=obj.ParseXML()
	print(datalist)
	