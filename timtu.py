products = ["cat", "banana", "batman", "car", "cow", "alibaba"]  
index = -1  
timtu=input("Nhập từ")
for i in range(len(products)):  
    if products[i].startswith(timtu):  
        index = i  
        print(f"Từ là: {products[i]}, Index: {index}")  
        break  
if index == -1:  
    print(f"Ko có từ {timtu} trong danh sách")