from stack import Stack
def reverse_string(user_str):
    
    str_reverse_stack = Stack()

    for ch in user_str:
        str_reverse_stack.push(ch)
    
    reversed_str = ""

    while not str_reverse_stack.isEmpty():
        reversed_str += str_reverse_stack.pop()
    
    print("Reversed user string : {}".format(reversed_str))
    

user_str = input("Enter the string to be reversed : ")
reverse_string(user_str)