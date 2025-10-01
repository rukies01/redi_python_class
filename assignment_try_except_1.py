#PROBLEM
# Students MUST NOT change this map
data = {
    "name": "Ali",
    "age": "twenty",
    "numbers": [1, 2],
    "divisor": 0
}

def process_data(d):
    # 1) Accessing missing key
    city = d["city"]

    # 2) Wrong type conversion
    age = int(d["age"])

    # 3) Index out of range
    third_number = d["numbers"][2]

    # 4) Division by zero
    result = 10 / d["divisor"]

    print("Result is:", result)


#process_data(data)

#print("Program finished successfully!")

#SOLUTION TO PROBLEM
# Students MUST NOT change this map
data = {
    "name": "Ali",
    "age": "twenty",
    "numbers": [1, 2],
    "divisor": 0
}

def process_data(d):
    # 1) Accessing missing key
    try:           # try to run the code beloe
        city = d["city"]
    except KeyError:
        city = 'not found'
        print("Warning: 'city' not found")

    # 2) Wrong type conversion
    try:
        age = int(d["age"])
    except ValueError:
        age = None
        print("Warning 'age' is no a number")

    # 3) Index out of range
    try:
       third_number = d["numbers"][2]
    except IndexError:
        third_number = 'does not exist'
        print(" 'third numbr' does not exist")

    # 4) Division by zero
    try:
       result = 10 / d["divisor"]
    except ZeroDivisionError:
        ZeroDivisionError
        result = None
        print('Encouter div by zero')

    print("Result is:", result)


process_data(data)

print("Program finished successfully!")
