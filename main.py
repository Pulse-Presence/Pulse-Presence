import customtkinter as ctk
from pystyle import Colors, Colorate
from pypresence import Presence

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

pulse = ctk.CTk()
pulse.geometry("950x650")
pulse.minsize(950, 650)
pulse.maxsize(950, 650)
pulse.title("Pulse Presence")
pulse.iconbitmap("assets/logo.ico")

                # Connection Discord

def connect():
    entry_values = {
        "id": id_entry.get(),
        "details": details_entry.get(),
        "state": state_entry.get(),
        "min_party": min_entry.get(),
        "max_party": max_entry.get(),
        "large_img": large_entry.get(),
        "largtext": largetext_entry.get(),
        "small_img": small_entry.get(),
        "smalltext": smalltext_entry.get(),
        "label1": button1_entry.get(),
        "url1": button1_url_entry.get(),
        "label2": button2_entry.get(),
        "url2": button2_url_entry.get()
    }

    mandatory = ['id', 'details']
    for key in mandatory:
        if entry_values[key] == '':
            error = "Vous devez fournir une valeur pour le champ " + key
            print(Colorate.Color(Colors.red, error, True))
            return

    button=[]
    if entry_values['label1'] and entry_values['url1']:
        button.append(
            {
                "label": entry_values['label1'],
                "url": entry_values['url1']
            }
        )
    else:
        pass

    if entry_values['label2'] and entry_values['url2']:
        button.append(
            {
                "label": entry_values['label2'],
                "url": entry_values['url2']
            }
        )
    else:
        pass

    global RPC
    RPC = Presence(entry_values['id'])
    RPC.connect()

    RPC.update(
        details=entry_values['details'],
        state=entry_values['state'] if entry_values['state'] else None,
        party_size=[int(entry_values['min_party']), int(entry_values['max_party'])] if entry_values['min_party'] and entry_values['max_party'] else None,
        large_image=entry_values['large_img'] if entry_values['large_img'] else None,
        large_text=entry_values['largtext'] if entry_values['largtext'] else None,
        small_image=entry_values['small_img'] if entry_values['small_img'] else None,
        small_text=entry_values['smalltext'] if entry_values['smalltext'] else None,
        buttons=button if button else None
    )
    print(Colorate.Color(Colors.green, "Connected to Discord !", True))

def update():
    entry_values = {
        "id": id_entry.get(),
        "details": details_entry.get(),
        "state": state_entry.get(),
        "min_party": min_entry.get(),
        "max_party": max_entry.get(),
        "large_img": large_entry.get(),
        "largtext": largetext_entry.get(),
        "small_img": small_entry.get(),
        "smalltext": smalltext_entry.get(),
        "label1": button1_entry.get(),
        "url1": button1_url_entry.get(),
        "label2": button2_entry.get(),
        "url2": button2_url_entry.get()
    }

    mandatory = ['id', 'details']
    for key in mandatory:
        if entry_values[key] == '':
            print(Colorate.Color(Colors.red, "Vous devez fournir une valeur pour le champ " + key, True))
            return

    button=[]
    if entry_values['label1'] and entry_values['url1']:
        button.append(
            {
                "label": entry_values['label1'],
                "url": entry_values['url1']
            }
        )
    else:
        pass

    if entry_values['label2'] and entry_values['url2']:
        button.append(
            {
                "label": entry_values['label2'],
                "url": entry_values['url2']
            }
        )
    else:
        pass

    RPC.clear()

    RPC.update(
        details=entry_values['details'],
        state=entry_values['state'] if entry_values['state'] else None,
        party_size=[int(entry_values['min_party']), int(entry_values['max_party'])] if entry_values['min_party'] and entry_values['max_party'] else None,
        large_image=entry_values['large_img'] if entry_values['large_img'] else None,
        large_text=entry_values['largtext'] if entry_values['largtext'] else None,
        small_image=entry_values['small_img'] if entry_values['small_img'] else None,
        small_text=entry_values['smalltext'] if entry_values['smalltext'] else None,
        buttons=button if button else None
    )
    log="Updated !"
    print(Colorate.Color(Colors.blue, log, True))

