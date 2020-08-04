#-*- coding:utf-8 -*-
import error
def hasMoreThan1NumSeq_in(order):
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