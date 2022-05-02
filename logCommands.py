# SJSU CMPE 120 Spring 2022 TEAM4
def erase():
  '''Clears debug and erase files'''
  open('log4p-debug.log', 'w').close()
  open('log4p-errors.log', 'w').close()