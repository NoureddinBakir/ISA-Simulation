# SJSU CMPE 120 Spring 2022 TEAM4
def convert(instruction):
  '''
    Method returns the binary machine code equivalent to each instruction
  '''
  conversionDictionary = {
    'I'      :   '01'.zfill(2),
    'R'      :   '10'.zfill(2),
    'J'      :   '11'.zfill(2),
    'add'    :   '000001'.zfill(6),
    'sub'    :   '000010'.zfill(6),
    'sw'     :   '000011'.zfill(6),
    'lw'     :   '000100'.zfill(6),
    'jump'   :   '000101'.zfill(6),
    'and'    :   '000110'.zfill(6),
    'or'     :   '000111'.zfill(6),
  }
  
  def registerValue(str):
    return bin(int(str[1:]))[2:].zfill(6)

  return conversionDictionary[instruction] if instruction.isalpha() else registerValue(instruction)