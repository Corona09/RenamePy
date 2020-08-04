#-*- coding:utf-8 -*-
import error
def judgeRaw(raw):
	tmp=raw.split('\\')
	if len(tmp)>3:
		return 401
	if len(tmp)<1:
		return 402
	return 0
def judgeValid(str1,str2,command):
	
	return 0