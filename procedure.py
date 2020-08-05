#-*- coding:utf-8 -*-
import os,sys,error,classFile,classCommands,processFuncs
def renew_working_dir():
	os.chdir(os.path.dirname(__file__)+'\\..\\testDir')

def display(cnt):
	if not cnt:
		print("----------------------------------------")
		print("| This is a program written by Corona. |")
		print("| Copyright(C)Corona 2020              |")
		print("----------------------------------------")
	else:
		renew_working_dir()
		print("opertion {}:".format(cnt))
		print("************The file list:*************")
		print('* [***] : Current Working Directory:"{}"'.format(os.getcwd().upper()))
		flt=os.listdir()
		del_lt=[]
		for i in range(len(flt)):
			if os.path.isdir(flt[i]):
				del_lt.append(flt[i])
		for elem in del_lt:
			flt.remove(elem)
		for i in range(len(flt)):
			print('* [{num:0>3d}] : "{fname}"'.format(num=i+1	,fname=flt[i]))
		print("***************************************")
		
def splitRaw(raw):
	raw=raw.split('\\')
	str1=raw[0]
	str2=raw[1]
	command='' if len(raw)<3 else raw[2]
	return tuple([str1,str2,command])

def getFileList():
	result=os.listdir(os.getcwd())
	del_lt=[]
	for elem in result:
		if os.path.isdir(elem):
			del_lt.append(elem)
	for elem in del_lt:
		result.remove(elem)
	for i in range(len(result)):
		result[i]=classFile.File(result[i],os.getcwd())
	return result

def mainProcess(str1,str2,order):
	renew_working_dir()
	# --- get the std command.
	std_order=processFuncs.separate_num_and_letter(order)
	command=classCommands.makeCommand(std_order)
	# command:\number \upLower \beginEnd \sort \cancel \Quit \Help

	# --- Get the file list:
	flt=getFileList()
	fl_num=len(flt)
	
	if not command.whether_rename(): #--- this command will not rename the files
		pass
	else: #--- this command will rename the files.
		flt=processFuncs.sort_by_command(flt,command)
		for i in range(len(flt)):
			begs,ends=processFuncs.getBegs_and_ends(flt[i].mainName,str1,command)
			real_str2=processFuncs.real_str2(i,str2,command,len(flt))
			print('real str2:{}'.format(real_str2))

