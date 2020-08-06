#-*- coding:utf-8 -*-
import error,processFuncs,classCommands
validCommand='uUlLtTsSqzhbe'
invalidNameChar='\\/:?"<>|' #--- it doesn't contain '*' because str2 can have '*' in some cases

def hasConflict_in(std_order):
	#--- std_order=[number,'','','',...]
	#--- group inner conflict.
	conflictLt=[('u','U','l','L'),('t','T','s','S'),('e','b')]
	for elem in conflictLt:
		if processFuncs.hasMoreThan_1_Elem_in(elem,std_order):
			return True
	
	#--- group conflict.
	if processFuncs.bothHas('uUlLeb','tTsS',std_order) or processFuncs.bothHas('uUlLebtTsS','z',std_order):
		return True
	
	#--- conflict with Number:
	if processFuncs.hasNum_and_mem_in('hztTsS',std_order):
		return True
	
	return False

def notValid(raw):
	rawAfterSplit=raw.split('\\')
	#---split the s1/s2/order
	if len(rawAfterSplit)>3:
		return 401
	if len(rawAfterSplit)<2:
		return 402
	str1=rawAfterSplit[0]
	str2=rawAfterSplit[1]
	order='' if len(rawAfterSplit)==2 else rawAfterSplit[2]

	if order=='':
		if processFuncs.hasMem_in(invalidNameChar+'*',str1) or processFuncs.hasMem_in(invalidNameChar,str2):
			return 405
		else:
			return 0
	else:
		for elem in order:
			if not elem.isdigit() and elem not in validCommand:
				return 404
		if processFuncs.hasMoreThan_1_NumSeq_in(order):
			return 407
		std_order=processFuncs.separate_num_and_letter(order)

		if hasConflict_in(std_order):
			return 406
		
		command=classCommands.makeCommand(std_order)
		a=classCommands.Command()
		if not command.is_possible():
			return 406
		whe_str_empty=command.whether_str_empty()
		if (whe_str_empty.whether_str1_empty==1 and str1=='') or (whe_str_empty.whether_str1_empty==-1 and str1):return 413
		if (whe_str_empty.whether_str2_empty==1 and str2=='') or (whe_str_empty.whether_str2_empty==-1 and str2):return 413
		
		# --- Special Judge:
		# if 'tTsS' exists, str2 should have special format.
		if command.sort:
			if str2 and '*' not in str2:
				return 414
			if str2.count('*')>1:
				return 415

	return 0

def conflict_while_rename(flt):
	ori_name_lt=[]
	new_name_lt=[]
	for elem in flt:
		ori_name_lt.append(elem.oriFullName)
		new_name_lt.append(elem.fullName)
	for elem in new_name_lt:
		if new_name_lt.count(elem)>1:
			return 416
	for i in range(len(new_name_lt)):
		for j in range(i+1,len(ori_name_lt)):
			if new_name_lt[i]==ori_name_lt[j]:
				return 417
	return 0