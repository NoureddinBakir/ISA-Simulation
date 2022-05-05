# Instruction Set Architecture Simulator
#### Based off of the MIPS ISA

---
![Processor Diagram](/processor_diagram.png)
---

## 🚀 How to run the program
1. First install the necessary libraries
    * Enter into the program directory & enter `pip install log4p`
2. Run the software
    * To run the software: enter into the program directory & type
`python3 main.py`

## ⚙️ How to use ISA Simulator
### Exiting the CLI and Clearing Logs
* Enter `END` to end the CLI
* Enter `ERASE` to erase the logs
### Addresses & Important Remarks
* Registers R1-R16
  * R16 is the Program Counter (increments by 32 ever instruction)
* Data memory: M1-M16
* Instruction Array
  * Stores instructions once `LOOP` is entered
  * Stops storing instrucitons once `END LOOP` is entered
  * Once `END LOOP` is entered, the stored instructions are executed once
  * It is by design to ask the programmer to execute the loop again by re-entering `END LOOP`
  * We have reserved R16 as the beq stored value, use this register for beq as specified below

### R-type Instructions
* add
  * `R add R1, R2, R3`
* sub
  * `R sub R1, R2, R3`
* lw
  * `R lw R1, M2, R14` # R14 is a placeholder
* sw
  * `R sw M1, R2, R14` # R14 is a placeholder
* and
  * `R and R1, R2, R3` # R1 = R2 & R3
* or
  * `R or M1, R2, R15` # R1 = R2 | R3
* beq
  * `R beq R16, R2, R3` # R1 = 0 if (R2 == R3) else 1

### I-type Instructions
* add
  * `R add R1, Imm` # Immediate value between (-64) - 63 decimal values
* sub
  * `R sub R1, Imm` # Immediate value between (-64) - 63 decimal values
* sw
  * `I sw M1, Imm` # Immediate value between (-64) - 63 decimal values
### J-type Instructions
* Given the scope of this project and the implementation of LOOP and the Instruction Array, J-type instructions provide little to no value, hence it has been discarded

## ✅ Demo
### The following High-Level-Code is represented by the assembly code below

```
int A[1024];
int sum = 0;
for(i=0; i<1024; i++){
  sum += A[i];
}
```
First, we store any values we want within Data memory, treating it as the array A by using

```
I sw M(1-16), (value)
```
* `Assume array of [5,5,5,5,5,5]`

Initiate the loop:
```
LOOP
```
Then we use R15 as the 'stack pointer' but it instead points to the value of the memory element location

```
I add R15, 1
```

Then we load each value of M(1-16) into R2

```
R lw R2, M(1-16), R14
```

Add the value of R2 to R1

```
R add R1, R1, R2
```
Ende the loop

```
END LOOP
```

` ! Manually iterate loop `