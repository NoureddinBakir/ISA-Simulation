import log4p # import log4p
import logCommands # includes erase(), ...

# initialize logger
logger = log4p.GetLogger(__name__)
log = logger.logger

instruction = ''

# instruction read, continuious, 'END' will end
while(instruction != 'END'):
  
  instruction = input("Enter code:") # Prompt
  log.debug(f'Instruction: {instruction}') # Log each instruction
  
  if instruction == 'ERASE': # Clears logs
    logCommands.erase()