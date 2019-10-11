'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    result = [0,0]
    split = list(word)
    if(len(split) > 2):
        recursion_th(word,result);
    elif(len(word) == 2):
        if(word == 'th'):
           result[1] = 1
    return result[1]

def recursion_th(word,result):
    if(result[0]+1 != len(word)):
        check = str(word[result[0]] + word[result[0]+1]);
        if(check == 'th'):
            result[1] += 1
        result[0] += 1
        recursion_th(word,result)
    else:
        return result
