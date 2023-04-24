import tkinter

# window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=400, height=200)

def BMI_Calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            result = "Under Weight"
        elif 18.5 <= bmi <= 24.9:
            result = "Normal"
        elif 25 <= bmi <= 29.9:
            result = "Over Weight"
        elif 30 <= bmi <= 34.9:
            result = "Obesity (Class 1)"
        elif 35 <= bmi <= 39.9:
            result = "Obesity (Class 2)"
        else:  # bmi > 40
            result = "Extreme Obesity"

        result_label.config(text=f"BMI: {bmi:.2f}, {result}")

    except ValueError:
        result_label.config(text="Please enter valid values for weight and height.")

label = tkinter.Label(text="Enter Your Weight (kg)")
label.pack()

weight_entry = tkinter.Entry()
weight_entry.pack()

label_2 = tkinter.Label(text="Enter Your Height (cm)")
label_2.pack()

height_entry = tkinter.Entry()
height_entry.pack()

# button
calculate_button = tkinter.Button(text="Calculate", command=BMI_Calculate)
calculate_button.pack()

# result label
result_label = tkinter.Label()
result_label.pack()

window.mainloop()