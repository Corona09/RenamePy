# -*- coding:utf-8 -*-
# --- Written by Corona
# --- Finished on 2020-08-06
  
debugOn=True
def warning(errorCode=None):
    errorCode=errorCode if errorCode else 0
    information={
		0:'Program Processes Correctly.',
		401:'Input Includes MORE THAN 2 "\\".',
		402:'"\\" Missing.',
		403:'Inupt Length out of Limit',
		404:'Unknown Command.',
		405:'Invalid Charactor in Filename.',
		406:'Command Confilct.',
		407:'Number Repeat.',
		408:'Empty Input.',
		409:'Nothing to Operate',
		410:'Command Repeat.',
		411:'Command Missing.',
		412:'Command Order Error.',
		413:'File Names don\'t Match the Command.',
		414:'"*" Not Found.',
		415:'Too MUCH "*"!',
		416:'Conflict exists in new names.',
		417:'Conflict with original names.',
		418:'Nothing to Recover.',
		419:'Empty exists in new names.',
		420:'Meaningless Operation.',
		501:'Unknown Error.'
	}.get(errorCode)
    print('0x{err:0>6x}:{info}'.format(err=errorCode,info=information))

def debug(information):
    if not debugOn:
        return None
    print(information)