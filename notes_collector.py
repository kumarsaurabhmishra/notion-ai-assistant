import os
from datetime import datetime

def collect_note(user):
    while True:
        note = input("Write note (or type exit:) ")
        if(note.lower()=="exit"):
            break
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("my_notes.txt", "a") as f:
            f.write(f"[{timestamp}] {user} : {note}\n")

    print("notes saved")


if __name__ == "__main__":
    print("Welcome to simple CLI Notepad")
    user = input("Enter your name: ")
    collect_note(user)