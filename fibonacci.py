def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    
    return fibonacci(num-2) + fibonacci(num-1)

try:
    num = int(input("몇 번째 피보나치 수를 구하시나요? : "))
    if(isinstance(num, int) == False or num <= 0):
        raise Exception
    print("{}번째 피보나치의 수는 {}입니다.".format(num, fibonacci(num)))
    
except:
    print("입력할 수 있는 것은 0이상의 정수 입니다.")