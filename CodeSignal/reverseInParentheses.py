def reverseInParentheses(inputString):
    stack = []
    for x in inputString:
        if x == ")":
            tmp = ""
            while stack[-1] != "(":
                tmp += stack.pop()
                print("temp", tmp)
            stack.pop() # pop the (
            for item in tmp:
                stack.append(item)
                print("stack", stack)
        else:
            stack.append(x)
            print("stack else", stack)

    return "".join(stack)
    

inputString = "foo(bar)baz(blim)"
inputString2 = "foo(bar(baz))blim"
# print(inputString, reverseInParentheses(inputString))
print(inputString2, reverseInParentheses(inputString2))