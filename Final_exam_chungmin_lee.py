#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201881 이름 : 이충민

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_strung, target):
    str = my_strung                         #매개변수 my_strung의 값을 str에 저장
    tgt = target                            #매개변수 target의 값을 tgt에 저장
    if str.find(tgt)==-1:                   #find() 함수는 찾는 문자열이 없을 때 -1을 반환하므로 조건문을 이용해, 
        answer = 0                          #찾는 문자열이 없는경우 answer = 0
    else:                                   #그 외 문자열을 찾을 경우 문자열의 위치를 반환하므로
        answer = 1                          #-1외의 값이 나올 시, answer = 1
    return answer                           #결과값 리턴
#my_strung = "my name is lee chung min"
#target = "name"
#result = solution(my_strung, target)
#print(result)


# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = {                                   #모스부호 딕셔너리 생성
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    letter_list = letter.split()                #letter의 모스부호는 공백으로 나누어져있기 때문에 split()함수를 이용해
    a = len(letter_list)                        #한 글자씩 리스트로 분리 후 for문을 위해 전체 길이 측정
    answer = ''                                 #결과값 변수 초기화
    for i in range(a):                          #반복문을 사용하여 분리한 모스부호를 딕셔너리를 통해 해당되는 문자로
        answer += morse[letter_list[i]]         #변환 후 결과값에 계속 추가
    return answer                               #각각의 모스부호를 해석해 나온 최종 결과값 리턴
#letter = '-.-. .- .-. .--. . -.. .. . --'      #좌우명 - "carpediem" : "현재를 즐겨라" 
#result = solution(letter)
#print(result)


# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.


def solution(age):
    progeammer = {'0':'a','1':'b','2':'c','3':'d','4':'e',      #각각의 숫자에 해당하는 알파벳을 딕셔너리를 이용해 표현
                  '5':'f','6':'g','7':'h','8':'i','9':'j'}
    str_age = str(age)                                          #매개변수로 받은 나이의 값을 문자열로 변환
    a = len(str_age)                                            #for문을 위해 문자열의 길이 측정
    answer = ''                                                 #결과값 변수 초기화
    for i in range(a):                                          #반복문을 사용해서 딕셔너리를 통해 해당되는 숫자를
        answer += progeammer[str_age[i]]                        #문자로 변환 후 결과값에 계속 추가
    return answer                                               #결과값 리턴
#age = 369
#result = solution(age)
#print(result)


# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    inner_1 = 0                             #변수(원 안에 있는 점의 갯수)값 초기화
    for i in range(r1, r2-1):               #반복문을 사용해 원 안에 있는 점 중 1/4에 해당하는 부분에서
        inner_1 += (i*2+3)                  #2*i+3의 규칙을 갖고 있는 점들을 i의 두 반지름 사이 범위에서 갯수 계산
    inner = inner_1 + (2*r1-1)              #inner_1에서 측정한 점 외에 내부 원에 근접해 있는 점의 갯수를 2*r1-1규칙을 이용해 계산
    answer = 8 + inner*4                    #위에서 구한 내부갯수에 4를 곱해주고 원 2개 위의 점 8개를 더해 최종 갯수(결과값)계산
    return answer                           #결과값 리턴
#r1 = 2
#r2 = 5
#result = solution(r1, r2)
#print(result)

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    a = len(numbers)                                                    #반복문 위해 numbers 길이 측정
    num = [''] * a                                                      #변수초기화 : 정수 배열을 문자열로 바꾸기 위해 배열의 길이만큼 문자열 크기설정
    answer = ''                                                         #결과값 변수 초기화                                         
    for i in range(a):                                                  #반복문을 통해 정수 리스트를 문자열로 변환
        num[i] = str(numbers[i])
    for i in range(a):                                                  #sorting을 위해 반복문 시작                           
        high_num = 0                                                    #최댓값 인덱스넘버 저장을 위한 변수 0으로 초기화
        for j in range(a):                                              #붙였을 때 최댓값이 나오려면 처음 숫자가 제일 커야하기 때문에,
            if int(num[j][0]) > int(num[high_num][0]):                  #이차원배열 뒷부분은 0으로 고정하고 앞부분만 수정하여 최댓값 계산
                high_num = j                                            #앞의 숫자 비교 후 가장 최댓값의 인덱스넘버를 high_num에 저장
            if int(num[j][0]) == int(num[high_num][0]):                 #처음 숫자가 같을 시 그 다음숫자를 비교해야하므로
                temp = 0                                                #반복문 중 high_num을 수정했는지 여부를 측정하는 변수 0으로 초기화
                f = len(num[j])                                         #비교값 문자열의 길이와
                h = len(num[high_num])                                  #기준값 문자열의 길이 측정
                if f == h:                                              #첫번째로, 두 문자열의 길이가 같을 경우,
                    if numbers[j] > numbers[high_num]:                   #처음에 받았던 numbers값을 이용해 최댓값을 구한 뒤,
                        high_num = j                                     #그 값의 인덱스넘버를 high_num에 저장
                if f > h:                                               #두번째로, 비교값 문자열의 길이가 더 길 경우,
                    for k in range(h):                                   #반복문 범위를 짧은 문자열의 길이로 지정 후,
                        if int(num[j][k]) > int(num[high_num][k]):       #자릿수를 하나씩 옮겨가면서 최댓값 계산
                            temp = 1                                     #이 반복문에서 모든 값이 같을 경우를 대비하여,
                            high_num = j                                 #최댓값을 찾으면 temp값을 1로 바꾸고 해당하는 인덱스넘버를 high_num에 저장
                    if temp == 0:                                        #만약, 위의 반복문에서 최댓값의 변경이 없어서 temp값이 0일 때,
                        if num[j][f-1] > num[high_num][0]:               #긴 문자열의 제일 끝 값과 짧은 문자열의 처음 값을 비교해 전자가 크다면,
                            high_num = j                                 #그 값이 최댓값이 되므로, 인덱스넘버를 high_num에 저장
                if f < h:                                               #세번째로, 비교값 문자열의 길이가 더 짧을 경우,
                    for k in range(f):                                   #위에서와 같이 반복문 범위를 짧은 문자열의 길이로 지정 후,
                        if int(num[j][k]) > int(num[high_num][k]):       #자릿수를 하나씩 옮겨가며 최댓값 계산
                            temp = 1                                     #여기서도 모든 값이 같을 경우에 대비하여,
                            high_num = j                                 #최댓값을 찾으면 temp값을 1로 바꾸고 해당하는 인덱스넘버를 high_num에 저장
                    if temp == 0:                                        #만약, 변경사항이 없어서 temp값이 0일 때,
                        if num[j][0] > num[high_num][h-1]:               #마찬가지로 긴 문자열의 끝 값과 짧은 문자열의 처음 값을 비교. 이때는 위에서와는 반대로, 
                            high_num = j                                 #짧은 문자열의 처음값이 클 때, 그 값이 최대값이 되므로 이때 인덱스넘버를 high_num에 저장
        answer += num[high_num]                                         #구한 최댓값의 인덱스넘버를 대입해 결과값에 추가하고
        num[high_num] = str('0')                                        #이미 구한 값은 0으로 초기화 
                                                                        #이 내부 반복문의 과정을 계속 반복하면 answer에는 최종 결과값이 계산됨.
    return answer                                                       #결과값 리턴
#numbers = [8, 30, 17, 2, 23]
#result = solution(numbers)
#print(result)