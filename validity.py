#-*- coding:utf-8 -*-
import error,processFuncs
validCommand='ruUlLtTsSqzhbe'
invalidNameChar='\\/:*?"<>|'
def notValid(raw):
	rawAfterSplit=raw.split('\\')
	#---split the s1/s2/order
	if len(rawAfterSplit)>3:
		return 401
	if len(rawAfterSplit)<2:
		rturn 402
	str1=rawAfterSplit[0]
	str2=rawAfterSplit[1]
	order='' if len(rawAfterSplit)==2 else rawAfterSplit[2]

	#---check whether there are invalid chars in str1/str2/order
	for elem in str1:
		if elem in validNameChar:
			return 405
	for elem in str2:
		if elem in validCommand and elem!='*':
			return 405
	for elem in order:
		if elem not in validCommand:
			return 404
	if processFuncs.hasMoreThan_1_NumSeq_in(order):
		return 	407
	
	#---seperate the number and alpha in order and del the repeated order
	orderAfterSep=processFuncs.separate_num_and_letter(order)
	
	return False