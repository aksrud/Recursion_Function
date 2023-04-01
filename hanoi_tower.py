count = 0

def move(n, start, to):
    print("{}번째 원반을 {}에서 {}로 이동".format(n, start, to))

def hanoi(n, start, by, to):

    # 하노이 함수가 몇번 호출했는지 알려주는 변수
    global count
    count += 1

    # 하노이 함수 탈출 조건
    if n == 1:
        move(n, start, to)
        return
    
    # 하노이 공식
    hanoi(n-1, start, to, by)
    move(n, start, to)
    hanoi(n-1, by, start, to)

try:
    num = int(input("몇개의 판을 이동 시키겠습니까? : "))
    if(isinstance(num, int) == False or num <= 0):
        raise Exception
    hanoi(num, "A", "B", "C")
    print(count)
    
except:
    print("입력할 수 있는 것은 0이상의 정수 입니다.")

