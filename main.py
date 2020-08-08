 # -*- coding:utf-8 -*-
# --- Written by Corona
# --- Finished on 2020-08-06
 
import error,procedure,validity,classCommands,processFuncs

name_log=[]
count=1
procedure.display(0)
while True:
	procedure.display(count)
	count=count+1
	raw=input('Please input your operation:') # --- to get the original operation order :str1\str2[\command]
	errCode=validity.notValid(raw)
	if errCode:
		error.warning(errCode)
		continue
	str1,str2,order=procedure.splitRaw(raw)
	if procedure.mainProcess(str1,str2,order,name_log):# --- Function return True if the program need to quit(\q).
		break