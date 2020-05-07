"""CPU functionality."""

import sys

# OP CODES
HLT = 0b00000001  # Halt function, if HLT is encountered running = False
LDI = 0b10000010  # SAVE function
PRN = 0b01000111  # PRINT function


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.CPU = {}
        self.ram = [0] * 8
        self.reg = [0] * 8
        self.pc = 0
        self.running = False

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def ram_read(self, pc_num):
        return(self.ram[pc_num])

    def ram_write(self, value, pc_num):
        print(value, pc_num)
        self.ram[pc_num] = value

    def run(self):
        """Run the CPU."""
        INSTRUCTION_REGISTER = None
        # inst_inc = 0
        self.running = True

        while self.running:
            self.trace()
            # Add our instruction to the instruction register from ram
            INSTRUCTION_REGISTER = self.ram[self.pc]
            # Extract the command
            COMMAND = INSTRUCTION_REGISTER
            # print(COMMAND)

            # Execution Loop #

            # if our command is HALT
            if COMMAND == HLT:
                # shutdown
                self.running = False
                self.pc += 1
            # if our command is LDI (save)
            elif COMMAND == LDI:
                # get the value to be saved from ram
                val_to_save = self.ram[self.pc + 2]
                # get destination from ram
                destination = self.ram[self.pc + 1]
                # save_to_ram
                self.reg[destination] = val_to_save
                # increment pc
                self.pc += 3
            # if command is PRN (print)
            elif COMMAND == PRN:
                # get reg location of value to print
                reg_loc = self.ram[self.pc + 1]
                # get value to print
                val_to_print = self.reg[reg_loc]
                # print it
                print(f'PRINTING REQUESTED VALUE: {val_to_print}')
                # increment pc
                self.pc += 2
            # if command is unrecognized
            else:
                # error message
                print(f'Unknown instruction{COMMAND}')
                # crash
                sys.exit(1)
