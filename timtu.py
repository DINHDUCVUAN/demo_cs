products = ["cat", "banana", "batman", "car", "cow", "alibaba"]  
timtu = input("Nhập từ: ")
found_items = False 
for i in range(len(products)):  
    if timtu in products[i]:  
        print(f"Từ là: {products[i]}, Index: {i}")  
        found_items=True
if not found_items:  
    print(f"Không có từ '{timtu}' trong danh sách.")