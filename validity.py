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
	if 'h' in order:
		h_pos=order.find('h')
		if h_pos!=0:
			return 412

	#---seperate the number and letters in `order` and del the repeated order
	#---orderAfterSep is a `list` 
	#---if orderAfterSep has number order, it must be the first element.
	orderAfterSep=processFuncs.separate_num_and_letter(order)

	#---judge process begins:
	if str1=='':
		if str2=='':
			if orderAfterSep=='':
				return 408 #--error Code : ???
			else:
				#return orderAfterSep is not the valid combination of 'tTsSqzh'
				#valid combination : t/T/s/S/q/z/h/*q/h*
				if orderAfterSep[0].isdigit():
					return 409
				if processFuncs.hasMoreThan_1_Elem_in(('t','T','s','S'),orderAfterSep):
					return 406
				if 'z' in orderAfterSep and len(orderAfterSep)>1:
					return 406
				if 'h' in orderAfterSep and len(orderAfterSep)>2:
					return 406

		else:
			#if tTsS in orderAfterSep:
			#	if str2 suits the order:
			# 		return 0
			# 	else:
			# 		return True
			#else:
			#	return True # --- errCode : ??? 
	else:
		if '*' not in str2:
			#---judge the orderAfterSep's validity with  
			pass
		else:
			return True #---error Code : ???
	return False