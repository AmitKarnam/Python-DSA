from numpy import binary_repr
from stack import Stack

def decimal_to_binary(dec_num):
    
    binary_nos_stack = Stack()
    binary_nos = ""
    
    while(dec_num!=0):
        binary_nos_stack.push((dec_num%2))
        dec_num = dec_num//2
        
    
    while not binary_nos_stack.isEmpty():
        binary_nos += str(binary_nos_stack.pop())
        
    return binary_nos


decimal_number = int(input("Enter the decimal number : "))
binary_number = decimal_to_binary(decimal_number)

print('Binary of {} is {}'.format(decimal_number,binary_number))