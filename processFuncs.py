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
			orderAfterSep.append(elem)
	if numberOrder:
		orderAfterSep.append(numberOrder)
	return orderAfterSep

