#-*- coding:utf-8 -*-
import procedure, validity
count=1
while True:
	count+=1
	str1,str2,command=procedure.getRawOperation() #--- to get the original operation order :str1\str2[\command]
	if not validity.judgeValide(str1,str2,command):
		continue
	procedure.do(str1,str2,command)
	if command.quit():
		break