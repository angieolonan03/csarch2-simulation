decimal = input("Input: ")
decimal_int = int(decimal)

#This line calculates the absolute value of decimal_int, converts it to binary using the built-in bin() function, and removes the prefix "0b" 
#by slicing from the 3rd character onward (i.e., [2:]). The resulting binary value is assigned to the binary variable as a string.
binary= bin(abs(decimal_int))[2:] #convert absolute value of decimal to binary

def valid_binary(input):
    # check if input is valid binary number
    if not all(char in '01' for char in input):
        return False
    # check if input is integer (either binary or decimal format)
    try:
        int(input, 2)
        return True
    except ValueError:
        try:
            int(input)
            return True
        except ValueError:
            return False
        
 def valid_decimal(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

def decToBin(num):
    return bin(abs(num))[2:]

def binToDec(binary):
    if not valid_binary(binary):
        return "Invalid binary input"
    return int(binary, 2)

#This is a function that takes a binary string num and calculates its two's complement. 
#It first initializes a boolean variable foundOne to False. 
#Then it loops through the num string in reverse order using the reversed() and range() functions. 
#If it encounters a '1' digit and foundOne is False, it sets foundOne to True. If it encounters a '1' 
#digit and foundOne is True, it changes the digit to '0'. If it encounters a '0' digit and foundOne is True, it changes the digit to '1'.
def twosComp(num):
    #convert binary string to list of integers
    binary_list = list(map(int, num))
    
    foundOne = False # boolean
     # iterate through binary digits in reverse order
    for x in reversed(range(len(binary_list))):
        if binary_list[x] == 1 and not foundOne:
            foundOne = True
        elif binary_list[x] == 1 and foundOne:
            binary_list[x] = 0
        elif binary_list[x] == 0 and foundOne:
            binary_list[x] = 1
            
    # convert list of integers back to binary string
    return ''.join(map(str, binary_list))

options = {
    "1": (decToBin, "Decimal to binary"),
    #"2": (binToDec, "Binary to decimal"), not yet made
    "3": (twosComp, "Two's complement")
}

mode = input("Mode (1: Decimal to binary, 2: Binary to decimal, 3: Two's complement): ")

if decimal_int < 0:  # input is negative
    binary = decToBin(abs(decimal_int))  # get positive of input
    binary = twosComp(binary)
else:  # input is positive
    binary = decToBin(decimal_int)

if mode == "2":  # binary to decimal
    print(binToDec(decimal))
else:
    print(binary)
