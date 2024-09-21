import customtkinter  

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green") 
 
root = customtkinter.CTk()  
root.title("main customtkinter")   
root.geometry("500x300")  

root.resizable(width=False, height=False)
root.mainloop()