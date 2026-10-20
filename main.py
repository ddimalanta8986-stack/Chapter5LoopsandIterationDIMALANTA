total = 0
count = 0
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        num = float(user_input)
        total += num
        count += 1
    except:
        print("Invalid input")
if count > 0:
    average = total / count
    print(total, count, average)
else:
    print("No numbers entered")