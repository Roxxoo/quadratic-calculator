import cmath
# def decision(choice):
#     return {
#            'a': a+b,
#            'b': a-b,
#            'c': (a*b),
#            'd': (a/b),
#            }.get(choice,"Invalid")

#this is used to calculate the answer for a quadratic equation

def quadratic_equation(a,b,c):
      soln1 = (-b + (cmath.sqrt(b**2 - 4*(a*c)))) / 2 * a
      soln2 = (-b - (cmath.sqrt(b**2 - 4*(a*c)))) / 2 * a
      answers = [soln1, soln2]
      return answers

#choice is used to pick between a (quadratic equation) or b (mathematical operations)

choice = None
while (choice != 'a') and (choice != 'b'):
    choice = str.lower(input("A (quadratic equation) or B: "))

#start of the quadratic equation
if choice == 'a':
    a = int(input("Enter value of A: " ))
    b = int(input("Enter value of B: " ))
    c = int(input("Enter value of C: " ))
    #answers = [] is a list containing the 2 answers from the quadratic equation
    answers = []

    #this is where the operation is being done while the answers list is going to contain those answerss
    answers = quadratic_equation(a,b,c)

    print("Answer of b + root: ", answers[0].real)
    print("Answer of b - root: ", answers[1])

    input("Press Enter to continue...")
#end of the quadratic equation
else:
    choice = None

    while choice != 'a' and choice != 'b' and choice != 'c' and choice != 'd':
        choice = str.lower(input("A. Add\nB. Subtract\nC. Multiply\nD. Divide\nChoice:"))
#A
    print("You have chosen option: ", choice)
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))

    # print(decision(choice))

    if choice == 'a':
        print("Sum = " , a + b)

    elif choice == 'b':
        print("Difference = ", a - b)

    elif choice == 'c':
        print("Product = ", a * b)

    else:
        print("Quotient = ", a/b)

    input("Press Enter to continue...")