#Calculator alpha ver.3 (CGPT helped TUI)

import math, time

Error_L = {
    'VL-ER:InptVL':'에러-값:입력값 오류',
    'VL-ER:OtptVL':'에러-값:출력값 오류'
    }
Cclted = []

Exced = 0
ExcedC = 0
ExcedF, ExcedS, ExcedT = 0, 0, 0

#메인 스크린
def Main_Screen():
    global Exced, Cclted, LnCd
    LnCd = len(Cclted)
    if Exced == 0:
        print("==" * 10)
        print("Calculator alpha ver.3")
        print('''1. 사칙연산 | 2. 간단한 수학적 계산
0. 계산 기록 보기''')
    select = input("번호를 입력하여 원하는 계산 시작: ")
    if select == '1':
        Exced = 0
        return 'FFAO'
    elif select == '2':
        Exced = 0
        return 'SMC_M'
    elif select == '0':
        Exced = 0
        return 'Cclted_Screen'
    if select == '/Cclted+10':
        for i in range(10):
            Cclted.append('1')
        print(f'[System]: "{select}" Command Successfully Applied!')
        Exced = 1
        return 'Main_Screen'
    if select == '/Cclted-10':
        if LnCd >= 10:
            for i in range(10):
                del Cclted[-1]
            print(f'[System]: "{select}" Command Successfully Applied!')
        elif LnCd < 10:
            print(f'[System]: "{select}" Command Failed!')
        Exced = 1
        return 'Main_Screen'
    if select == '/Cclted+100':
        for i in range(100):
            Cclted.append('1')
        print(f'[System]: "{select}" Command Successfully Applied!')
        Exced = 1
        return 'Main_Screen'
    if select == '/Cclted-Clr':
        Cclted.clear()
        print(f'[System]: "{select}" Command Successfully Applied!')
        Exced = 1
        return 'Main_Screen'
    else :
        print('###'*3, Error_L['VL-ER:InptVL'], '###'*3)
        Exced = 1
        return 'Main_Screen'

#계산 기록
def Cclted_Screen():
    global Cclted, Exced
    LnCd = len(Cclted)
    HwMc = 0
    if Exced == 0:
        print('_' * 10)
        print(f'''[계산 기록 보기]
원하시는 계산 기록의 양을 입력해 주세요.
[현재 {LnCd}개 의 기록이 있습니다.]
계산 기록의 양보다 많이 입력하거나, 100 이상을 입력할 경우 모든 기록(최대 100개)을 출력합니다.
0 을 입력할 경우, 메인 메뉴로 돌아갑니다.''')
        if LnCd == 0:
            print('#  기록이 없습니다. :(  #')
            input('아무 키나 입력하여 메인 메뉴로 돌아가기: ')
            Exced = 0
            return 'Main_Screen'
    try: HwMc = int(input('출력할 기록량(최대 100) 입력:'))
    except:
        print('###'*3, Error_L['VL-ER:InptVL'], '###'*3)
        Exced = 1
        return 'Cclted_Screen'
    if HwMc == 0:
        Exced = 0
        return 'Main_Screen'
    elif HwMc <= LnCd:
        for i in range(HwMc):
            print(f'{i+1}. [{Cclted[i]}]')
        input('메인메뉴로 돌아가기: ')
        Exced = 0
        return 'Main_Screen'
    elif HwMc > LnCd or HwMc >= 100:
        print('모든 기록(최대 100)을 출력합니다.')
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1...')
        time.sleep(2)
        print('--------')
        for i, val in enumerate(Cclted[:100]):
            print(f'{i+1}. [{val}]')
        print('--------')
        input('메인메뉴로 돌아가기: ')
        Exced = 0
        return 'Main_Screen'
    else :
        print('###'*3, Error_L['VL-ER:InptVL'], '###'*3)
        Exced = 0
        return 'Main_Screen'

#사칙연산
def FFAO():
    global Cclted, Exced, ExcedF, ExcedS, ExcedT
    PstNum_L = ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    Nu1 = 0
    Nu2 = 0
    Rslt = 0
    if Exced == 0:
        print("--" * 10)
        print('''사칙연산
수 입력시 항상 시작부분이 +, - 또는 정수로 시작하게 입력해 주세요''')
        print('[M]을 입력할 경우, 메인 메뉴로 돌아갑니다.')
#첫번째 정수
    while ExcedF == 0:
        FiNu = input("첫번째 정수 입력: ")
        if FiNu == 'M' or FiNu == 'm':
            Exced, ExcedF, ExcedS, ExcedT = 0, 0, 0, 0
            return 'Main_Screen'
        else:
            try: Nu1 = int(FiNu)
            except:
                print('###'*3, Error_L['VL-ER:InptVL'], '###'*3)
                Exced = 1
                ExcedF = 0
                return 'FFAO'
            ExcedF = 1
#연산자
    while ExcedS == 0:
        Oper = input("연산자(+, -, *, / 중 하나) 입력: ")
        OperLs = list(Oper)
        if Oper == 'M' or Oper == 'm':
            Exced, ExcedF, ExcedS, ExcedT = 0, 0, 0, 0
            return 'Main_Screen'
        else:
            for i in range(len(OperLs)):
                if OperLs[i] == '+':
                    Oper = '+'
                    ExcedS = 1
                    break
                elif OperLs[i] == '-':
                    Oper = '-'
                    ExcedS = 1
                    break
                elif OperLs[i] == '*':
                    Oper = '*'
                    ExcedS = 1
                    break
                elif OperLs[i] == '/':
                    Oper = '/'
                    ExcedS = 1
                    break
                else:
                    print('###'*3, Error_L['VL-ER:InptVL'], '###'*3)
                    ExcedS = 0
