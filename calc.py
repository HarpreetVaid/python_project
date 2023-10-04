from tkinter import *  # importing the tkinter library
import math

#creating tkinter window
root = Tk()

# title function change the tittle to calculator
root.title('Calculator')

root.iconbitmap(r"C:\Users\acer\Downloads\logo-removebg-preview.ico")

#setting the dimension of window
root.geometry('370x470')

# disable window resizing
#root.resizable(False, False)

# changing background
root['bg']="grey"


# Create a StringVar to hold the value of the entry
expression_value = StringVar()
equation = ""
expression_value.set("")

def adjust_text_size(event):

    new_height = root.winfo_height()  # Get the new height of the window
    new_width = root.winfo_width()    # Get the new width of the window
    font_size = new_height // 12
    paddingx = new_height // 36
    paddingy = new_width // 36

    # Update the font size for the entry field and buttons
    entry_field.config(font=("Arial", font_size))
    input_frame.grid_configure(padx=paddingx,pady=paddingy)
    button_frame.grid_configure(padx=paddingx,pady=paddingy)

    # update buttons size

    for button in buttons_list:
        button.config(font=("Arial", font_size//2))



#  function pressing different key

def button_click(function):
    global equation

    if function == 'C':
        expression_value.set("")
        equation = ""

    elif function == '+/-':
        change_sign()

    elif function == '.':
        dot_press()

    elif function == 'x':
        press_key("*")

    elif function == 'Sqrt':
        sqrt_press()

    elif function == 'Del':
        delete_key()

    elif function == '=':
        press_equal()

    else:
        press_key(function)


def press_equal():

    global equation

    if equation == "":
        return ""
    try:
            result = str(eval(equation))
            expression_value.set(result)
            equation = result
            return result
    except :
            expression_value.set("Error")
            equation = ""
            return ""

def dot_press():

    global equation

    if equation == "":
        press_key("0")
        press_key(".")

    elif not equation[-1].isdigit():
        if equation[-1] == ".":
            return
        press_key("0")
        press_key(".")

    else :
        press_key(".")



def press_key(key):

    global equation

    if key in  ["+","/","*"] and equation == "":
        return

    if key in ["+","/","*"] and equation[-1] in ["+","/","*"]:
        equationw = equation[:-1] + key
        expression_value.set(equation)
        return

    equation = equation + str(key)
    expression_value.set(equation)


def change_sign():

    global equation
    if equation[-1] == "+":
        new_expression = equation[:-1] + "-"
        equation = new_expression
        expression_value.set(new_expression)
        return

    if equation[-1] == "-":
        new_expression = equation[:-1] + "+"
        equation = new_expression
        expression_value.set(new_expression)
        return

    current_expression = equation

    if current_expression == "":
        new_expression = '-'

    elif current_expression and current_expression[0] == "-":
        new_expression = current_expression[1:]

    else:
        new_expression = "-" + current_expression

    equation = new_expression
    expression_value.set(new_expression)



def sqrt_press():

    global equation
    result  = press_equal()
    if result == "" :
        return

    if result[0] != '-':
        result = math.sqrt(float(result))
        expression_value.set(result)
        equation = str(result)
    else :
        expression_value.set("Value can't be negative")
        equation = ""


def delete_key():

    global equation
    equation = equation[:-1]
    expression_value.set(equation)



root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=10)
root.grid_columnconfigure(0, weight=1)
root.bind("<Configure>", adjust_text_size)

# Set the window icon using the iconbitmap method
#root.iconbitmap(os.path.join(script_dir, "calc.ico"))

# Create the input frame
input_frame = Frame(root, bd=5 ,background='black')
input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

# Create the Entry widget and set its font size
entry_field = Entry(input_frame, textvariable=expression_value, font=("Arial"),state="readonly")
entry_field.pack(fill="both", expand=True, padx=5, pady=5)

# create a frame for buttons
button_frame = Frame(root,bd = 8 )
button_frame.grid(row=1, column=0,padx = 10, pady=10, sticky='nsew')
button_data=["C","+/-","Sqrt","x","7","8","9","/","4","5","6","+","1","2","3","-","0",".","Del","="]
buttons_list=[]


for i in range(5):

    button_frame.grid_rowconfigure(i, weight=1)
    for j in range(4):

        no = int(i * 4 + j)
        button_frame.grid_columnconfigure(j, weight=1)
        button = Button(
                button_frame,
                text=button_data[no],
                padx=2,
                pady=2,
                command=lambda key=button_data[no]: button_click(key)
            )
        button.grid(row=i, column=j, sticky="nsew")
        buttons_list.append(button)

#Execute Tkinter
root.mainloop()
