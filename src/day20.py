# Day 20 of the 2023 Advent of Code
class FlipFlop():
    def __init__(self,id,outsig):
        self.id = id
        self.outsig = outsig
        self.status = 0
    def recievePulse(type):
        if type == "low":
            self.status = 1 - self.status
            return self.status

class Conjunction():
    def __init__(self,id,outsig):
        self.id = id
        self.memory = {}
        self.outsig = outsig
    def recievePulse(type,insig):
        self.memory[insig] = type
        if all(self.memory): return 0
        else: return 1

def pushButton(num_push):
    for push in range(num_push):
        for device in instruction_order:

# Read input file
with open("../include/example20.inc","r") as connection_file:
    connection_list = connection_file.read().split("\n")

########################### Part 1 ###########################
flipflop_dict = {}
conjunction_dict = {}
instruction_order = []
for net in connection_list:
    [input,output] = net.split(" -> ")
    prefix = input[0]
    id = input[1:]
    if prefix == "%": flipflop_dict[id] = FlipFlop(id,output)
    elif prefix == "&": conjunction_dict[id] = Conjunction(id,output)
    elif prefix == "b": broadcaster_list = output
    instruction_order.append(id)
print("Part 1: %s"%pushButton(1000))