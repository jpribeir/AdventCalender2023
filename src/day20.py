# Day 20 of the 2023 Advent of Code
class Device():
    def __init__(self,type,id,outsig):
        self.type = type
        self.id = id
        self.outsig = outsig
        if type == "%": self.status = 0
        elif type == "&": self.memory = {}
    def recievePulse(val):
        if self.type == "%":
            if type == "low": self.status = 1 - self.status
        elif self.type == "&":
            

def pushButton(num_push):
    for push in range(num_push):
        for device in instruction_order:

# Read input file
with open("../include/example20.inc","r") as connection_file:
    connection_list = connection_file.read().split("\n")

########################### Part 1 ###########################
device_dict = {}
instruction_order = []
for net in connection_list:
    [input,output] = net.split(" -> ")
    prefix,id = input[0],input[1:]
    device_dict[id] = Device(prefix,id,output)
    instruction_order.append(input)
print("Part 1: %s"%pushButton(1000))