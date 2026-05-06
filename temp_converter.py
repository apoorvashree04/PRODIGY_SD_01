import customtkinter as ctk

# Theme setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("420x520")
app.title("Temperature App")

# Main container (center card UI)
frame = ctk.CTkFrame(app, corner_radius=20)
frame.pack(pady=40, padx=20, fill="both", expand=True)

# Title
title = ctk.CTkLabel(frame, text="🌡️ Temperature Converter", 
                     font=("Arial", 20, "bold"))
title.pack(pady=(20,10))

# Input field
entry = ctk.CTkEntry(frame, placeholder_text="Enter temperature", height=40)
entry.pack(pady=10, padx=20, fill="x")

# Dropdown
unit_option = ctk.CTkOptionMenu(frame, 
                               values=["Celsius", "Fahrenheit", "Kelvin"])
unit_option.pack(pady=10)

# Result label
result = ctk.CTkLabel(frame, text="", font=("Arial", 16))
result.pack(pady=20)

# Convert function
def convert():
    try:
        temp = float(entry.get())
        unit = unit_option.get()

        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result.configure(text=f"🔥 {f:.2f} °F\n❄️ {k:.2f} K")

        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result.configure(text=f"🌡️ {c:.2f} °C\n❄️ {k:.2f} K")

        elif unit == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result.configure(text=f"🌡️ {c:.2f} °C\n🔥 {f:.2f} °F")

    except:
        result.configure(text="❌ Invalid input")

# Buttons row
btn_frame = ctk.CTkFrame(frame, fg_color="transparent")
btn_frame.pack(pady=10)

convert_btn = ctk.CTkButton(btn_frame, text="Convert", command=convert)
convert_btn.grid(row=0, column=0, padx=10)

def clear():
    entry.delete(0, "end")
    result.configure(text="")

clear_btn = ctk.CTkButton(btn_frame, text="Clear", command=clear)
clear_btn.grid(row=0, column=1, padx=10)

# Theme toggle
def toggle_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

toggle_btn = ctk.CTkButton(frame, text="🌙 Toggle Theme", command=toggle_theme)
toggle_btn.pack(pady=15)

app.mainloop()