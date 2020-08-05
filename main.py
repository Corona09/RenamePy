#-*- coding:utf-8 -*-
import error,procedure,validity,classCommands
count=1
procedure.display(0)
while True:
	procedure.display(count)
	count=count+1
	raw=input('Please input your operation:') #--- to get the original operation order :str1\str2[\command]
	errCode=validity.notValid(raw)
	if errCode:
		error.warning(errCode)
		continue
	str1,str2,order=procedure.splitRaw(raw)
	if procedure.mainProcess(str1,str2,order):#---func rturn True when need to do '\q'
		break