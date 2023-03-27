gStack = []

def main() :
    global gOrder; global gStack
    order = ""

    try :
        while True :
            print("""\033[32m명령을 입력하시오.\033[33m
    (1)\033[31mS\033[33mhowall (2)\033[31mI\033[33mnit (3)\033[31mPu\033[33msh (4)\033[31mPo\033[33mp (5)\033[31mH\033[33melp (0)\033[31mQ\033[33muit
입력 : """, end = '')
            order = input()

            if order == "Showall" or order == "showall" or order == "1" or order == "s" or order == "S" or order == "SHOWALL":
                if len(gStack) == 0 :
                    print("스택이 비어있네요..")
                else :
                    # gStack.reverse()
                    for i in range(len(gStack)-1, -1, -1) :
                        print((i)+1, "번째 스택 : \t", gStack[i])
                    # gStack.reverse()
            elif order == "Init" or order == "init" or order == "2" or order == "I" or order == "i" or order == "INIT":
                order = input("\033[31m지금까지 작성한 게 전부 날라가요, 괜찮나요?(y/n)")
                if order == 'y' or "Y" or "yes" or "YES" : 
                    gStack = []
            elif order == "Push" or order == "push" or order == "3" or order == "Pu" or order == "PU" or order == "pu" or order == "PUSH":
                order = input("추가하고자 하는 값을 입력하시오.")
                gStack.append(order)
                print(order + "가 stack에 추가됨")
            elif order == "Pop" or order == "pop" or order == "4" or order == "Po" or order == "PO" or order == "POP" or order == "po":
                del gStack[-1]
            elif order == "Help" or order == "help" or order == "5" or order == "HELP" or order == "H" or order == "h" :
                print("""사용법 : 
                (1)Showall :
                   입력 방법 : Showall, showall, SHOWALL, s, S, 1
                   스택의 상태를 수정하지 않으면서 스택의 모든 값을 출력하는 기능
                (2)Init :
                   입력 방법 : Init, init, INIT, i, I, 2
                   스택 생성 및 초기화 함수
                (3)Push :
                   입력 방법 : Push, push, PUSH, Pu, pu, PU, 3
                   스택에 값을 삽입
                (4)Pop :
                   입력 방법 : Pop, pop, POP, Po, po, PO, 4
                   스택에 가장 마지막으로 집어넣은 값을 삭제
                (5)Help : 
                   입력 방법 : Help, help, HELP, h, H, 5
                   도움말을 요청합니다.(잘 사용하고 계시네요..)
                (6)Quit :
                   입력 방법 : Quit, quit, QUIT, q, Q, 0
                   프로그램을 종료합니다.
                """)
            elif order == "Quit" or order == "quit" or order == "QUIT" or order == "q" or order == "Q" or order == "0" :
                print("Byebye..")
                break
            elif order == "Sample" or order == "sample":
                order = int(input("개발자 전용 코드 실행됨, 집어넣을 수의 개수는? "))
                for i in range(order) :
                    gStack.append(i)
            else :
                print("\033[31m인식할 수 없는 명령이네요..")

    except Exception as err :
        print(err)

if __name__ == "__main__" :
    main() 
