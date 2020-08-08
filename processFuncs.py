# -*- coding:utf-8 -*-
# --- Written by Corona
# --- Finished on 2020-08-06

import error,classCommands,os
def get_set():
	set_file=open(os.path.dirname(__file__)+"\\init.set")
	set_text=[]
	i=0
	while True:
		tmp=set_file.readline().strip('\n')
		comment_pos=tmp.find('#')
		if comment_pos>0:
			tmp=tmp[:comment_pos]
		set_text.append(tmp.split('='))
		if not set_text[i][0]:
			del set_text[i]
			break
		i+=1
	result={}
	for i in range(len(set_text)):
		result[set_text[i][0]]=set_text[i][1]
	return result

def get_in_dir_name():
	abs_dir_name=os.path.dirname(__file__).split('\\')
	return abs_dir_name[len(abs_dir_name)-1]


def hasMoreThan_1_NumSeq_in(order):
	number_beg=-1
	number_end=-1
	for i in range(len(order)):
		if order[i].isdigit():
			number_beg=i
			break
	for j in range(len(order)):
		if order[j].isdigit():
			number_end=j
			break
	if number_beg<0 or number_end<0:
		return False
	for k in range(number_beg,number_end+1):
		if not order[k].isdigit():
			return True
	return False

def separate_num_and_letter(order):
	numberOrder=''
	orderAfterSep=[]
	for elem in order:
		if elem.isdigit():
			numberOrder+=elem
		else:
			if elem not in orderAfterSep:#--- del repeated order
				orderAfterSep.append(elem)
	
	if numberOrder:
		orderAfterSep.insert(0,numberOrder)
	return orderAfterSep

def hasMoreThan_1_Elem_in(conflictLt,Lt):
	for i in range(len(conflictLt)):
		if conflictLt[i] in Lt:
			for j in range(i+1,len(conflictLt)):
				if conflictLt[j] in Lt:
					return True
	return False

def hasMem_in(lt1,lt2):
	result=[]
	for elem in lt1:
		if elem in lt2:
			result.append(elem)
	return result

def bothHas(lt1,lt2,lt):
	has_lt1_mem_in_lt=False
	has_lt2_mem_in_lt=False
	for elem in lt1:
		if elem in lt:
			has_lt1_mem_in_lt=True
	for elem in lt2:
		if elem in lt:
			has_lt2_mem_in_lt=True
	return has_lt1_mem_in_lt and has_lt2_mem_in_lt

def hasNum_and_mem_in(Set,lt):
	hasMem_of_set=False
	for elem in Set:
		if elem in lt:
			hasMem_of_set=True
	if not hasMem_of_set:return False

	for elem in lt:
		if elem.isdigit():
			return True
	return False

def getElem(subLt,lt):
	for elem in subLt:
		if elem in lt:
			return elem
	return None

def find_all_start(substr,string):
	if not substr:
		return []
	result=[]
	len_sub=len(substr)
	len_str=len(string)
	i=0
	while i <= len_str-len_sub:
		if string[i:i+len_sub]==substr:
			result.append(i)
			i=i+len_sub
		else:
			i=i+1
	return result

def getBegs_and_ends(mainName,str1,command):#--- used in procedure.py
	if str1 not in mainName:
		return ([],[])
	begins=find_all_start(str1,mainName)

	ends=[]
	i=0
	while i < len(begins):
		ends.append(begins[i]+len(str1))
		i+=1
	if command.number:
		if int(command.number.value)>len(begins):
			return ([],[])
		begins=[begins[int(command.number.value)-1]]
		ends=[ends[int(command.number.value)-1]]
	if command.beginEnd:
		if command.beginEnd.value=='b':
			begins=[0]
			ends=[ends[0]]
		elif command.beginEnd.value=='e':
			begins=[begins[0]]
			ends=[len(mainName)]
	if command.sort or command.cancel:
		begins=[0]
		ends=[len(mainName)]
	return (begins,ends)

def compare_by_command(f1,f2,command):
	if command.sort.value=='t':
		return f1.mtime<f2.mtime
	elif command.sort.value=='T':
		return f1.mtime>f2.mtime
	elif command.sort.value=='s':
		return f1.size<f2.size
	elif command.sort.value=='S':
		return f1.size>f2.size
	else:
		return True
def sort_by_command(flt,command):
	for i in range(len(flt)):
		for j in range(i+1,len(flt)):
			if not compare_by_command(flt[i],flt[j],command):
				flt[i],flt[j]=flt[j],flt[i]
	return flt

def real_str2(it,ori_str2,command,max_num):
	if command.sort.value=='':
		return ori_str2
	max_len=len(str(max_num))
	it=str(it)
	while len(it)<max_len:
		it='0'+it
	star_pos=ori_str2.find('*')
	return ori_str2[0:star_pos]+it+ori_str2[star_pos+1:]

def replace(ori_main_name,str2,begins,ends):
	name_piece=[]
	
	for i in range(len(begins)+1):
		if i==0:
			name_piece.append(ori_main_name[0:begins[0]])
		if i==len(begins):
			name_piece.append(ori_main_name[ends[i-1]:])
		if 0<i<len(begins):
			name_piece.append(ori_main_name[ends[i-1]:begins[i]])
	new_main_name=name_piece[0]
	for i in range(1,len(name_piece)):
		new_main_name=new_main_name+str2+name_piece[i]
	return new_main_name

