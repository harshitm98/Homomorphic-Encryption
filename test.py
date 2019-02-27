import hmencrypt as hm

hm.generateSecretKeys()
print("Secret keys (J, K):", hm.getSecretKeys())


N = int(input("Enter N: "))


C = hm.encrypt(N)
print("N encryption (C):", C)
if C == N:
    print("Encryption was not performed")
    operator = -1
else:
    operator = 4

operations = "C"
C_ini = C
while operator > 0:
    print()
    print("Operations")
    print("===========")
    print("[ 0 ] Exit")
    print("[ 1 ] Addition")
    print("[ 2 ] Subtraction")
    print("[ 3 ] Multiplication")
    operator = int(input("Select the operation: "))
    if operator == 0:
        break
    number = int(input("Number: "))
    if operator == 1:
        C = C + number
        operations = operations + " + " + str(number)
        continue
    elif operator == 2:
        C = C - number
        operations = operations + " - " + str(number)
        continue
    elif operator == 3:
        C = C * number
        operations = "( " + operations + " ) * " + str(number)
        continue

print()
print("Resume")
print("=======")
print("N initial:", N)
print("C initial:", C_ini)
print()
print("Operations :", operations, " = ", C)

NN = hm.decrypt(C)
print()
print("C decrypt:", NN)
