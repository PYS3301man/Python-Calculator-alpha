#Calculator alpha ver.0 (CGPT helped TUI)

import math


#메인 스크린
def Main_Screen():
    print("==" * 10)
    print("Calculator alpha ver.0")
    print('''1. 사칙연산 |
''')
    select = input("번호를 입력하여 원하는 계산 시작: ")
    if select == '1':
        return 'FFAO'
    else :
        print("#ERROR!#")
        return 'Main_Screen'

#사칙연산
def FFAO():
    print("--" * 10)
    print("사칙연산(양수)")
    print('''조건:
"숫자" "+, -, *, / 중 하나" "숫자" 형식으로 입력
숫자는 양수만 가능''')
    print("0. 돌아가기")
    Result = 0
    FFAO_Operators = ['+', '-', '*', '/']
    FiVa, SeVa = [], []
    ReFiVa, ReSeVa = 0, 0
    Opr = ''
    modification_ip = input("수식 입력: ")
    modification = list(modification_ip)
    #modification 공백제거 (DelSpa)
    for DelSpa in modification:
        if DelSpa == ' ':
            modification.remove(DelSpa)
    #modification 문자열 - 정수 변환 (ConStr_Int)
    for ConStrDgt in range(len(modification)):
        if modification[ConStrDgt].isdigit():
            modification[ConStrDgt] = int(modification[ConStrDgt])
    #modification 속 연산자를 찾고 이전 및 이후 정수 리스트화 (FiOpr_ConBeAfInt_Li)
    for idx, val in enumerate(modification):
        if val in FFAO_Operators:
            if idx > 0 and idx < len(modification) - 1:
                Opr = modification[idx]
                for CecFVIdx in range(0, idx):
                    FiVa.append(modification[CecFVIdx])
                for CecSVIdx in range(idx+1,len(modification)):
                    SeVa.append(modification[CecSVIdx])
#                print(FiVa, Opr, SeVa) #Opr와 Opr 이전 및 이후 리스트화 된 정수 FiVa 및 SeVa
    #FiVa와 SeVa 자연수화 (ConFiVaSeVa_Ntn)
    for FConDgtNtn in FiVa:
        ReFiVa = ReFiVa * 10 + FConDgtNtn
    for SonDgtNtn in SeVa:
        ReSeVa = ReSeVa * 10 + SonDgtNtn
#    print(ReFiVa, ReSeVa) #자연수화된 FiVa와 SeVa
    #사칙연산
    if Opr == '+':
        Result = ReFiVa + ReSeVa
        print(f"계산값은 {Result} 입니다.")
    elif Opr == '-':
        Result = ReFiVa - ReSeVa
        print(f"계산값은 {Result} 입니다.")
    elif Opr == '*':
        Result = ReFiVa * ReSeVa
        print(f"계산값은 {Result} 입니다.")
    elif Opr == '/':
        Result = round(ReFiVa / ReSeVa, 4)
        print(f"계산값은 {Result} 입니다.")

    AskRty = input("1. 계속하기 | 0. 돌아가기: ")

    if modification_ip == '0':
        return 'Main_Screen'
    if AskRty == '1':
        return 'FFAO'
    elif AskRty == '0':
        return 'Main_Screen'

current_screen = 'Main_Screen'
screens = {
    'Main_Screen': Main_Screen,
    'FFAO' : FFAO

}

#실행 루프

while True:
    #미완성 부분 재실행 예외처리
    try:
        current_screen = screens[current_screen]()

    except:
        current_screen = Main_Screen()
        continue
