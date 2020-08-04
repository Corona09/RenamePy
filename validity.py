#-*- coding:utf-8 -*-
import error,processFuncs
validCommand='ruUlLtTsSqzhbe'
invalidNameChar='\\/:*?"<>|'
def invalidCombi_of_SortOrder(orderLt):
#---return orderAfterSep is not the valid combination of 'tTsSqzh'
#---valid combination : t/T/s/S/q/z/h/*q/h*
	if orderLt[0].isdigit():
		return 406
	if processFuncs.hasMoreThan_1_Elem_in(('t','T','s','S'),orderLt):
		return 406
	if 'z' in orderLt and len(orderLt)>1:
		return 406
	if 'h' in orderLt and len(orderLt)>2:
		return 406
	return 0

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