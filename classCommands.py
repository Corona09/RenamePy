# -*- coding:utf-8 -*-
class Command:
	def __init__(self,number=None,reverse=None,upLower=None,beginEnd=None,Sort=None,Quit=None,cancel=None,Help=None):
		func=lambda elem:elem if elem else ''
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
	def __str__(self):
		return self.number+self.reverse+self.upLower+self.beginEnd+self.sort+self.Quit+self.cancel+self.Help
	
