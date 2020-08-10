# -*- coding:utf-8 -*-
# --- Written by Corona
# --- Finished on 2020-08-06
 
import os,sys,error,classFile,classCommands,processFuncs,validity,log
pre_name={}
set_text=processFuncs.get_set();

def renew_working_dir():
	VALUE_WHERE_POWERSHELL_RUNS = '0'
	VALUE_WHERE_PROGRAM_LOCATED = '1'
	KEY_WORKING_DIR = 'working_dir'
	if set_text[KEY_WORKING_DIR] == VALUE_WHERE_POWERSHELL_RUNS:
		os.chdir(os.getcwd())
	elif set_text[KEY_WORKING_DIR] == VALUE_WHERE_PROGRAM_LOCATED:
		os.chdir(os.path.dirname(__file__) + '\\..')

def display(cnt):
	KEY_LS_DIR = 'ls_dir'

	if not cnt:
		print("----------------------------------------")
		print("| This is a program written by Corona. |")
		print("| Copyright(C)Corona 2020              |")
		print("----------------------------------------")
	else:
		renew_working_dir()
		print("\nopertion {}:".format(cnt))
		print("************The file list:*************")
		print('* [***] : Current Working Directory:"{}"'.format(os.getcwd().upper()))
		flt=os.listdir()

		# --- Delete the directory from the list if the value of choice 'ls_dir' is 0.
		# --- But whether there are 0 or 1, the dirname must be deleted from the list, or error will occur.
		if not int(set_text[KEY_LS_DIR]):
			del_lt=[]
			for i in range(len(flt)):
				if os.path.isdir(flt[i]):
					del_lt.append(flt[i])
			for elem in del_lt:
				flt.remove(elem)
		if processFuncs.get_in_dir_name() in flt:
			flt.remove(processFuncs.get_in_dir_name())

		# --- if there are too many lines, only part of them will be printed.
		# --- the lines printed rely on the choice "max_print_line" in doc "init.set".
		max_print_line=int(set_text["max_print_line"])
		for i in range(min(len(flt),max_print_line)):
			if i+1>max_print_line:
				break
			print('* [{num:0>3d}] : "{fname}"{if_dir}'.format(num=i+1,fname=flt[i],if_dir='' if not os.path.isdir(flt[i]) else ' (DIR)'))
		if len(flt)>max_print_line:
			print('* ......')
			print('* Totally {tot} files. To see more, please check the working directory or see file "__cache.dat" in CWD.'.format(tot=len(flt)))
			cache=open(os.path.dirname(__file__)+'\\__cache.dat','w')
			for i in range(max_print_line,len(flt)):
				cache.write('[{num:0>3d}] : "{fname}"{if_dir}\n'.format(num=i+1,fname=flt[i],if_dir='' if not os.path.isdir(flt[i]) else ' (DIR)'))
		print("***************************************")
		
def splitRaw(raw):
	raw=raw.split('\\')
	str1=raw[0]
	str2=raw[1]
	command='' if len(raw)<3 else raw[2]
	return tuple([str1,str2,command])

def getFileList():
	result=os.listdir(os.getcwd())

	# --- Delete the directory from the list if the value of choice 'ls_dir' is 0.
	# --- But whether there are 0 or 1, the dirname must be deleted from the list, or error will occur.
	whether_ls_dir=int(set_text["ls_dir"])
	if not whether_ls_dir:
		del_lt=[]
		for elem in result:
			if os.path.isdir(elem):
				del_lt.append(elem)
		for elem in del_lt:
			result.remove(elem)
	if processFuncs.get_in_dir_name() in result:
		result.remove(processFuncs.get_in_dir_name())
	
	for i in range(len(result)):
		result[i]=classFile.File(result[i],os.getcwd())
	return result

def mainProcess(str1,str2,order,name_log):
	process_failed=False
	renew_working_dir()
	# --- get the std command.
	std_order=processFuncs.separate_num_and_letter(order)
	command=classCommands.makeCommand(std_order)

	# --- Get the file list:
	flt=getFileList()

	if not command.whether_rename(): # --- this command will not rename the files
		if command.Help.value:
			command.print_help()
	else: # --- this command will rename the files.
		if command.cancel.value:
			if name_log and name_log[0].length>=2:
				for i in range(len(name_log)):
					cur_name=name_log[i].back()
					dot_pos=cur_name.rfind('.')
					suffix=cur_name[dot_pos:] if dot_pos>0 else ''
					tmp_name='Begin_bcigiuipgva3cvGHVGHjsbv__{Num:0>6d}__avhav_End'.format(Num=i)+suffix
					os.rename(cur_name,tmp_name)
				for i in range(len(name_log)):
					pre_name=name_log[i].lists[name_log[i].length-2]
					dot_pos=pre_name.rfind('.')
					suffix=pre_name[dot_pos:] if dot_pos>0 else ''
					cur_name='Begin_bcigiuipgva3cvGHVGHjsbv__{Num:0>6d}__avhav_End'.format(Num=i)+suffix
					os.rename(cur_name,pre_name)
					name_log[i].pop()
			else:
				error.warning(418)
				process_failed=True
		else:
			flt=processFuncs.sort_by_command(flt,command)
			for i in range(len(flt)):
				begins,ends=processFuncs.getBegs_and_ends(flt[i].mainName,str1,command)

				if begins:
					real_str2=processFuncs.real_str2(i+1,str2,command,len(flt))
					new_main_name=processFuncs.replace(flt[i].mainName,real_str2,begins,ends)
					flt[i].rename(new_main_name)
			# --- To Check if there are empty names in new names.
			if validity.have_empty_names_in(flt):
				error.warning(419)
				process_failed=True
				return command.Quit and not command.Help
			# --- To Check if new names are the sames the olds.
			all_same=True
			for f in flt:
				if f.oriFullName!=f.fullName:
					all_same=False
			if all_same:
				error.warning(420)
				process_failed=True
				return command.Quit and not command.Help
			# --- To Check if the new names have conflict with old names during and after the process of raneming
			if not validity.conflict_while_rename(flt):
				for i in range(len(flt)):
					os.rename(flt[i].oriFullName,flt[i].fullName)
				log.update(name_log,flt)
			else:
				error.warning(validity.conflict_while_rename(flt))
				process_failed=True
	if not process_failed:
		error.warning(0)
	return command.Quit and not command.Help
