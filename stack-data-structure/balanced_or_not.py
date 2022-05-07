from stack import Stack


def is_match(p1,p2):
    if p1=='(' and p2 == ')':
        return True
    
    if p1=='{' and p2 == '}':
        return True
    
    if p1=='[' and p2 == ']':
        return True
    
    else:
        return False

def is_ParenBalanced(string):
    is_balanced_stack = Stack()
    is_balanced = True
    index = 0
    
    
    while index < len(string) and is_balanced :
        
        if string[index] in '{[(':
            is_balanced_stack.push(string[index])
            
        else:
            if is_balanced_stack.isEmpty():
                is_balanced = False
                break
            
            else:
                top = is_balanced_stack.pop()
                if not is_match(top,string[index]) :
                    is_balanced = False
                    break
                
        index += 1
        
    if is_balanced_stack.isEmpty and is_balanced:
        return True
    
    else:
       return False 
   
   
print("String : (((({})))) Balanced or not?")
print(is_ParenBalanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_ParenBalanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_ParenBalanced("[][]"))
                    
    