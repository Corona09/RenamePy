#-*- coding:utf-8 -*-
import procedure, validity
count=1
while True:
	count+=1
	raw=input() #--- to get the original operation order :str1\str2[\command]
	if validity.judgeRaw(raw):
		continue
	str1,str2,command=procedure.splitRaw(raw)
	if validity.judgeValid(str1,str2,command):
		continue
	procedure.mainProcess(str1,str2,command)
	if command.Quit=='q':
		break