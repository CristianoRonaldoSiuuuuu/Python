score = 0

while True:
    num = input ("Enter Number :")
    if num == 'exit':
        break
    elif not num.isdigit():
        print("Invalid Integer")
    else:
        num = int(num)
        if num % 2 == 0:
            print("The Number Is Even")
            score += 1
        else:
            print("The Number Is Odd")
            score -= 1

print("Your Score Is", score)





