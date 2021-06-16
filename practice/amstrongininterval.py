start = int(input("Enter the start range : "))
stop = int(input("Enter the stop range : "))

for n in range(start, stop+1): 
    temp = n
    sum = 0
    while temp > 0:
        rem = temp % 10
        sum += (rem**3)
        temp /= 10
    if n == sum:
        print(n, "is an Armstrong number")

print("Program Ends here")