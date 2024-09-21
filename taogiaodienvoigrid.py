import customtkinter as ctk  

# Khởi tạo ứng dụng  
ctk.set_appearance_mode("System")  # Chế độ appearance: "Light" hoặc "Dark"  
ctk.set_default_color_theme("blue")  # Đặt chủ đề màu sắc  

app = ctk.CTk()  # Tạo cửa sổ chính  
app.geometry("800x600")  # Kích thước cửa sổ  
app.title("Giao diện với 4 Frame")  

# Tạo 4 frame với màu sắc khác nhau  
frame1 = ctk.CTkFrame(app, fg_color="yellow")  
frame1.grid(row=0, column=0, sticky="nsew")  

frame2 = ctk.CTkFrame(app, fg_color="red")  
frame2.grid(row=0, column=1, sticky="nsew")  

frame3 = ctk.CTkFrame(app, fg_color="gray")  
frame3.grid(row=1, column=0, sticky="nsew")  

frame4 = ctk.CTkFrame(app, fg_color="blue")  
frame4.grid(row=1, column=1, sticky="nsew")  

# Điều chỉnh tỷ lệ các hàng và cột  
app.grid_rowconfigure(0, weight=1)  # Hàng 0 chiếm phần không gian  
app.grid_rowconfigure(1, weight=1)  # Hàng 1 chiếm phần không gian  
app.grid_columnconfigure(0, weight=1)  # Cột 0 chiếm phần không gian  
app.grid_columnconfigure(1, weight=1)  # Cột 1 chiếm phần không gian  

# Chạy ứng dụng  
app.mainloop()