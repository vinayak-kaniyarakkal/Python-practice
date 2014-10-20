from excercises import palindrome,pangram,letter_freq,evaluate_postfix

def test_palindrome():
    assert palindrome("malayalam") == True
    assert palindrome("abba") == True
    assert palindrome("b") == True
    assert palindrome("something") == False
    
def test_pangram():
    assert pangram("The quick brown fox jumps over the lazy dog") == True
    assert pangram("Sphinx of black quartz, judge my vow") == True
    assert pangram("humpty dumpty sat on a wall") == False
    assert pangram("abcdefghijklmnopqrstuvwxyz") == True
    
def test_letter_freq():
    d = letter_freq ("she sells sea shells on the sea shore")
    assert d['a'] == 2
    assert d[' '] == 7
    assert d['e'] == 7
    assert d['h'] == 4
    assert d['l'] == 4
    assert d['o'] == 2
    assert d['n'] == 1
    assert d['s'] == 8
    assert d['r'] == 1
    assert d['t'] == 1
    
def test_evaluate():
    """
    for i in postfix expression
    if i is an operand
    push it on to a stalk
    else
    pop the top two items on the stalk (a, b)
    result = apply i on a and b
    push result back on to stalk
    final_result = topof stalk
    """
    assert evaluate_postfix("23+") == 5
    assert evaluate_postfix("23+5*") == 25
    assert evaluate_postfix("235*+") == 17
    assert evaluate_postfix("235*+a") == False
    assert evaluate_postfix("225*%") == False