#두번째 정수
    while ExcedT == 0:
        SeNu = input("두번째 정수 입력: ")
        if SeNu == 'M' or SeNu == 'm':
            Exced, ExcedF, ExcedS, ExcedT = 0, 0, 0, 0
            return 'Main_Screen'
        else:
            try: Nu2 = int(SeNu)
            except:
                print('###'*3, Error_L['VL-ER:InptVL'], '###'*3)
                Exced, ExcedF, ExcedS, ExcedT = 0, 1, 1, 0
                return 'FFAO'
            ExcedT = 1
    if Oper == '+':
        Rslt = Nu1 + Nu2
    elif Oper == '-':
        Rslt = Nu1 - Nu2
    elif Oper == '*':
        Rslt = float(Nu1) * float(Nu2)
    elif Oper == '/':
        Rslt = float(Nu1) / float(Nu2)
    
    print('결과값은 %0.6f 입니다.'%Rslt)
    Cclted.append(Rslt)
    AskRty = input("0.돌아가기 | 1.계속하기 :")
    if AskRty == '1':
        Exced, ExcedF, ExcedS, ExcedT = 0, 0, 0, 0
        return 'FFAO'
    elif AskRty == '0':
        Exced, ExcedF, ExcedS, ExcedT = 0, 0, 0, 0
        return 'Main_Screen'
    else:
        print('###' * 3, Error_L['VL-ER:InptVL'], '###' * 3)
        Exced, ExcedF, ExcedS, ExcedT = 0, 0, 0, 0
        return 'Main_Screen'

#SMC_1 [제곱]
def SMC_1():
    global Cclted
    print("--" * 10)
    print('''간단한 수학적 계산-[제곱]
제곱할 수를 입력해 주세요.''')
    Rslt = 0
    try: SqNu = int(input('제곱할 수 입력: '))
    except:
        print('###' * 3, Error_L['VL-ER:InptVL'], '###' * 3)
        return 'SMC_1'
    print(f'''[제곱할 수:{SqNu}]
제곱할 횟수를 입력해 주세요''')
    try: SqCnNu = int(input('제곱할 횟수 입력: '))
    except:
        print('###' * 3, Error_L['VL-ER:InptVL'], '###' * 3)
        return 'SMC_1'
    Rslt = SqNu ** SqCnNu
    print(f'결과값은 {Rslt} 입니다.')
    Cclted.append(Rslt)
    print('[M] 을 입력하여 메인 화면으로 돌아갈 수 있습니다.')
    AskRty = input("0.돌아가기 | 1.계속하기 :")
    if AskRty == '1':
        return 'SMC_1'
    elif AskRty == '0':
        return 'SMC_M'
    elif AskRty == 'M' or AskRty == 'm':
        return 'Main_Screen'
    else:
        print('###' * 3, Error_L['VL-ER:InptVL'], '###' * 3)
        return 'Main_Screen'
    
#SMC_2 [제곱근]
def SMC_2():
    global Cclted
    print("--" * 10)
    print('''간단한 수학적 계산-[제곱근]
제곱근을 구할 수를 입력해 주세요.''')
    Rslt = 0
    try: SqNu = int(input('제곱근을 구할 수 입력: '))
    except:
        print('###' * 3, Error_L['VL-ER:InptVL'], '###' * 3)
        return 'SMC_2'
    try: Rslt = math.sqrt(SqNu)
    except:
        print('###' * 3, Error_L['VL-ER:OtptVL'], '###' * 3)
        return 'SMC_2'

    print('결과값은 %0.6f 입니다.'%Rslt)
    Cclted.append(Rslt)
    print('[M] 을 입력하여 메인 화면으로 돌아갈 수 있습니다.')
    AskRty = input("0.돌아가기 | 1.계속하기 :")
    if AskRty == '1':
        return 'SMC_2'
    elif AskRty == '0':
        return 'SMC_M'
    elif AskRty == 'M' or AskRty == 'm':
        return 'Main_Screen'
    else:
        print('###' * 3, Error_L['VL-ER:InptVL'], '###' * 3)
        return 'Main_Screen'
    

#간단한 수학적 계산
def SMC_M():
    print("--" * 10)
    print('''간단한 수학적 계산
아래의 번호를 입력하여 제곱, 제곱근, 파이와 같은
간단한 계산 요소들을 이용하실 수 있습니다.
1. 계산:[제곱]
2. 계산:[제곱근]
3. 계산:[파이]''')
    print("0. 돌아가기")

    AskRty = input("번호 입력: ")
    if AskRty == '1':
        return 'SMC_1'
    elif AskRty == '2':
        return 'SMC_2'
    elif AskRty == '3':
        return 'SMC_3'
    elif AskRty == '0':
        return 'Main_Screen'
    else:
        print('###' * 3, Error_L['VL-ER:InptVL'], '###' * 3)
        return 'Main_Screen'

current_screen = 'Main_Screen'
screens = {
    'Main_Screen': Main_Screen,
    'Cclted_Screen' : Cclted_Screen,
    'FFAO' : FFAO,
    'SMC_M': SMC_M,
    'SMC_1': SMC_1,
    'SMC_2': SMC_2,

}

#실행 루프

while True:
    current_screen = screens[current_screen]()
