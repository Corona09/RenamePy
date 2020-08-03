#-*- coding -*-
debugOn=True
def warning(errorCode=None,information=None):
    errorCode=errorCode if errorCode else 0
    information=information if information else ''
    print('0x{err:0>6x}:{info}'.format(err=errorCode,info=information))
def debug(information):
    if not debugOn:
        return None
    print(information)