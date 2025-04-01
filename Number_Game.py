from tkinter import *
from tkinter import messagebox
import random

count = 0
score = 10

def Hard():
    clear_Screen()

    a = random.randint(1,500)
    b = random.randint(501, 1000)

    global count, score
    score = 100
    count = 0
    tries = 10


    Label(window, text="Hard Level", fg="red", bg="black", font=("Times New Roman", 23, 'bold') ).pack()

    global score_label
    score_label = Label(window, text=f"Score: {score}", font=("Calibre", 10))
    score_label.pack(anchor="ne", padx=10, pady=10)

    GuessNumber = Label(window, text=f"Enter a Number from {a} to {b}",bg="black", fg="white",font=("Times New Roman", 13, 'bold'))
    GuessNumber.pack(pady=20)

    #making input box empty
    Guessvalue = IntVar(value="")

    global Guessentry
    Guessentry = Entry(window, textvariable=Guessvalue)
    Guessentry.pack()
    secretNum = random.randint(a, b)

    Button(text="    CHECK   ", command=lambda: hint(secretNum,tries), bg='blue', fg="white", bd=3).pack(padx=10, pady=10)


    btn_frame = Frame(window, bg="black")
    btn_frame.pack(side="bottom", fill="x", expand=False)

    Button(btn_frame, text="    BACK   ", command=mainscreen, bg='grey', fg="white", bd=3).pack(side="left", padx=10,
                                                                                                pady=10)
    Button(btn_frame, text="    EXIT   ", command=quit, bg='black', fg="white", bd=3).pack(side="right", padx=10,
                                                                                           pady=10)
    # Restart Button
    Button(btn_frame, text="Restart Level", command=Hard, bg="red", fg="white", bd=3).pack(side="left", padx=125, pady=10)

    global display
    display = StringVar()
    display.set(f"You have {tries} tries")
    Label(window, textvariable=display, bg="black", fg= "white").pack()

    global display2
    display2 = StringVar()
    display2.set("")
    Label(window, textvariable=display2, fg="white", bg="black").pack()

def Medium():
    clear_Screen()
    global count, score
    score = 50
    count = 0
    tries = 7

    Label(window, text="Medium Level", fg="green", bg="black",font=("Times New Roman", 23, 'bold') ).pack()


    global score_label
    score_label = Label(window, text=f"Score: {score}", font=("Calibre", 12))
    score_label.pack(anchor="ne", padx=10, pady=10)

    GuessNumber = Label(window, text='Enter a Number from 1 to 100',bg="black", fg="white",font=("Times New Roman", 13, 'bold'))
    GuessNumber.pack(pady=20)

    #making input box empty
    Guessvalue = IntVar(value="")

    global Guessentry
    Guessentry = Entry(window, textvariable=Guessvalue)
    Guessentry.pack()
    secretNum = random.randint(1, 100)

    Button(text="    CHECK   ", command=lambda: hint(secretNum,tries), bg='blue', fg="white", bd=3).pack(padx=10, pady=10)

    btn_frame = Frame(window, bg="black")
    btn_frame.pack(side="bottom", fill="x", expand=False)

    Button(btn_frame, text="    BACK   ", command=mainscreen, bg='grey', fg="white", bd=3).pack(side="left", padx=10,
                                                                                                pady=10)
    Button(btn_frame, text="    EXIT   ", command=quit, bg='black', fg="white", bd=3).pack(side="right", padx=10,
                                                                                           pady=10)
    # Restart Button
    Button(btn_frame, text="Restart Level", command=Medium, bg="red", fg="white", bd=3).pack(side="left", padx=125,
                                                                                           pady=10)
    global display
    display = StringVar()
    display.set(f"You have {tries} tries")
    Label(window, textvariable=display, fg="white",bg="black").pack()

    global display2
    display2 = StringVar()
    display2.set("")
    Label(window, textvariable=display2, fg="white", bg="black").pack()


