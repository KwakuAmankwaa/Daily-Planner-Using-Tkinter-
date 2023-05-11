import tkinter as tk
import random

# Array containing motivational quotes

quotes = [
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "You are never too old to set another goal or to dream a new dream.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going.",
    "If you can't fly then run, if you can't run then walk, if you can't walk then crawl, but whatever you do you have to keep moving forward.",
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "You miss 100\'%'of the shots you don’t take.",
    "If you want to live a happy life, tie it to a goal, not to people or things.",
    "It's not whether you get knocked down, it's whether you get up.",
    "Success is stumbling from failure to failure with no loss of enthusiasm.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "The best way to predict your future is to create it.",
    "You can't build a reputation on what you are going to do.",
]


# Creates the window and frame

window = tk.Tk()
frame = tk.Frame(window)


# Start up window asking for user's name and date of plan

welcome = tk.Label(text= "Daily Planner", font=("Times New Roman", 30))
welcome.pack()

# User's name and Date of Plan are stored into string variables
user_var = tk.StringVar()
date_var = tk.StringVar()

# Used for Spacing
blank = tk.Label(text="")
blank.pack()


# Labels and entries created for user and date of plan

username = tk.Label(text="User", width=50)
username_entry = tk.Entry(textvariable=user_var)
username.pack()
username_entry.pack()


# Used for Spacing
blank = tk.Label(text="")
blank.pack()

date = tk.Label( text="Date of Plan", width=50)
date_entry = tk.Entry(textvariable=date_var)
date.pack()
date_entry.pack()


# Used for Spacing
blank = tk.Label( text="")
blank.pack()

# Function to get the username and date values and open new window
def newWindow():
    # Gets values entered by user
    username = user_var.get()
    date = date_var.get()

    # Creates new window and frame
    new_window = tk.Toplevel()
    new_frame = tk.Frame(new_window)


    # Labels to display values passed from the first page
    username_label = tk.Label(new_frame, text="Welcome " + username , font=("Arial", 20))
    date_label = tk.Label(new_frame, text="Date of Plan: " + date , font=("Arial", 20))
    
    # Packs labels into the frame
    username_label.pack()
    date_label.pack()

    # Used for Spacing
    blank = tk.Label(text="")
    blank.pack()

    # Frame for planner labels and entries
    planner_frame = tk.Frame(new_frame)



    # Loop that displays 12 hour format labels. (Both AM and PM)

    for hour in range(1, 13):
        hour_label = tk.Label(planner_frame, text=f"{hour}:00 AM")
        hour_label.grid(row=hour, column=0, pady=5)
        hour_entry = tk.Text(planner_frame, height=1, width=70)
        hour_entry.grid(row=hour, column=1, pady=5)
    for hour in range(1, 13):
        hour_label = tk.Label(planner_frame, text=f"{hour}:00 PM")
        hour_label.grid(row=hour+12, column=0, pady=5)
        hour_entry = tk.Text(planner_frame, height=1, width=70)
        hour_entry.grid(row=hour+12, column=1, pady=5)


   

    # Pack the planner frame on the left side of the parent frame
    planner_frame.pack(side=tk.LEFT)

    # Create a frame for the meal plan labels and entries
    mealplan_frame = tk.Frame(new_frame, padx=50, pady=80)
    mealplan_frame.pack()

    # Add labels and entries for meal plan
    breakfast_label = tk.Label(mealplan_frame, text="Breakfast")
    breakfast_label.pack()
    breakfast_entry = tk.Text(mealplan_frame, height=5, width=30)
    breakfast_entry.pack()

    lunch_label = tk.Label(mealplan_frame, text="Lunch")
    lunch_label.pack()
    lunch_entry = tk.Text(mealplan_frame, height=5, width=30)
    lunch_entry.pack()

    dinner_label = tk.Label(mealplan_frame, text="Dinner")
    dinner_label.pack()
    dinner_entry = tk.Text(mealplan_frame, height=5, width=30)
    dinner_entry.pack()


    # Pack the meal plan frame on the right side of the parent frame
    mealplan_frame.pack()

    # Create a label to display the motivational quote
    quote_label = tk.Label(new_frame, text="", font=("Arial", 16),padx=50, pady=80)
    quote_label.pack()

    # Function to display a random motivational quote
    def display_quote():
        random_quote = random.choice(quotes)
        quote_label.config(text=random_quote)

    # Create a button to show a random quote
    # Create a button to show a random quote
    quote_button = tk.Button(new_frame, text="Show Quote", command=display_quote, padx=50, pady=80)
    quote_button.pack(pady=10, anchor='s')


    # Pack the frames into the window
    new_frame.pack()



# Create the enter button
btn_enter = tk.Button(text="Enter", command=newWindow)
btn_enter.pack(ipadx=10)

# Pack the frame into the window and start the main event loop
frame.pack()
window.mainloop()
