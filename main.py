import customtkinter as ctk 
from pypresence import Presence 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

pulse = ctk.CTk()
pulse.geometry("941x644")
pulse.minsize(941, 644)
pulse.title("Pulse Presence")
pulse.iconbitmap("assets/logo.ico")

frame = ctk.CTkFrame(
    master=pulse,
    width=100,
    height=300,
)
frame.pack(
    pady=10,
    padx=5,
    fill="both",
    expand=True
)
"""frame.place(
    x=5,
    y=5
)"""

label = ctk.CTkLabel(
    master=frame,
     text="Custom"
)
label.pack(
    pady=12,
    padx=10
)
def get_data():
    id=champ1.get()
    print(id)
    State=champ2.get()
    print(State)
    Img=champ3.get()
    print(Img)
    Text=champ4.get()
    print(Text)
    URL=champ5.get()
    print(URL)

    RPC = Presence(id)

    RPC.connect()

    RPC.update(
        state=State,
        large_image=Img,
        buttons=[{
            "label": Text,
            "url": URL
        }]
    )

label2 = ctk.CTkLabel(
    master=frame, 
    text="Client Id :",
    width=350,
    justify="left",
    anchor="w",
)
label2.place(
    x=295,
    y=67
)
champ1 = ctk.CTkEntry(
    master=frame,
    placeholder_text="ex : 1123612385421312052",
    width=170,
)
champ1.pack(
    pady=15,
    padx=10
)

label3 = ctk.CTkLabel(
    master=frame,
    text="State :",
    width=350,
    justify="left",
    anchor="w",
)
label3.place(
    x=312,
    y=125
)
champ2 = ctk.CTkEntry(
    master=frame,
    placeholder_text="ex : My dream",
    width=170,
)
champ2.pack(
    pady=15,
    padx=10
)

label4 = ctk.CTkLabel(
    master=frame,
    text="Large Image :",
    width=350,
    justify="left",
    anchor="w",
)
label4.place(
    x=270,
    y=182
)
champ3 = ctk.CTkEntry(
    master=frame,
    placeholder_text="Votre image",
    width=170,
)
champ3.pack(
    pady=15,
    padx=10
)

label5 = ctk.CTkLabel(
    master=frame,
    text="Text Button :",
    width=350,
    justify="left",
    anchor="w",
)
label5.place(
    x=278,
    y=242
)
champ4 = ctk.CTkEntry(
    master=frame,
    placeholder_text="ex : Support",
    width=170,
)
champ4.pack(
    pady=15,
    padx=10
)

label6 = ctk.CTkLabel(
    master=frame,
    text="URL Button :",
    width=350,
    justify="left",
    anchor="w",
)
label6.place(
    x=278,
    y=300
)
champ5 = ctk.CTkEntry(
    master=frame,
    placeholder_text="ex : https://discord.gg/KW4jHyMjJJ",
    width=170,
)
champ5.pack(
    pady=15,
    padx=10
)
button = ctk.CTkButton(master=frame, text="Connexion", command=get_data)
button.pack(pady=12, padx=10)

pulse.mainloop()

