# SJSU CMPE 120 Spring 2022 TEAM4
import log4p # import log4p
import logCommands # includes erase(), ...
import encoding
import instructionExecution

# initialize logger
logger = log4p.GetLogger(__name__)
log = logger.logger

# initialize local variables
instruction = ''
registers = [0]*(16) # Initialize the register
memory = [0]*(16) # Initialize the memory
instructionArray = [] # Initialize the Instruction array
loop = False # boolean determines when to store instructions

# instruction read, continuious, 'END' will end
while(instruction != 'END'):
  
  instruction = input("Enter code:") # Prompt
  if instruction == 'ERASE': # Clears logs
    logCommands.erase()

  elif instruction == 'LOOP':
    loop = True
  elif instruction == 'END LOOP':
    loop = False

    for ins in instructionArray:
      # Log the input immediately
      log.debug(f'Instruction: {ins}') 
      # Show machine code for each instruction
      print(f'Machine Code: {encoding.encodeToMachineCode(ins)}')
  
      # Program counter increments by 32 bits
      registers[15] += 32 
    
      # Execute the code, store value into an array
      results = instructionExecution.execute(encoding.encode(ins), registers, memory)
      
      registers = results[0]
      memory = results[1]
      
      print('Registers: ' + str(registers))
      print('Memory:    ' + str(memory))
    
    # instruction = 'END' # Design choice
  elif instruction != 'END':
    
    if loop:
      instructionArray.append(instruction)
    
    # Log the input immediately
    log.debug(f'Instruction: {instruction}') 
    # Show machine code for each instruction
    print(f'Machine Code: {encoding.encodeToMachineCode(instruction)}')

    # Program counter increments by 32 bits
    registers[15] += 32 
  
    # Execute the code, store value into an array
    results = instructionExecution.execute(encoding.encode(instruction), registers, memory)
    
    registers = results[0]
    memory = results[1]
    
    print('Registers: ' + str(registers))
    print('Memory:    ' + str(memory))