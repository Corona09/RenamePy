#-*- coding:utf-8 -*-
import error
def splitRaw(raw):
	raw=raw.split('\\')
	str1=raw[0]
	str2=raw[1]
	command='' if len(raw)<3 else raw[2]
	return tuple(str1,str2,command)
def mainProcess(str1,str2,command):
	return