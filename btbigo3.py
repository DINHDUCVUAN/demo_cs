n = int(input())  
i = 0  
a = 0  
b = 0  
c = 0  
while i < n:  
    while a < n:  
        while b < n:  
            b = b + 1  
        a = a + 1  
    while c < n:  
        c = c + 1  
    i = i + 10
print(f"Độ phức tạp là O({n**3})")