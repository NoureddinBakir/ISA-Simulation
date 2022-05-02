# SJSU CMPE 120 Spring 2022 TEAM4
def execute(instruction, registers, memory):
  '''
    Takes in array of encoded instruction [opcode, rs,rt,rd] array and register array
    returns new register array outcome
  '''
  
  if(instruction[0] == 'R'):
    
    if instruction[1] == 'add':
      registers[int(instruction[2])-1] = registers[int(instruction[3])-1] + registers[int(instruction[4])-1]
    
    if instruction[1] == 'sub':
      registers[int(instruction[2])-1] = registers[int(instruction[3])-1] - registers[int(instruction[4])-1]

    if instruction[1] == 'lw':
      registers[int(instruction[2])-1] = memory[int(instruction[3])-1]
    
    if instruction[1] == 'sw':
      memory[int(instruction[2])-1] = registers[int(instruction[3])-1]

    if instruction[1] == 'and':
      registers[int(instruction[2])-1] = registers[int(instruction[3])-1] & registers[int(instruction[4])-1]
    
    if instruction[1] == 'or':
      registers[int(instruction[2])-1] = registers[int(instruction[3])-1] | registers[int(instruction[4])-1]
    
    if instruction[1] == 'beq':
      registers[int(instruction[2])-1] = registers[int(instruction[3])-1] == registers[int(instruction[4])-1]
    
  
  if(instruction[0] == 'I'):
    
    if instruction[1] == 'add':
      registers[int(instruction[2])-1] = registers[int(instruction[2])-1] + int(instruction[3])
      
    if instruction[1] == 'sub':
      registers[int(instruction[2])-1] = registers[int(instruction[2])-1] - int(instruction[3])
      
    if instruction[1] == 'sw':
      memory[int(instruction[2])-1] = int(instruction[3])

  return [registers, memory]