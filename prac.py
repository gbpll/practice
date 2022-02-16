# a, b, c = map(int, input().split())
# print(a, b, c)

# #f
# a = 7
# print(f"정답은 {a}입니다.")

# a = 15
# if a<10:
#     print("a<10")

# elif a>=20:
#     print("a>=20")
# else :
#     print("a = 15")

# score = 85
# if score >= 90:
#     print("학점: A")
# elif score >= 80:
#     print("학점: B")
# elif score >=70:
#     print("학점: C")
# else:
#     print("학점: F")

# score = 80
# result = "success" if score >=75 else "fail"
# print(result)

#while
# from re import I


# i = 1
# result = 0
# # while i <= 9:
#     result += i
#     i += 1
# print(result)

# while i <= 9:
#     if i % 2 ==1:
#         result += i
#     i +=1
# print(result)

#for
# array = [9, 8, 7, 6, 5]
# for x in array:
#     # print(x)
# print(sum[])

# result = 0

# # for i in range(1, 31):
# #     result += i

# # print(result)

# #1~9 홀수의 합
# for i in range(1,10):
#     if i % 2 ==0:
#         continue #건너 뜀
#     result +=i
# print(result)

# scores=[90, 85, 77, 65, 97]
# for i in range(5):
#     if scores[i]>=80:
#         print(i+1,"번 학생은 합격입니다.")

#sorted()

# result=sorted([9, 1, 8, 4, 5])
# print(result)

# reverse_result= sorted([9, 1, 8, 5, 4], reverse=True)
# print(reverse_result)

#counter

# from collections import Counter
# counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])

# print(counter['blue']) #'blue'의 횟수
# print(counter['green'])
# print(dict(counter))


# print('''\    /\\
#  )  ( ')
# (  /  )
#  \(__)|''')

# #10172
# print('''|\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\__|''')



# A, B = map(int, input().split())
# print(A+B, A-B, A*B, A//B, A%B, sep="\n")
# ID=input("")
# print(ID+"??!")

# year = int(input())
# print(year-543)

# A, B, C = map(int, input().split())
# print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep=("\n"))

# a = int(input())
# b = input()
# c = a*int(b[2])
# d = a*int(b[1])
# e = a*int(b[0])
# f = a*int(b)
# print(c, d, e, f, sep=("\n"))

# a, b = map(int, input().split())
# if a>b:
#     print('>')
# if a<b:
#     print('<')
# if a==b:
#     print('==')

# a = int(input())
# if 90<=a<=100:
#     print("A")
# if 80<=a<=89:
#     print("B")
# if 70<=a<=79:
#     print("C")
# if 60<=a<=69:
#     print("D")
# if a<60:
#     print("F")

# a = int(input())
# if a%4 == 0 and a%100 !=0 or a%400 == 0:
#     print(int(1))
# else:
#     print(int(0))

x = int(input())
y = int(input())
if x<0 and y>0:
    print(int(2))
elif x>0 and y>0:
    print(int(1))
elif x<0 and y<0:
    print(int(3))
else:
    print(int(4))