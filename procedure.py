#-*- coding:utf-8 -*-
import os,sys,error,classFile,classCommands,processFuncs
def renew_working_dir():
	os.chdir(os.path.dirname(__file__)+'\\..')
def display(cnt):
	if not cnt:
		print("----------------------------------------")
		print("| This is a program written by Corona. |")
		print("| Copyright(C)Corona 2020              |")
		print("----------------------------------------")
	else:
		print("opertion {}:".format(cnt))
		print("************The file list:*************")
		flt=os.listdir()
		del_lt=[]
		for i in range(len(flt)):
			if os.path.isdir(flt[i]):
				del_lt.append(flt[i])
		for elem in del_lt:
			flt.remove(elem)
		for i in range(len(flt)):
			flt[i]=classFile.File(flt[i],os.getcwd())
		for i in range(len(flt)):
			print('* [{num:0>3d}] : "{fname}"'.format(num=i,fname=flt[i].mainName+flt[i].suffix))
		print("***************************************")
		
def splitRaw(raw):
	raw=raw.split('\\')
	str1=raw[0]
	str2=raw[1]
	command='' if len(raw)<3 else raw[2]
	return tuple(str1,str2,command)
def mainProcess(str1,str2,command):
	renew_working_dir()

	return