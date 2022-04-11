print("Hello World")

counter = 0
maximum =int(input())
while counter < maximum:
    print(counter)
    counter+=1

    def get_median(num1, num2, num3):
        if ((num1 < num2) or (num1 < num3)) and ((num1>num2) or (num1 >num3)):
            return num1
        elif ((num2 < num1) or (num2 < num3)) and ((num2>num1) or (num2 >num3)):
         return num2
        elif ((num3 < num1) or (num3 < num2)) and ((num3>num1) or (num3 >num2)):
            return num3

print("\n"+"Median:"+str(get_median(5,8,7)))

