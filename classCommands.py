# -*- coding:utf-8 -*-
import processFuncs
class whether_empty:
	def __init__(self,tup):
		self.__whether_str1_empty=tup[0]
		self.__whether_str2_empty=tup[1]
	@property
	def whether_str1_empty(self):return self.__whether_str1_empty
	@property
	def whether_str2_empty(self):return self.__whether_str2_empty

	def __add__(self,that):
		#--- you should judge and avoid case `-1 + 1` happening.
		return whether_empty(
			(self.whether_str1_empty | that.whether_str1_empty , self.whether_str2_empty | that.whether_str2_empty)
		)

	def __str__(self):
		dic={
			-1:'must be empty',
			0:'can be empty or not',
			1:'cannot be empty'
		}
		return 'str1 {},str2 {}'.format(dic.get(self.whether_str1_empty),dic.get(self.whether_str2_empty))

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
	@property
	def whether_str1_empty(self):return self.__whether_str12_empty.whether_str1_empty
	@property
	def whether_str2_empty(self):return self.__whether_str12_empty.whether_str2_empty
	@property
	def whether_empty(self):return self.__whether_str12_empty

	def __bool__(self):
		return bool(self.value)
 
class Command:
	def __init__(self,number=None,upLower=None,beginEnd=None,Sort=None,Quit=None,cancel=None,Help=None):
		func=lambda elem:singleCommand(elem) if elem else singleCommand('')
		self.__number=func(number)
		self.__upLower=func(upLower)
		self.__beginEnd=func(beginEnd)
		self.__sort=func(Sort)
		self.__quit=func(Quit)
		self.__cancel=func(cancel)
		self.__help=func(Help)
	@property
	def number(self):return self.__number
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
	@property
	def valueList(self):
		return (self.number,self.upLower,self.beginEnd,self.sort,self.Quit,self.cancel,self.Help)

	def is_possible(self):
		whether_str1_empty_list=[]
		whether_str2_empty_list=[]
		tup=self.valueList
		for elem in tup:
			whether_str1_empty_list.append(elem.whether_str1_empty)
			whether_str2_empty_list.append(elem.whether_str2_empty)
		if processFuncs.hasMoreThan_1_Elem_in((1,-1),whether_str1_empty_list) or processFuncs.hasMoreThan_1_Elem_in((1,-1),whether_str2_empty_list):
			return False
		return True

	def empty(self):
		return not(self.number or self.upLower or self.beginEnd or self.sort or self.Quit or self.cancel or self.Help)

	def whether_str_empty(self):
		#--- number,upLower,beginEnd,sort,quit,cancel,help
		return self.number.whether_empty+self.upLower.whether_empty+self.beginEnd.whether_empty+self.sort.whether_empty+self.Quit.whether_empty+self.cancel.whether_empty+self.Help.whether_empty

	def whether_quit(self):
		return self.Quit=='q' and self.Help==''

def makeCommand(std_order):
	getElem=processFuncs.getElem
	return Command(
		number=std_order[0] if len(std_order)>0 and std_order[0].isdigit() else  '',
		upLower=getElem('uUlL',std_order),
		beginEnd=getElem('be',std_order),
		Sort=getElem('tTsS',std_order),
		Quit=getElem('q',std_order),
		cancel=getElem('z',std_order),
		Help=getElem('h',std_order)
	)