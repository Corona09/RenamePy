#-*- coding -*-
debugOn=True
def warning(errorCode=None):
    errorCode=errorCode if errorCode else 0
    information={
		0:'All Correct.',
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
		501:'Unknown Error.'
	}.get(errorCode)
    print('{err:0>6d}:{info}'.format(err=errorCode,info=information))
def debug(information):
    if not debugOn:
        return None
    print(information)