FF: 00 <- SP
FE: 00
FD: 00
FC: 00
FB: 00
FA: 00
F9: 00
F8: 00
F7: 00
F6: 00
F5: 00
F4: 00
F3: 00
F2: 00
F1: 00
F0: 00
EF: 00
.
.
.
05: 00
04: 00
03: XX
02: XX
01: XX
00: XX <- PC - our self.pc pc counter

^ Use a stack pointer to indicate beginning of stack
 -- usually stored in a dedicated register
^ Start the stack pointer at the top of memory
 -- grows down
^ Implement a stack by creating POP and PUSH functionality