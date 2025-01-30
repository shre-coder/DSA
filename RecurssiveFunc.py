# question 1
# def printN(n):
#     if n > 0:
#         printN(n - 1)
#         print(n, end=" ")


# n = int(input("Enter a number here: "))
# printN(n)


# question 2
# def printN(n):
#     if n > 0:
#         print(n, end=" ")
#         printN(n - 1)


# n = int(input("Enter a number here: "))
# printN(n)


# question 3
# def printNOdd(n):
#     if n > 0:
#         printNOdd(n - 1)
#         print(2 * n - 1, end=" ")


# n = int(input("Enter a number here: "))
# printNOdd(n)


# question 4
# def printNEven(n):
#     if n > 0:
#         printNEven(n - 1)
#         print(2 * n, end=" ")


# n = int(input("Enter a number here: "))
# printNEven(n)


# Question 5
# def printNOddRev(n):
#     if n > 0:
#         print(2 * n - 1, end=" ")
#         printNOddRev(n - 1)


# n = int(input("Enter a number here: "))
# printNOddRev(n)


# Question 5
def printNEvenRev(n):
    if n > 0:
        print(2 * n, end=" ")
        printNEvenRev(n - 1)


n = int(input("Enter a number here: "))
printNEvenRev(n)
