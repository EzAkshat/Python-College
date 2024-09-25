A = int(input('Enter Value of A : '))
B = int(input('Enter Value of B : '))
C = int(input('Enter Value of C : '))

if A == B and B > C:
    print('B is greater then C but is equal to A')
elif B == C and C > A:
    print('C is greater then A but is equal to C')
elif C == A and A > B:
    print('A is greater then B but is equal to C')
elif A > B and A == C:
    print('A is greater then B but is equal to C')
elif B > A and A == C:
    print('B is greater then A but is equal to C')
elif C > B and B == A:
    print('C is greater then B but is equal to A')
elif A != B and B != C and C != A:
    print('All not equal')
else:
    print('All equal')