def Easy():
    clear_Screen()

    global count,score
    count = 0
    score = 10
    tries = 3

    Label(window, text="Easy Level", fg="yellow",bg="black", font=("Times New Roman", 23, 'bold')).pack()

    global score_label
    score_label = Label(window, text=f"Score: {score}", font=("Calibre", 12))
    score_label.pack(anchor="ne", padx=10, pady=10)

    GuessNumber = Label(window, text='Enter a Number from 1 to 10',bg="black", fg="white",font=("Times New Roman", 13, 'bold'))
    GuessNumber.pack(pady=20)

    #making input box empty
    Guessvalue = IntVar(value="")

    global Guessentry
    Guessentry = Entry(window, textvariable=Guessvalue)
    Guessentry.pack()
    secretNum = random.randint(1, 10)



    Button(text="    CHECK   ",command= lambda: hint(secretNum,tries), bg='blue', fg="white", bd=3).pack(pady=15)

    btn_frame = Frame(window, bg="black")
    btn_frame.pack(side="bottom" ,fill="x",expand=False)

    Button(btn_frame, text="    BACK   ", command=mainscreen, bg='grey', fg="white", bd=3).pack(side="left", padx=10, pady=10)

    Button(btn_frame, text="    EXIT   ", command=quit, bg='black', fg="white",bd=3).pack(side="right", padx=10, pady=10)

    # Restart Button
    Button(btn_frame, text="Restart Level", command=Easy, bg="red", fg="white", bd=3).pack(side="left", padx=125,
                                                                                           pady=10)

    global display
    display = StringVar()
    display.set(f"You have {tries} tries")
    Label(window, textvariable=display, fg="white",bg="black").pack()

    global display2
    display2 = StringVar()
    display2.set("")
    Label(window, textvariable=display2, fg="white", bg="black").pack()

def hint(actN,tries):
    global count,score, score_label
    count += 1
    actN = int(actN)
    userN = int(Guessentry.get())

    #checking number is prime or not
    def IsPrime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Will be used to display hints
    if count < tries:
        if userN < actN:
            score -= 1
            display.set(f"Your number is smaller than the secret number\n Tires left: {tries-count}")
        elif userN > actN:
            score -= 1
            display.set(f"Your number is larger than than the secret number\n Tires left: {tries-count}")
        else:
            display.set(f"Congratulations! You guessed it!\nYou guessed in {count} tries")

        if actN == userN:
            display2.set("")
        elif actN % 2 == 0:
            display2.set("The secret number is an even number")
        elif actN % 2 != 0 and IsPrime(actN):
            display2.set("The secret number not is divisible by 2 and a Prime Number")
        elif actN % 2 != 0 or IsPrime(actN):
            display2.set("The secret number is an odd number")

        score_label.config(text=f"Score: {score}")

    else:
        score -= 1
        score_label.config(text=f"Score: {score}")

        messagebox.showinfo("Game Over", f"Sorry, you've reached the maximum number of attempts.\nThe correct number was: {actN}")
        display.set(f"You lose\n The correct number was {actN}")





def mainscreen():
    clear_Screen()


    #Settinf Button Styles
    btn_style = {
        'width': 15,
        'height': 1,
        'bg': "#7B3F00",
        'fg': "white",
        'highlightbackground': "white",
        'highlightthickness': 1,
        'bd': 5,
        'font': ('Helvetica', 10, 'bold')
    }

    #LABELS
    Label(text="Number Guessing Game", fg="cyan", bg="black",font=("Times New Roman", 25, "bold")).pack()

    Label(text="Choose Difficulty Level", bg="black", fg="white",font=("Times New Roman", 12, "bold")).pack(pady=15)

    #BUTTONS
    Button(text="EASY", command=Easy,**btn_style).pack(pady=(20,5))
    Button(text="MEDIUM",command=Medium,**btn_style).pack(pady=5)
    Button(text="HARD", command= Hard, **btn_style).pack(pady=5)

    Label(text="----------  OR  ----------", bg="black", fg="white", font=("Times New Roman", 12, "bold")).pack(pady=5)
    Button(text="QUIT GAME", command=quit, **btn_style).pack(pady=5)


# Function to clear the screen widgets, frames or anything
def clear_Screen():
    for widget in window.winfo_children():
        widget.destroy()


#making a GUI interface
window = Tk()
window.geometry("500x400")
window.title("Number Guessing Game")
window.config(bg="black")
window.resizable(False, False)

# Calling main function
mainscreen()

window.mainloop()
