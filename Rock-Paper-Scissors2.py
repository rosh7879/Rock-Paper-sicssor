import tkinter as tk
from PIL import Image, ImageTk
import random as rd

root = tk.Tk()
root.title("Rock Paper Scissors")
root.config(bg="#ffa12f")
root.geometry("600x500")
root.resizable(False, False)


def load_image(path, size=(150,150)):
    img = Image.open(path)
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)


rock_image = load_image("hand.png")
paper_image = load_image("hand-paper.png")
scissors_image = load_image("scissors.png")

# Title
title = tk.Label(root, text="Rock Paper Scissors",
                 font=("Arial", 24, "bold"), bg="#ffa12f", fg="white")
title.pack(pady=20)

# Result label
result_label = tk.Label(root, text="Make your move!",
                        font=("Arial", 16), bg="#ffa12f", fg="white")
result_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#fda942")
button_frame.pack(pady=30)

def play(player_choice):
    computer_choice = rd.choice(["Rock", "Paper", "Scissors"])

    if player_choice == computer_choice:
        result = "Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Scissors" and computer_choice == "Paper") or
        (player_choice == "Paper" and computer_choice == "Rock")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(
        text=f"You chose {player_choice} | Computer chose {computer_choice}\n{result}"
    )


rock_btn = tk.Button(button_frame, image=rock_image,
                     command=lambda: play("Rock"), bd=0, bg="#ffa12f")
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, image=paper_image,
                      command=lambda: play("Paper"), bd=0, bg="#ffa12f")
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, image=scissors_image,
                         command=lambda: play("Scissors"), bd=0, bg="#ffa12f")
scissors_btn.grid(row=0, column=2, padx=10)

root.mainloop()
