# -*- coding:utf-8 -*-
class whether_empty:
	def __init__(self,tup):
		self.__whether_str1_empty=tup[0]
		self.__whether_str2_empty=tup[1]
	@property
	def whether_str1_empty(self):return self.__whether_str1_empty
	def whether_str2_empty(self):return self.__whether_str2_empty

	def __add__(self,that):
		ansTup=(1,1)
		if self.whether_str1_empty
class singleCommand:
	def __init__(self,sinCommand):
		self.__value=sinCommand
		self.__whether_str12_empty=whether_empty({
			#--- -1 : must be empty
			#--- 0 : empty or not are both allowed
			#--- 1 : cannot be empty
			#--- up&lower command
			'u':(1,0),
			'l':(1,0),
			'U':(0,0),
			'L':(0,0),
			#--- begin&end command
			'e':(1,0),
			'b':(1,0),
			#---sort command
			't':(-1,0),
			'T':(-1,0),
			's':(-1,0),
			'S':(-1,0),
			#---function command
			'q':(0,0),
			'z':(-1,-1),
			'h':(-1,-1),
			#---empty command:
			'':(0,0)
		}.get(sinCommand,(1,0)))
	@property
	def value(self):return self.__value
	def whether_str1_empty(self):return self.__whether_str12_empty.whether_str1_empty
	def whether_str2_empty(self):return self.__whether_str12_empty.whether_str2_empty
	def whether_empty(self):return self.__whether_str12_empty

	def __bool__(self):
		return bool(self.value)

class Command:
	def __init__(self,number=None,reverse=None,upLower=None,beginEnd=None,Sort=None,Quit=None,cancel=None,Help=None):
		func=lambda elem:singleCommand(elem) if elem else singleCommand('')
		self.__number=func(number)
		self.__reverse=func(reverse)
		self.__upLower=func(upLower)
		self.__beginEnd=func(beginEnd)
		self.__sort=func(Sort)
		self.__quit=func(Quit)
		self.__cancel=func(cancel)
		self.__help=func(Help)
	@property
	def number(self):return self.__number
	@property
	def reverse(self):return self.__reverse
	@property 
	def upLower(self):return self.__upLower
	@property
	def beginEnd(self):return self.__beginEnd
	@property
	def sort(self):return self.__sort
	@property
	def Quit(self):return self.__quit
	@property
	def cancel(self):return self.__cancel
	@property
	def Help(self):return self.__help
	
	def empty(self):
		return not(self.number or self.reverse or self.upLower or self.beginEnd or self.sort or self.Quit or self.cancel or self.Help)

	def whether_str_empty(self):
		pass