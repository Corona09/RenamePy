#-*- coding:utf-8 -*-
import error,classCommands
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


def makeCommand(std_order):
	return classCommands.Command(
		number=std_order[0] if len(std_order)>0 and std_order[0].isdigit() else  '',
		upLower=getElem('uUlL',std_order),
		beginEnd=getElem('be',std_order),
		Sort=getElem('tTsS',std_order),
		Quit=getElem('q',std_order),
		cancel=getElem('z',std_order),
		Help=getElem('h',std_order)
	)
