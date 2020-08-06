#-*- coding:utf-8 -*-
import error,classFile

class log_list:
	def __init__(self):
		self.lists=[]
	def __str__(self):
		result=''
		if not self.lists:
			return result
		for i in range(len(self.lists)):
			result+=self.lists[i]
			if i!=len(self.lists)-1:
				result+=' -> '
		return result
	def append(self,file_name):
		self.lists.append(file_name)
	def pop(self):
		del a[len(a)-1]
	def back(self):
		return self.lists[len(self.lists)-1] if self.lists else None
	

def update(name_list,flt):
	changed=False
	for elem in flt:
		if elem.oriFullName!=elem.fullName:
			changed=True
			break
	if changed:
		if not name_list:
			for i in range(len(flt)):
				name_list.append(log_list())
			for i in range(len(flt)):
				name_list[i].append(flt[i].oriFullName)
				name_list[i].append(flt[i].fullName)
		else:
			pushed_list=[]

			for i in range(len(flt)):
				for j in range(len(flt)):
					if name_list[j].back()==flt[i].oriFullName and j not in pushed_list:
						name_list[j].append(flt[i].fullName)
						pushed_list.append(j)
		
