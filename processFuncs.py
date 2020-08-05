#-*- coding:utf-8 -*-
import error
def hasMoreThan_1_NumSeq_in(order):
	number_beg=0
	number_end=len(order)-1
	for i in range(len(order)):
		if order[i].isdigit():
			number_beg=i
			break
	for j in range(len(order)):
		if order[j].isdigit():
			number_end=j
			break
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
