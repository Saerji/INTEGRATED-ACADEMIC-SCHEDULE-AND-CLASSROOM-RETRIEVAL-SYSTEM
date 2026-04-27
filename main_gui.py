import customtkinter as ctk
from tkinter import messagebox
import logic_package

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("1100x600")
root.configure(fg_color = "#F8F4EC")

sidebar = ctk.CTkFrame(root, fg_color="#BEC5A4", width=220)
sidebar.pack(side="left", fill="y")
sidebar.propagate(False)

main_area = ctk.CTkFrame(root, fg_color="#F8F4EC", corner_radius=0)
main_area.pack(side="left", fill="both", expand=True)

logo_frame = ctk.CTkFrame(sidebar, fg_color="#6B8F5E", corner_radius=0, height=100)
logo_frame.pack(fill="x")
logo_frame.pack_propagate(False)

ctk.CTkLabel(logo_frame, text="🎓  BSU",
             font=ctk.CTkFont("Georgia", 20, "bold"),
             text_color="#F8F4EC").pack(expand=True)

ctk.CTkLabel(sidebar, text="Welcome!", font=("Arial",20,"bold")).pack(pady=10)
ctk.CTkFrame(sidebar, fg_color="gray", height=1).pack(fill="x", padx=15, pady=8)

sidebar_nav = [
    ("Add Schedule", "add"),
    ("Search Schedule/s", "search"),
    ("View Schedules", "view"),
    ("Update Schedule", "update"),
    ("Delete Schedule", "delete")
]

for i, view in sidebar_nav:
    btn = ctk.CTkButton (sidebar,
                         text = f"{i}",
                         font = ("Georgia", 17, "bold"),
                         fg_color="transparent",
                         text_color="#344E41",
                         hover_color="#F1EAD8",
                         corner_radius=3,
                         height=55,
                         command=lambda v=view : switch_view(v))
    btn.pack(fill="x", pady=10, padx=0)
    
exit_btn = ctk.CTkButton (sidebar,
                          text="Exit",
                          font = ("Georgia", 15, "bold"),
                          fg_color="transparent",
                          text_color="#344E41",
                          hover_color="#BEC5A4",
                          command=None)
exit_btn.pack(pady=21)

title_bar = ctk.CTkFrame (main_area,
                          fg_color="transparent", 
                          width=220, 
                          height=100,
                          corner_radius=0)
title_bar.propagate(False)
title_bar.pack(fill="x",side="top")

title = ctk.CTkLabel(title_bar,
                     text="INTEGRATED ACADEMIC SCHEDULE\nAND CLASSROOM RETRIEVAL SYSTEM",
                     font=("Georgia", 28, "bold"),
                     text_color="#344E41",
                     justify="left",
                     anchor="w")
title.pack(padx=5,pady=0, side="left")

content_frame = ctk.CTkFrame(main_area, fg_color="#F8F4EC", corner_radius=0)
content_frame.pack(fill="both", expand=True, padx=20, pady=20)



def show_add_schedule():
    ctk.CTkLabel(content_frame,
                 text="Add Schedule",
                 font=("Georgia", 24, "bold"),
                 text_color="#344E41").pack(padx=20, pady=20)
    


def show_search_schedule():
    ctk.CTkLabel(content_frame,
                 text="Search",
                 font=("Arial", 20, "bold")
                 ).pack()

def show_view_schedules():
    ctk.CTkLabel(content_frame,
                 text="View",
                 font=("Arial", 20, "bold")
                 ).pack()

def show_update_schedule():
    ctk.CTkLabel(content_frame,
                 text="update Sched",
                 font=("Arial", 20, "bold")
                 ).pack()
    
def show_delete_schedule():
    ctk.CTkLabel(content_frame,
                 text="delete sched",
                 font=("Arial", 20, "bold")
                 ).pack()
    
def switch_view(view_name):
    for widget in content_frame.winfo_children():
        widget.destroy()
        
    if view_name == "add":
        show_add_schedule()
    elif view_name == "search":
        show_search_schedule()
    elif view_name == "view":
        show_view_schedules()
    elif view_name == "update":
        show_update_schedule()
    elif view_name == "delete":
        show_delete_schedule()
        
        
root.mainloop()
    