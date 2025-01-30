# Question 1
# def sumN(n):
#     if n == 1:
#         return 1
#     return n + sumN(n - 1)


# n = int(input("Enter a number here: "))
# print(sumN(n))


# Question 2
# sum of first N odd numbers is n^2
# def sumNOdd(n):
#     if n == 1:
#         return 1
#     return 2 * n - 1 + sumNOdd(n - 1)


# n = int(input("Enter a number here: "))
# print(sumNOdd(n))


# Question 3
# sum of first N odd numbers is n(n+1)
# def sumNEven(n):
#     if n == 1:
#         return 2
#     return 2 * n + sumNEven(n - 1)


# n = int(input("Enter a number here: "))
# print(sumNEven(n))


# Question 4
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)


# n = int(input("Enter a number here: "))
# print(fact(n))


# Question 5
def sumNSquares(n):
    if n == 1:
        return 1
    return (n * n) + sumNSquares(n - 1)


n = int(input("Enter a number here: "))
print(sumNSquares(n))