def disconnect():
    RPC.close()
    print(Colorate.Color(Colors.yellow, "Disconnected from Discord !", True))

                        # Frame (cadre gris)

frame1 = ctk.CTkFrame(
    master=pulse,
    width=460,
    height=170,
)
frame1.pack(
    pady=10,
    padx=10,
    expand=False,
)
frame1.place(
    x=10,
    y=10
)

frame2 = ctk.CTkFrame(
    master=pulse,
    width=460,
    height=310,
)
frame2.pack(
    pady=10,
    padx=10,
    expand=False,
)
frame2.place(
    x=480,
    y=10
)

frame3 = ctk.CTkFrame(
    master=pulse,
    width=460,
    height=310,
)
frame3.pack(
    pady=10,
    padx=10,
    expand=False,
)
frame3.place(
    x=10,
    y=330
)

frame4 = ctk.CTkFrame(
    master=pulse,
    width=460,
    height=130,
)
frame4.pack(
    pady=10,
    padx=10,
    expand=False,
)
frame4.place(
    x=10,
    y=190
)

                        # Bouton

button1 = ctk.CTkButton(
    master=pulse,
    text="Connect",
    font=("Arial", 15),
    fg_color="#5865F2",
    hover_color="#5865F2",
    width=150,
    height=35,
    command=connect
)
button1.pack(
    pady=12,
    padx=10)
button1.place(
    x=650,
    y=400
)

button2 = ctk.CTkButton(
    master=pulse,
    text="Update", 
    font=("Arial", 15), 
    text_color="black", 
    fg_color="#57F287", 
    hover_color="#57F287",
    width=150,
    height=35,
    command=update
)
button2.pack(
    pady=12, 
    padx=10
)
button2.place(
    x=650,
    y=460
)

button3 = ctk.CTkButton(
    master=pulse,
    text="Disconnect", 
    font=("Arial", 15), 
    fg_color="#ED4245", 
    hover_color="#ED4245",
    width=150,
    height=35,
    command=disconnect
)
button3.pack(
    pady=12, 
    padx=10
)
button3.place(
    x=650,
    y=520
)

                        # status

id_label = ctk.CTkLabel(
    master=frame1,
    text="Client ID : ",
    width=350,
    justify="left",
    anchor="w",
)
id_label.place(
    x=100,
    y=20
)
id_entry = ctk.CTkEntry(
    master=frame1,
    placeholder_text="ex : 1123612385421312052",
    width=170
)
id_entry.place(
    x=170,
    y=20,
)

details = ctk.CTkLabel(
    master=frame1,
    text="Details : ",
    width=350,
    justify="left",
    anchor="w",
)
details.place(
    x=108,
    y=70
)
details_entry = ctk.CTkEntry(
    master=frame1,
    placeholder_text="ex : Playing with friends",
    width=170
)
details_entry.place(
    x=170,
    y=70,
)

state = ctk.CTkLabel(
    master=frame1,
    text="State : ",
    width=350,
    justify="left",
    anchor="w",
)
state.place(
    x=117,
    y=120
)
state_entry = ctk.CTkEntry(
    master=frame1,
    placeholder_text="ex : My world",
    width=170
)
state_entry.place(
    x=170,
    y=120,
)
                    # Party frame

button1_title = ctk.CTkLabel(
    master=frame4,
    text="Party (require \"State\") ",
    width=400,
    justify="center",
    anchor="w",
)
button1_title.place(
    x=185,
    y=10
)

min_party = ctk.CTkLabel(
    master=frame4,
    text="Min Party : ",
    width=350,
    justify="left",
    anchor="w",
)
min_party.place(
    x=50,
    y=70
)
min_entry = ctk.CTkEntry(
    master=frame4,
    placeholder_text="ex : 0",
    width=50
)
min_entry.place(
    x=120,
    y=70,
)

