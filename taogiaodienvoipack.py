import customtkinter  

root = customtkinter.CTk()  
root.title("TechX")  
root.geometry("600x400")  

top_frame = customtkinter.CTkFrame(master=root, fg_color="pink")  
top_frame.pack(side="top", expand=True, fill="both")  

frame_yellow = customtkinter.CTkFrame(master=top_frame, fg_color="yellow")  
frame_yellow.pack(side="left", expand=True, fill="both")  

frame_red = customtkinter.CTkFrame(master=top_frame, fg_color="red")  
frame_red.pack(side="left", expand=True, fill="both")  

frame_gray = customtkinter.CTkFrame(master=bot_frame, fg_color="gray")  
frame_gray.pack(side="left", expand=True, fill="both")  

frame_blue = customtkinter.CTkFrame(master=bot_frame, fg_color="blue")  
frame_blue.pack(side="left", expand=True, fill="both")  

root.mainloop()