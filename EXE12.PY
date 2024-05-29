def isValid(s):
    stack=[]
    openBracket=["(","{","["]
    for ele in s:
        if ele in openBracket:
            stack.append(ele)
        else:
            if len(stack)==0:
                return False
            elif ele==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            elif ele==']':
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            elif ele=='}':
                if stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            else:
                return False
    if len(stack)==0:
        return True
    return False
s="()[]{}"
result=isValid(s)
print(result)
