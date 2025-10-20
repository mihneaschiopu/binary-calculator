def toBinary(n):
    if n == 0:                
        return "0"
    binary = ""                # sets the number as 0 before placing a number value
    while n > 0:
        binary = str(n % 2) + binary    # constantly divides number by 2 to get binary value
        n //= 2
    return binary        # outputs the remainders due to the MOD

while True:
    num = int(input("Enter a number between 1 and 255: "))    # asks for an input
    if 1 <= num <= 255:
        break
    print("Impossible try again.")         # if number isnt right number set it sets as impossible

print("The binary value is :", toBinary(num))   # outputs final results

