from functools import cmp_to_key


def sortAlgorithm(a, b):
    aSplitted = a.split(' ', 1)
    bSplitted = b.split(' ', 1)

    aWithoutIdentifer = aSplitted[1]
    bWithoutIdentifer = bSplitted[1]

    isADigitLog = aWithoutIdentifer[0].isdigit()
    isBDigitLog = bWithoutIdentifer[0].isdigit()

    if isADigitLog and isBDigitLog:
        return 0
    elif isADigitLog and not isBDigitLog:
        return 1
    elif not isADigitLog and isBDigitLog:
        return -1
    else:
        if aWithoutIdentifer == bWithoutIdentifer:
            if aSplitted[0] < bSplitted[0]:
                return -1
            else:
                return 1
        elif aWithoutIdentifer < bWithoutIdentifer:
            return -1
        else:
            return 1

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a3 act zoo"]
# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(sorted(logs, key=cmp_to_key(sortAlgorithm)))
