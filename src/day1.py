# Day 1 of the 2023 Advent of Code
import re

def findNum(line):
    word = ""
    for letter in line:
        if letter.isdigit(): return letter
        elif letter.isalpha():
            word+=letter
            for key in num_dict.keys():
                if key in word: return num_dict[key]

def findRevNum(line):
    word = ""
    for letter in line[::-1]:
        if letter.isdigit(): return letter
        elif letter.isalpha():
            word+=letter
            for key in num_dict.keys():
                if key[::-1] in word: return num_dict[key]

# Read input file
with open("../include/input1.inc","r") as calibration_file:
    calibration_list = list(map(lambda a: a.strip(),calibration_file.readlines()))

########################### Part 1 ###########################
cal_val = 0
for line in calibration_list:
    digit_list = re.findall("[0-9]",line)
    cal_val += int(digit_list[0]+digit_list[-1])
print("Part1: %s"%cal_val)

########################### Part 2 ###########################
num_dict = {"one":"1",
            "two":"2",
            "three":"3",
            "four":"4",
            "five":"5",
            "six":"6",
            "seven":"7",
            "eight":"8",
            "nine":"9"}

cal_val = 0
for line in calibration_list:
    init = findNum(line)
    last = findRevNum(line)
    cal_val += int(init+last)
print("Part2: %s"%cal_val)