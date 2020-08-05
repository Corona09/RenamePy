#-*- coding:utf-8 -*
import os
class File:
	def __init__(self,oriFullName,oriPath):
		self.__oriFullName=oriFullName
		self.__path=oriPath
		dot_pos=oriFullName.rfind('.')
		self.__suffix=oriFullName[dot_pos:] if dot_pos>0 else ''
		self.__mainName=self.__oriMainName=oriFullName[:dot_pos] if dot_pos>0 else oriFullName
		self.__size=os.path.getsize(oriPath+'\\'+oriFullName)
		self.__mtime=os.path.getmtime(oriPath+'\\'+oriFullName)
	@property
	def oriFullName(self):return self.__oriFullName
	@property
	def fullName(self):return self.__mainName+self.__suffix
	@property
	def path(self):return self.__path
	@property
	def suffix(self):return self.__suffix
	@property
	def mainName(self):return self.__mainName
	@property
	def size(self):return self.__size
	@property
	def mtime(self):return self.__mtime

	def __str__(self):return self.fullName
	def rename(newMainName):self.__mainName=newMainName
