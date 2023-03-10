from random import randint

def eq2text(list):
    """Takes a list of four numbers and returns a string"""
    
    return f'{firstPart(list[0])} {secondPart(list[1])} = {firstPart(list[2])} {secondPart(list[3])}'


def firstPart(digit):
    """Evaluates the first or third digit and returns correct string"""
    
    if digit == 1:
        return "x"
    elif digit == -1:
        return "-x"
    else:
        return f'{digit}x'


def secondPart(digit):
    """Evaluates the second or fourth digit and returns correct string"""

    if digit > 0:
        return f'+ {digit}'
    else:
        return f'- {abs(digit)}'


def ok(list):
    """Checks if input digits are valid for equation"""
    
    return not (0 in list or list[0] == list[2] or list[1] == list[3])


def make_eq():
    """Uses random.randint() to create digits for equation"""
    
    while True:
        returnList = [randint(-9, 9) for i in range (4)]
        if ok(returnList):
            return returnList


def make_n_eqs(number):
    """Returns a list with given number of sets of digits for equations"""
    
    returnList = [make_eq()]
    while len(returnList) < 5:
        newEq = make_eq()
        if newEq not in returnList or (newEq[2:] + newEq[0:2]) not in returnList:
            returnList.append(newEq)
        else:
            continue
    return returnList

    
def make_test(students, n):
    """Takes list of students and creates a test for each of them"""
    
    return {student:make_n_eqs(n) for student in students}


def answer_questions(D):
    """Asks student to input name and answer their own equations"""
    
    while True:
        inputName = input("Enter your name: ").capitalize()
        if inputName in D.keys():
            break
    print("Please solve these equations:")
    startLetter = ord('a')
    for i in range(len(D[inputName])):
        print(f'{chr(startLetter + i)}) {eq2text(D[inputName][i])}')
        while True:
            try:              
                answer = float(input("x = "))
                break
            except:
                print("Please input a number")                
        D[inputName][i].append(answer)


def main():
    """Main program tests if other code works as intended"""
    
    tests = make_test(['Ola', 'Kari', 'Fredrik'], 5)
    answer_questions(tests)
    print(tests)

main()