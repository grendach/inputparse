#!/usr/bin/python3
import sys
import random
import json

from functools import reduce

input_data = (sys.argv[1:])
digit_list = []
json_list = []
key_list = ["InputNumber1","InputNumber2", "InputNumber3", "InputNumber4", "InputNumber5", "InputNumber6" ]

def print_header():
    header = """
    Choose options from menu below(1 to 5):
    _____________________________________________________
    1. Perform subtraction
    2. Perform multiplication and store result in a JSON
    3. Pick randomly a number
    4. Print sorted (highest to lowest)
    5. Print sorted (lowest to highest)
    x. Exit
    _____________________________________________________
    Please make your choise, from 1 to 5 or x):
    """
    print(header)

# Function to multiplication and store result in a JSON file
def json_mult(list):
    
    for i in range(len(input_data)):
        json_list.append(json.dumps({key_list[i]:digit_list[i]}))
    json_list.append(json.dumps({"Multiplication":reduce(lambda x,y: x*y, digit_list)}))
    with open('json_report.json', 'w') as outfile:
        json.dump(json_list, outfile)
    print(json_list)


if len(input_data) != 6:
    raise Exception("You should pass 6 digits to your program") 
else:
    for i in input_data:
        digit_list.append(int(i))
    print("You've entered: ", digit_list)
    
while True:
    print_header()
    cmd = input(">")
    if cmd == "1":
        print("Perform elements subtractions: ", reduce(lambda x,y: x-y, digit_list))
    elif cmd == "2":
        json_mult(digit_list)
    elif cmd == "3":
        print("Rundom number is: ", random.choice(digit_list))
    elif cmd == "4":
        print("Highest to lowest order is: ", sorted(digit_list, reverse=True))
    elif cmd == "5":
        print("Lowest to highest order is: ", sorted(digit_list))
    elif cmd == "x":
        print("Bye-bye")
        break
    else:
        print("!!!ERROR!!!\nWrong parameter, please choose again...")



            