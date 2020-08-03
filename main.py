#-*- coding:utf-8 -*-
import procedure,validity,error
procedure.copyright()
count=1
fChainLt=procedure.initFCL()
while True:
	procedure.display(count)
	count+=1
	while True:
		str1,str2,command=procedure.getRawOperation()
		if validity.check():
			continue
		break
	if not 
