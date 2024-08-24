#bài 1
# a,b=map(int,input().split())
# print(a+b)

#bài 2
# a=int(input())
# print(a**2)

#bài 3
# a=int(input())
# print(a**3)

#bài 4
# a,b=map(int,input().split())
# print(int(a+b))
# print(int(a-b))
# print(int(a*b))

#bài 5
# a,b=map(int,input().split())
# print(a//b)
# print(a%b)

#bài 6
# a,b,c=map(int,input().split())
# print(a*b+c)

#bài 7
# a,b=map(int,input().split())
# print(a*6-b)

#bài 8
# a=float(input())
# print(round(a*7,1))

#bài 9
# a,b,c=map(float,input().split())
# number = a**2-b**2+c**3
# print(f"{number:.2f}")

#bài 10
# a,b,x,y=map(float,input().split())
# number= (a-b+x)*(b-a+y)
# print(f"{number:.3f}")

#bài 11
# a=int(input())
# print(a*4)
# print(a*a)

#bài 12
# a,b=map(float,input().split())
# num1=2*(a+b)
# num2=a*b
# print(f"{num1:.4f}")
# print(f"{num2:.4f}")

#bài 13
# a=float(input())
# num1=a*2*3.14159265358979
# num2=a*a*3.14159265358979
# print(f"{num1:.6f}")
# print(f"{num2:.6f}")


#bài 14
# a=int(input())
# print(7-a)

#bài 15
# a=int(input())
# print(a-a*2)

#bài 16
# a=int(input())
# print(a-1,a+1)

#bài 18
# a=float(input())
# num1=a**0.5
# print(f"{num1:.2f}")

#bài 19
# a,b=map(int,input().split())
# print(a**2+a*b+b**2)

#bài 20
# import math

# a,b = map(float,input().split())

# num = math.sqrt(a**2 + b**2)

# print(f"{num:.1f}")


#bài 21
# a=float(input())
# num=a*(2**0.5)
# print(f"{num:.3f}")


#bài 23
# a=int(input())
# print(2024-a)

#bài 24
# a,b=map(int,input().split())
# print(b-a+1)

#bài 25
# a=int(input())
# if a%2==0:
#     print(a+2)
# else:
#     print(a+1)

#bài 26
# a=int(input())
# if a%2==0:
#     print(a)
# else:
#     print(a-1)

#bài 27
# from math import *
# a=int(input())
# print(a//2+1 if a%2==0 else ceil(a/2))

#bài 28
# a,b,c,d=map(int,input().split())
# num1=((a-c)**2+(b-d)**2)**0.5
# print(f"{num1:.3f}")

# bài 29
# import math
# a, b, c = map(float, input().split())
# CV = a + b + c
# print(f"{CV:.2f}")
# p = (a + b + c) / 2
# DT = math.sqrt(p * (p - a) * (p - b) * (p - c))
# print(f"{DT:.2f}")

#bài 30
# n,k=map(int,input().split())
# print(n//k)

#bài 31
# a,b=map(int,input().split())
# print(b//2-(a-1)//2)

#bài 32
# n=int(input())
# print(n%10)

#bài 33
# h=float(input())
# n=(2*9.8*h)**0.5
# print(f"{n:.1f}")

#bài 34
# w,h=map(int,input().split())
# n=w/(h**2)
# print(f"{n:.1f}")

#bài 35
# n=int(input())
# print((n%100)//10)

#bài 36
# n=int(input())
# print((n-1)**2)

# bài 37
# n = int(input())
# max_square = 0
# i = 1
# while i * i <= n:
#     max_square = i * i
#     i += 1
# print(max_square)

#bài 38

# n = int(input())
# start = 1
# print(0)
# while start * start <= n:
#     print(start * start)
#     start += 1

#bài 39
# def convert_seconds(seconds):
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     seconds = seconds % 60
#     return f"{hours}:{minutes:02}:{seconds:02}"

# # Đọc số giây từ đầu vào và in kết quả
# n = int(input())
# print(convert_seconds(n))


# #bài 40
# a,b=map(int,input().split())
# print(abs(b-a))

#bài 41
# a, b, c = map(int, input().split())
# print(a * c + b)

#bài 42
# a, b, d = map(float, input().split())
# print("{:.3f}".format((d-b)/a))

#bài 43
# import math
# n = int(input())
# print(math.floor(n/2), math.ceil(n/2))

#bài 44
# x, y = map(int, input().split())
# print(12*x + y)

#bài 45
# import math

# n = int(input())
# if math.sqrt(n) != int(math.sqrt(n)):
#     print(math.ceil(math.sqrt(n)))
# else:
#     print(math.ceil(math.sqrt(n)) + 1)

#bài 46
# import math
# n = int(input())
# if math.log2(n) == int(math.log2(n)):
#     print("YES")
# else:
#     print("NO")

#bài 47
# a, b = map(int, input().split())
# c, d = map(int, input().split())
# print(a, d)
# print(c, b)

#bài 48
# a = int(input())
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i)

#bài 49
# n = int(input())
# print((n+1)*n/2)

#bài 50
# n = int(input())
# result = n * (n + 1) * ((2 * n) + 1)
# result = result // 6
# print(result)

#bài 51
# n = int(input())
# print(((n*(n+1))//2)*((n*(n+1))//2))

#bài 52
# k, n = map(int, input().split())
# socantim = k
# while socantim < n:
#     socantim += k
# print(socantim)

#bài 53
# k, n = map(int, input().split())
# socantim = k
# while socantim < n:
#     socantim += k
# print(socantim - k)

#bài 54
# a, d, n = map(int, input().split())
# for i in range(n-1):
#     a += d
# print(a)

#bài 55
# n=input()
# print(ord(n))

#bài 56
# a = input()
# print(a.lower())

#bài 57
# a = input()
# print(a.upper())

#bài 58

print(ord("a"))
print(chr(97).upper())