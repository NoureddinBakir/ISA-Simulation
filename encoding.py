# SJSU CMPE 120 Spring 2022 TEAM4
import binaryEncoding

def encodeToMachineCode(instruction):
  '''
    method parses instruction string, and 
    returns an array of machine language
  '''
  fields   =     instruction.replace(',','').split()
  type     =     binaryEncoding.convert(fields[0])
  if fields[0] == 'R':
    opcode   =     binaryEncoding.convert(fields[1])
    rs       =     binaryEncoding.convert(fields[2])
    rt       =     binaryEncoding.convert(fields[3])
    rd       =     binaryEncoding.convert(fields[4])
  elif fields[0] == 'I':
    opcode   =     binaryEncoding.convert(fields[1])
    rs       =     binaryEncoding.convert(fields[2])
    rt       =     bin(int(fields[3]))[2:].zfill(6)
    rd       =     '00000000'.zfill(6)
  elif fields[0] == 'J':
    opcode   =     bin(int(fields[1]))[2:].zfill(6)
    rs       =     '00000000'.zfill(6)
    rt       =     '00000000'.zfill(6) 
    rd       =     '00000000'.zfill(6)
    

  return [type, opcode, rs, rt, rd]

def encode(instruction):
  '''
    method parses instruction string, and 
    executes instruction
  '''
  fields   =     instruction.replace(',','').split()
  type     =     fields[0]
  if type == 'R':
    opcode   =     fields[1]
    rs       =     fields[2][1:]
    rt       =     fields[3][1:]
    rd       =     fields[4][1:]
  elif type == 'I':
    opcode   =     fields[1]
    rs       =     fields[2][1:]
    rt       =     fields[3]
    rd       =     '00000000'.zfill(6)
  elif type == 'J':
    opcode   =     fields[1]
    rs       =     '00000000'.zfill(6)
    rt       =     '00000000'.zfill(6) 
    rd       =     '00000000'.zfill(6)

  return [type, opcode, rs, rt, rd]