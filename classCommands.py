# -*- coding:utf-8 -*-
class Command:
    def __init__(self,number=None,reverse=None,upLower=None,beginEnd=None,Sort=None,quit=None,cancel=None,help=None):
        func=lambda elem:elem if elem else ''
        self.__number=func(number)
        self.__reverse=func(reverse)
        self.__upLower=func(upLower)
        self.__beginEnd=func(beginEnd)
        self.__sort=func(Sort)
        self.__quit=func(quit)
        self.__cancel=func(cancel)
        self.__help=func(help)
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
    def quit(self):return self.__quit
    @property
    def cancel(self):return self.__cancel
    @property
    def help(self):return self.__help
    
    def __str__(self):
        return ''

a=Command()
print(a)