max_party = ctk.CTkLabel(
    master=frame4,
    text="Max Party : ",
    width=350,
    justify="left",
    anchor="w",
)
max_party.place(
    x=270,
    y=70
)
max_entry = ctk.CTkEntry(
    master=frame4,
    placeholder_text="ex : 10",
    width=50
)
max_entry.place(
    x=340,
    y=70,
)
                # Image (small and large)

large_img = ctk.CTkLabel(
    master=frame3,
    text="Large Image : ",
    width=350,
    justify="left",
    anchor="w",
)
large_img.place(
    x=75,
    y=50
)
large_entry = ctk.CTkEntry(
    master=frame3,
    placeholder_text="ex : img",
    width=170
)
large_entry.place(
    x=170,
    y=50,
)

largetext_img = ctk.CTkLabel(
    master=frame3,
    text="Text Large Image : ",
    width=350,
    justify="left",
    anchor="w",
)
largetext_img.place(
    x=45,
    y=100
)
largetext_entry = ctk.CTkEntry(
    master=frame3,
    placeholder_text="ex : That's my world",
    width=170
)
largetext_entry.place(
    x=170,
    y=100,
)

small_img = ctk.CTkLabel(
    master=frame3,
    text="Small Image : ",
    width=350,
    justify="left",
    anchor="w",
)
small_img.place(
    x=75,
    y=180
)
small_entry = ctk.CTkEntry(
    master=frame3,
    placeholder_text="ex : img",
    width=170
)
small_entry.place(
    x=170,
    y=180,
)

smalltext = ctk.CTkLabel(
    master=frame3,
    text="Text Small Image : ",
    width=350,
    justify="left",
    anchor="w",
)
smalltext.place(
    x=45,
    y=230
)
smalltext_entry = ctk.CTkEntry(
    master=frame3,
    placeholder_text="ex : That's my world",
    width=170
)
smalltext_entry.place(
    x=170,
    y=230,
)

                # Button (button 1 & button 2)

button1_title = ctk.CTkLabel(
    master=frame2,
    text="Button 1 : ",
    width=350,
    justify="center",
    anchor="w",
)
button1_title.place(
    x=200,
    y=10
)

button1_label = ctk.CTkLabel(
    master=frame2,
    text="Text : ",
    width=350,
    justify="left",
    anchor="w",
)
button1_label.place(
    x=120,
    y=40
)
button1_entry = ctk.CTkEntry(
    master=frame2,
    placeholder_text="ex : Join",
    width=170
)
button1_entry.place(
    x=170,
    y=40,
)
""" button1_url, button1_label """
button1_url = ctk.CTkLabel(
    master=frame2,
    text="URL : ",
    width=350,
    justify="left",
    anchor="w",
)
button1_url.place(
    x=120,
    y=90
)
button1_url_entry = ctk.CTkEntry(
    master=frame2,
    placeholder_text="ex : https://discord.gg/invite",
    width=170
)
button1_url_entry.place(
    x=170,
    y=90,
)

button2_title = ctk.CTkLabel(
    master=frame2,
    text="Button 2 : ",
    width=350,
    justify="center",

)
button2_title.place(
    x=55,
    y=130
)

button2_label = ctk.CTkLabel(
    master=frame2,
    text="Text : ",
    width=350,
    justify="left",
    anchor="w",
)
button2_label.place(
    x=120,
    y=170
)

button2_entry = ctk.CTkEntry(
    master=frame2,
    placeholder_text="ex : Join",
    width=170
)
button2_entry.place(
    x=170,
    y=170,
)

button2_url = ctk.CTkLabel(
    master=frame2,
    text="URL : ",
    width=350,
    justify="left",
    anchor="w",
)
button2_url.place(
    x=120,
    y=220
)
button2_url_entry = ctk.CTkEntry(
    master=frame2,
    placeholder_text="ex : https://discord.gg/invite",
    width=170
)
button2_url_entry.place(
    x=170,
    y=220,
)

pulse.mainloop()
