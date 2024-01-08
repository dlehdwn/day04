# a = "americano" # str
# # sowkdgkatn [ int, str, float, bool, list, print, input]
# # len() : 길이를 알려줌
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.strip()) #빈공간 없에기
# print(a.find()) # 몇번째에 'c'가 있니? #없으면 -1
# print(a.replace(a,b)) #왼쪽에서 오른쪽으로 바꾸기
# print(a.count(''))
#
# a = "mega"
# b = "study"
# c = a + b # 문자열 연결
# d = a*3 # 문자열 반복
# e = a[0] # []문자열 인덱싱   결과:m
# f = b[0:3] # 슬라이싱    결과:stu
# g = 'g' in a # "mega"에서 'g'가 있니?  결과:T/F
#
# title = "megastudy python programming"
# print(title.split()) # 빈공간 기준으로 str --> list로 만들어 줌

# print(title.split(','))
# 유저 이메일 -> ['유저아이디','도메인'] -> ['유저아이디','플랫폼','com']
em = str(input("이메일 입력 : "))
a = em.split('@')
b = a[1].split('.')
a[1] = b[0]
a.append(b[1])
print(a)

# join
word = ' '.join(['ice', 'cream']) # 'ice cream'

id = input("아이디 입력 : ")
domain = input("도메인 입력 : ")
print('@'.join([id,domain]))


