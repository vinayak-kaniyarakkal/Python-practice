def palindrome(string):
    for i in range (0, len(string)/2):
        if string[i] is not string[-i-1]:
            return False
            break
    else:
        return True

def pangram(sentence):
    for i in "qwertyuiopasdfghjklzxcvbnm":
        if i not in sentence.lower():
            return False
    return True

def letter_freq(string):
    d = dict()
    for i in string.lower():
        if i not in d.keys():
            d[i] = 0
        else:
            pass
        d[i] = d[i]+1
    return d

def evaluate_postfix(expression):

    stack = []

    for i in expression:
        if i.isdigit():
            stack.append(int(i))
        elif i is "*":
            stack = stack[:-2] + [stack[-1] * stack[-2]]
        elif i is "+":
            stack = stack[:-2] + [stack[-1] + stack[-2]]
        elif i is "-":
            stack = stack[:-2] + [stack[-1] - stack[-2]]
        elif i is "/":
            stack = stack[:-2] + [stack[-1] / stack[-2]]
        else:
            print "Unable to evaluate postfix"
            return False

    return stack[0]                                                            
