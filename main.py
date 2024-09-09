import customtkinter
import random



# set constants
TIMER = 30


#globals
list_to_type = []
guide_typing_words = ""
counter = 0
user_text = ""
t = TIMER

# text
instructions = "Find your typing speed in words per minute. Click the generate button below, then start the timer and type out the text you see on screen."
start_typing = "Click the button below to start your test"

#TODO 1 - create directory of words to type for test
word_list = ["english", "reflection", "time", "more", "old", "age", "begin", "after", "young", "project", "was", "hard",
         "soft", "next", "before", "what","how", "little", "big", "house", "place", "problem", "find", "search",
         "never", "always", "could", "follow", "last", "first", "child", "where", "because","face", "leg", "arm",
         "find", "line", "well", "many", "feel", "good", "he", "she", "it", "so", "need", "interest", "high", "low",
         "through", "say", "mean","stand", "will", "part", "early", "late", "begin", "end", "long", "short", "plan",
         "hand", "foot", "camera", "computer", "monkey", "dog", "cat", "bird", "sought","study", "many", "work",
         "present", "write", "read", "type", "trust", "fight", "find", "against", "madness", "life", "system",
         "possible", "by","develop", "general", "nation", "much", "back", "fact", "no", "change", "same", "just",
         "real", "fake", "help", "picture", "computer", "day", "night", "true", "false", "row", "column", "main",
         "find", "trust", "lies", "myth", "by", "and", "it", "bite", "right", "wrong", "watch", "type", "listen",
         "touch", "find", "lose", "forget", "win", "doubt", "ask", "answer"]




def word_count(string):
    count = 0
    for i in range(0, len(string)):
        if string[i] == " ":
            count += 1
    return count


#TODO 2 - choose words from directory as a test
def select_words(words):
    global list_to_type, guide_typing_words
    list_to_type = []
    wordcount = len(words)-1
    counter = 0
    while counter < 120:
        word_choice = random.randint(1, wordcount)
        try:
            if word_choice != list_to_type[-1]:
                list_to_type.append(words[word_choice].strip('"'))
                counter += 1
        except IndexError:
            list_to_type.append(words[word_choice].strip('"'))




#TODO 3 - display chosen words
def generate_text():
    select_words(word_list)
    global guide_typing_words, list_to_type
    guide_typing_words = ""
    for word in list_to_type:
        guide_typing_words += f"{word} "
    var.set(guide_typing_words)


def delete():
    user_text_box.delete(0.0, 'end')


#TODO 5 - get the users typing input
def get_user_text():
    user_text = user_text_box.get(0.0, "end")
    check_wpm(guide_typing_words, user_text)

#TODO 7 - create a time limit
def start_timer():
    global t, timer
    if t:
        user_text_box.configure(state="normal")
        minutes, seconds = divmod(t, 60)
        timer = f'{minutes:02d}:{seconds:02d}'
        canvas.itemconfig(timer_text, text=timer)
        t -= 1
        root.after(1000, start_timer)
    else:
        canvas.itemconfig(timer_text, text="Times up!")
        root.after_cancel(timer)
        get_user_text()
        t=TIMER
        user_text_box.configure(state="disabled")




#TODO 6 - compare the users input with the original sentence
def check_wpm(initial_text, inputted_text):
    initial_list = initial_text.split()
    inputted_list = inputted_text.split()
    del initial_list[len(inputted_list):]
    compared_list = [i == j for i, j in zip(initial_list, inputted_list)]
    wpm = 0
    mistakes = 0
    for n in compared_list:
        if n:
            wpm += 1
        else:
            mistakes += 1
    total_words = wpm+mistakes
    adj_wpm = wpm * 60/TIMER
    try:
        correct_pct = (wpm / total_words) * 100
    except ZeroDivisionError:
        pass
    wpm_label.configure(text=f"Your typing speed is {str(adj_wpm)} correct words per minute, and you made {mistakes} mistakes this time.\nYour typing accuracy was {correct_pct}%")


#TODO 8 - create results screen (showing: words typed, words typed correctly, accuracy %, wpm)
def round_statistics():
    top = customtkinter.CTkToplevel(root)
    top.geometry("500x250")
    top.title("Stats")
    top.attributes('-topmost', 'true')
    pass

def reset():
    global t
    reset = ""
    var.set(reset)
    user_text_box.configure(state="normal")
    user_text_box.delete(0.0, 'end')
    user_text_box.configure(state="disabled")
    if t:
        t=0
        t = TIMER
    else:
        t = TIMER
    print("time reset")
    wpm_label.configure(text="")



# CTk items
# CTk items
root = customtkinter.CTk()
root.title("Typing Speed Test")
root.geometry("1200x700")

var = customtkinter.StringVar()
var.set(guide_typing_words)


instructions_label = customtkinter.CTkLabel(root, text=instructions, font=("Ariel", 16))
instructions_label.pack(padx=5, pady=5)

button_frame = customtkinter.CTkFrame(root, fg_color="transparent")
button_frame.pack()
canvas = customtkinter.CTkCanvas(button_frame, width=300, height=50)
timer_text = canvas.create_text(150, 25, text=f"{TIMER} Seconds", fill="black", font=("Purisa", 24))

generate_text_button = customtkinter.CTkButton(button_frame, text="Generate Text", command=generate_text)
generate_text_button.grid(row=0, column=0)

reset_text_button = customtkinter.CTkButton(button_frame, text="Reset", command=reset)
reset_text_button.grid(row=0, column=2)


text_label = customtkinter.CTkLabel(root, textvariable=var, wraplength=1000, font=("Ariel", 16))
text_label.pack(pady=15)

#TODO 4 - create a place for user to type, and view typed text
user_text_box = customtkinter.CTkTextbox(root, width=600, height=300)
user_text_box.configure(state="disabled")
user_text_box.pack()

canvas.grid(row=1, column=1, pady=20)

start_timer_button = customtkinter.CTkButton(button_frame, text="Start Timer", command=start_timer)
start_timer_button.grid(row=0, column=1, padx=10)

wpm_label = customtkinter.CTkLabel(root, text="", font=("Ariel", 18))
wpm_label.pack(pady=15)

root.mainloop()