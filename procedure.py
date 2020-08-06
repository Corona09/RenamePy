#-*- coding:utf-8 -*-
import os,sys,error,classFile,classCommands,processFuncs,validity,log
pre_name={}

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

def mainProcess(str1,str2,order,name_log):
	renew_working_dir()
	# --- get the std command.
	std_order=processFuncs.separate_num_and_letter(order)
	command=classCommands.makeCommand(std_order)

	# --- Get the file list:
	flt=getFileList()

	if not command.whether_rename(): #--- this command will not rename the files
		if command.Help.value:
			command.print_help()
		else:
			if command.cancel.value:
				pass
			else:
				pass
	else: #--- this command will rename the files.
		flt=processFuncs.sort_by_command(flt,command)
		for i in range(len(flt)):
			begins,ends=processFuncs.getBegs_and_ends(flt[i].mainName,str1,command)
			# error.debug('begins:"{}",ends:"{}"'.format(begins,ends))
			if begins:
				real_str2=processFuncs.real_str2(i,str2,command,len(flt))
				# error.debug('real str2:{}'.format(real_str2))
				new_main_name=processFuncs.replace(flt[i].mainName,real_str2,begins,ends)
				flt[i].rename(new_main_name)
		if not validity.conflict_while_rename(flt):
			for i in range(len(flt)):
				os.rename(flt[i].oriFullName,flt[i].fullName)
			log.update(name_log,flt)
			for elem in name_log:
				print(elem)
	if command.Quit and not command.Help:
		return True
	return False

