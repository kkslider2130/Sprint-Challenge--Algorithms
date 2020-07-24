'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
counts = 0


def count_th(word):
    global counts

    if word[:2] == 'th':
        counts += 1
    elif len(word) == 0:
        res = counts
        counts = 0
        return res
    return count_th(word[1:])
