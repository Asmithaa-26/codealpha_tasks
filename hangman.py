import tkinter as tk
import random

# Word list with hints
WORDS = {
    "python": "A popular programming language 🐍",
    "banana": "A yellow fruit rich in potassium 🍌",
    "developer": "Someone who writes code 💻",
    "aesthetic": "Relating to beauty or design 🎨",
    "hangman": "This game you're playing 👻",
    "terminal": "Where you type commands 🖥️",
    "dynamic": "Opposite of static ⚡",
    "sunshine": "What brightens your day ☀️",
    "gravity": "What keeps you on the ground 🌍",
    "universe": "Everything that exists 🌌",
    "internet": "A global system of interconnected networks 🌐"
}

# Styling
BG_COLOR = "#f7f4ea"
BTN_COLOR = "#f2c94c"
BTN_TEXT = "#2d3436"
CORRECT_COLOR = "#55efc4"
WRONG_COLOR = "#ff7675"
TEXT_COLOR = "#2d3436"
FONT = ("Segoe UI", 14)
MAX_WRONG = 6

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎨 Aesthetic Hangman")
        self.root.geometry("620x700")
        self.root.configure(bg=BG_COLOR)

        self.word = ""
        self.hint_text = ""
        self.guessed = []
        self.wrong_guesses = 0

        self.setup_widgets()
        self.start_new_game()

    def setup_widgets(self):
        # Title
        tk.Label(self.root, text="🎨 HANGMAN", font=("Segoe UI", 24, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=20)

        # Canvas
        self.canvas = tk.Canvas(self.root, width=300, height=250, bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack()

        # Word display
        self.word_var = tk.StringVar()
        self.word_label = tk.Label(self.root, textvariable=self.word_var, font=("Segoe UI", 20), bg=BG_COLOR, fg=TEXT_COLOR)
        self.word_label.pack(pady=10)

        # Hint display
        self.hint_var = tk.StringVar(value="")
        self.hint_label = tk.Label(self.root, textvariable=self.hint_var, font=FONT, bg=BG_COLOR, fg="#636e72")
        self.hint_label.pack(pady=5)

        # Letter buttons
        self.buttons_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.buttons_frame.pack(pady=10)

        self.letter_buttons = {}
        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            btn = tk.Button(self.buttons_frame, text=letter, font=FONT, width=4, bg=BTN_COLOR, fg=BTN_TEXT,
                            command=lambda l=letter: self.check_letter(l.lower()))
            btn.grid(row=i // 9, column=i % 9, padx=3, pady=3)
            self.letter_buttons[letter.lower()] = btn

        # Control buttons (hint & retry)
        self.control_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.control_frame.pack(pady=10)

        self.hint_button = tk.Button(self.control_frame, text="💡 Hint", font=FONT, bg="#81ecec", fg=BTN_TEXT,
                                     command=self.show_hint)
        self.hint_button.grid(row=0, column=0, padx=10)

        self.retry_button = tk.Button(self.control_frame, text="🔁 Retry", font=FONT, bg="#fab1a0", fg=BTN_TEXT,
                                      command=self.start_new_game)
        self.retry_button.grid(row=0, column=1, padx=10)

        # Result message
        self.result_label = tk.Label(self.root, text="", font=("Segoe UI", 16, "bold"), bg=BG_COLOR)
        self.result_label.pack(pady=10)

    def draw_base(self):
        self.canvas.delete("all")
        self.canvas.create_line(50, 230, 250, 230, width=4)
        self.canvas.create_line(100, 230, 100, 30, width=4)
        self.canvas.create_line(100, 30, 200, 30, width=4)
        self.canvas.create_line(200, 30, 200, 60, width=4)

    def draw_hangman(self):
        parts = [
            lambda: self.canvas.create_oval(175, 60, 225, 110, width=3),               # Head
            lambda: self.canvas.create_line(200, 110, 200, 170, width=3),              # Body
            lambda: self.canvas.create_line(200, 120, 170, 150, width=3),              # Left Arm
            lambda: self.canvas.create_line(200, 120, 230, 150, width=3),              # Right Arm
            lambda: self.canvas.create_line(200, 170, 180, 210, width=3),              # Left Leg
            lambda: self.canvas.create_line(200, 170, 220, 210, width=3),              # Right Leg
        ]
        if self.wrong_guesses < len(parts):
            parts[self.wrong_guesses]()

    def update_word_display(self):
        display = ' '.join([ch if ch in self.guessed else '_' for ch in self.word])
        self.word_var.set(display)

    def check_letter(self, letter):
        self.letter_buttons[letter]['state'] = 'disabled'
        if letter in self.word:
            self.guessed.append(letter)
            self.update_word_display()
            if all(l in self.guessed for l in self.word):
                self.game_over(win=True)
        else:
            self.wrong_guesses += 1
            self.draw_hangman()
            if self.wrong_guesses >= MAX_WRONG:
                self.game_over(win=False)

    def show_hint(self):
        self.hint_var.set(f"Hint: {self.hint_text}")

    def game_over(self, win):
        for btn in self.letter_buttons.values():
            btn['state'] = 'disabled'
        result = f"🎉 You WON! The word was: {self.word.upper()}" if win else f"💀 You LOST! The word was: {self.word.upper()}"
        self.word_var.set(self.word.upper())
        self.result_label.config(text=result, fg=CORRECT_COLOR if win else WRONG_COLOR)

    def start_new_game(self):
        self.word, self.hint_text = random.choice(list(WORDS.items()))
        self.guessed = []
        self.wrong_guesses = 0
        self.update_word_display()
        self.draw_base()
        self.hint_var.set("")
        self.result_label.config(text="")

        for btn in self.letter_buttons.values():
            btn['state'] = 'normal'

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
