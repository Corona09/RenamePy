#-*- coding:utf-8 -*-
import error,procedure, validity
count=1
while True:
	count+=1
	raw=input() #--- to get the original operation order :str1\str2[\command]
	errCode=validity.notValid(raw)
	if errCode:
		error.warning(errCode)
		continue
	str1,str2,command=procedure.splitRaw(raw)
	if procedure.mainProcess(str1,str2,command):#---func rturn True when need to do '\q'
		break