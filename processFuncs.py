#-*- coding:utf-8 -*-
import error
def hasMemNot_in(lt1,lt2):
	for elem in lt1:
		if elem not in lt2:
			return True
	return False