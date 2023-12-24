# Day 20 of the 2023 Advent of Code
class Device():
    def __init__(self,type,id,outs):
        self.type = type
        self.id = id
        self.outs = outs
        if type == "%": self.status = 0
        elif type == "&": self.memory = {}
    def recievePulse(self,origin,pulse):
        if self.type == "%":
            if pulse == 0:
                self.status = 1 - self.status
                instruction_queue.append((self.id,self.status))
        elif self.type == "&":
            self.memory[origin] = pulse
            if all(self.memory.values()) == 1: val = 0
            else: val = 1
            instruction_queue.append((self.id,val))
        elif self.type == "b": instruction_queue.append((self.id,pulse))

def createDevices():
    device_dict = {}
    for net in connection_list:
        [input,output] = net.split(" -> ")
        prefix,id = input[0],input[1:]
        device_dict[id] = Device(prefix,id,output.split(", "))
    device_dict["utton"] = Device("b","utton",["roadcaster"])
    device_dict["rx"] = Device("o",output,None)
    for net in connection_list:
        [input,output] = net.split(" -> ")
        prefix,id = input[0],input[1:]
        for each in output.split(", "):
            if device_dict[each].type == "&": device_dict[each].memory[id] = 0
    return device_dict

def pushButton(high_count,low_count,dev):
    instruction_queue.append(("utton",0))
    while instruction_queue:
        origin,pulse = instruction_queue.pop(0)
        for out in device_dict[origin].outs:
            device_dict[out].recievePulse(origin,pulse)
            if pulse == 1: high_count += 1
            elif pulse == 0: low_count += 1
            if dev and out == dev:
                if pulse == 1: return True
    return high_count,low_count

def pushSequence(num_push):
    high_count,low_count = 0,0
    if isinstance(num_push,int):
        for _ in range(num_push): high_count,low_count = pushButton(high_count,low_count,None)
        return high_count*low_count
    else:
        foundDev = False
        push_count = 0
        while not foundDev:
            if pushButton(0,0,num_push): foundDev = True
            push_count += 1
        print(push_count)
        return push_count

# Read input file
with open("../include/input20.inc","r") as connection_file:
    connection_list = connection_file.read().split("\n")

########################### Part 1 ###########################
device_dict = createDevices()
instruction_queue = []
print("Part 1: %s"%pushSequence(1000))

########################### Part 2 ###########################
check_dict = {}
for dev in device_dict:
    if "rx" in device_dict[dev].outs: check_dict[dev] = pushSequence(dev)
#print("Part 2: %s"%pushSequence(0))