from tkinter import *
from tkinter import messagebox

def get_height():
    height = float(ENTRY2.get())
    return height

def get_weight():
    weight = float(ENTRY1.get())
    return weight

def calculate_bmi(a=""):
    print(a)
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 15.0:
            res = "Your BMI is " + str(bmi) + "\nVery severely underweight!"
            messagebox.showinfo("Result", res)
        elif 15.0 < bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nSeverely underweight!"
            messagebox.showinfo("Result", res)
        elif 16.0 < bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nUnderweight!"
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nNormal."
            messagebox.showinfo("Result", res)
        elif 25.0 < bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nOverweight."
            messagebox.showinfo("Result", res)
        elif 30.0 < bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nModerately obese!"
            messagebox.showinfo("Result", res)
        elif 35.0 < bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nSeverely obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nSuper obese!!"
            messagebox.showinfo("Result", res)

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x400")
    root.configure(background="Black")
    root.title("BMI Calculator")
    root.resizable(width=False, height=False)
    LABLE = Label(root, bg="White", text="Welcome to BMI Calculator", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=55, y=0)
    LABLE1 = Label(root, bg="White", text="Enter Weight (kg):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(root, bd=8, width=6, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(root, bg="White", text="Enter Height (cm):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE2.place(x=55, y=121)
    ENTRY2 = Entry(root, bd=8, width=6, font="Roboto 11")
    ENTRY2.place(x=240, y=121)
    BUTTON = Button(bg="#2187e7", bd=12, text="BMI", padx=33, pady=15, command=calculate_bmi,
                    font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=115, y=250)
    root.mainloop()
