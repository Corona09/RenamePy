#-*- coding:utf-8 -*-
import error,classCommands
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
	while i < len_str-len_sub:
		if string[i:i+len_sub]==substr:
			result.append(i)
			i=i+len_sub
	return result

def getBegs_and_ends(mainName,str1,command):#--- used in procedure.py
	if str1 not in mainName:
		return ([],[])
	begins=find_all_start(str1,mainName)
	ends=[]
	i=0
	while i < len(begins):
		ends.appen(begins[i]+len(str1))
		i+=1
	# dlt=[]
	# for i in range(len(begins)):
	# 	if begins[i]=='' or begins[i]==None:
	# 		dlt.append(i)
	# for elem in dlt:
	# 	begins.remove(begins[i])
	# 	ends.remove(ends[i])
	if command.number:
		begins=[begins[int(command.number)]]
		ends=[ends[int(command.number)]]
	if command.beginEnd:
		if command.beginEnd=='b':
			begins[0]=0
		elif command.beginEnd=='e':
			ends[0]=len(mainName)-1
	if command.sort or command.cancel:
		begins=[0]
		ends=[len(mainName)-1]
	return (begins,ends)

def compare_by_command(f1,f2,command):
	if command.sort=='t':
		return f1.mtime<f2.mtime
	elif command.sort=='T':
		return f1.mtime>f2.mtime
	elif command.sort=='s':
		return f1.size<f2.size
	elif command.sort=='S':
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
	if command.sort=='':
		return ori_str2
	max_len=len(str(max_num))
	it=str(it)
	while len(it)<max_len:
		it='0'+it
	star_pos=ori_str2.find('*')
	return ori_str2[0:star_pos]+it+ori_str2[star_pos+1:]
