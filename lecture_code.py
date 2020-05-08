# let's write a basic computer
import sys

# OP (operation) Codes
PRINT_IAN = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4
PRINT_REGISTER = 5
ADD = 6

print_ian_program = [
    PRINT_IAN,
    PRINT_IAN,
    PRINT_IAN,
    PRINT_IAN,
    HALT,
]

print_some_nums = [
    PRINT_NUM,
    19,
    PRINT_NUM,
    15,
    PRINT_NUM,
    37,
    PRINT_IAN,
    HALT,
]

save_num_to_reg = [
    # Save -- Value -- Registry number
    SAVE,
    65,
    2,
    PRINT_REGISTER,
    2,
    SAVE,
    145669828,
    6,
    PRINT_REGISTER,
    2,
    PRINT_REGISTER,
    6,
    HALT,
]

add_two_nums = [
    SAVE,  # save num 12 to reg 1
    12,
    1,
    SAVE,  # save num 45 to reg 2
    45,
    2,
    # reg[1] += reg[2] (add the two values storing the result in the first register)
    ADD,
    1,
    2,
    PRINT_REGISTER,
    1,
    SAVE,
    10,
    2,
    ADD,
    1,
    2,
    PRINT_REGISTER,
    1,
    HALT,
]

memory = [0] * 256
registers = [0] * 8
running = True
pc = 0

# Read from file, and load into memory
# Read the filename from command line arguments
# open file, load each line into memory
# try not to crash


def load_program():
    address = 0
    # get the arguments
    arguments = sys.argv
    # check to make sure there is an argument
    if len(arguments) < 2:
        print('Need proper filename passed')
        sys.exit(1)
    # extract filename from arguments
    filename = arguments[1]
    # open the file
    with open(filename) as f:
        for line in f:
            if line == '':
                continue
            # split the line into a list containing everything before # in [0] and everything after # in [1]
            comment_split = line.split('#')
            # extract num from comment_split
            num = comment_split[0].strip()
            # set in memory
            memory[address] = int(num)
            # int can take a 2nd argument for base, to convert this to binary use int(line, 2)
            # increment address
            address += 1


load_program()


while running:
    # lets do some things
    # lets receive some instructions and execute them
    # command = ??
    command = memory[pc]

    # if command is PRINT_IAN
    if command == PRINT_IAN:
        # print out Ian's name
        print('Ian!')
        pc += 1
    # if command is PRINT_NUM
    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2
    # if command is SAVE
    elif command == SAVE:
        # Pull the value we intend to save from the next place in memory
        num_to_save = memory[pc + 1]
        # Pull the REG_NUM from the following place in memory
        register = memory[pc + 2]
        # Save the value in the register
        registers[register] = num_to_save
        pc += 3
    # if command is PRINT_REGISTER
    elif command == PRINT_REGISTER:
        # pull the location from next line
        register = memory[pc + 1]
        # print from registry
        print(registers[register])
        pc += 2
    # if command is ADD
    elif command == ADD:
        register1 = memory[pc + 1]
        register2 = memory[pc + 2]
        val1 = registers[register1]
        val2 = registers[register2]
        registers[register1] = val1 + val2
        pc += 3
    # if command is HALT
    elif command == HALT:
        # shutdown
        running = False
        pc += 1
    # if command is non-recognizable
    else:
        # error message
        print(f'Unknown instruction {command}')
        # crash
        sys.exit(1)
