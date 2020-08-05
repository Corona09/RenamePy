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
	return (begins,ends)