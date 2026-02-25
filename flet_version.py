import flet as ft
import random

word_list = [
    "princess",
    "glitter",
    "sparkle",
    "bestie",
    "pink",
    "slay",
    "iconic",
    "queen",
    "fabulous",
    "dreamy"
]

def main(page: ft.Page):
    page.title = "Typing Master"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    words = word_list.copy()
    random.shuffle(words)

    current_index = 0
    score = 0

    word_display = ft.Text(words[current_index], size=30, weight="bold")
    user_input = ft.TextField(label="Type the word here ✨")
    result_text = ft.Text("")

    score_text = ft.Text("Score: 0", size=20)
    score = 0

    def check_word(e):
        nonlocal score, current_index

        if user_input.value == words[current_index]:
            score += 1
            result_text.value = "Correct (remember mell is the best) 💖"
        else:
            result_text.value = "Try again loseeerrr 😜"

        current_index += 1

        if current_index >= len(words):
            accuracy = (score / len(words)) * 100
            word_display.value = "Game Over 🎀"
            result_text.value = f"Accuracy: {accuracy:.0f}%"
            check_button.disabled = True
        else:
            word_display.value = words[current_index]

        user_input.value = ""
        score_text.value = f"Score: {score}"
        page.update()

    check_button = ft.ElevatedButton("Check ✨", on_click=check_word)

    def restart_game(e):
        nonlocal score, current_index, words

        score = 0
        current_index = 0
        words = word_list.copy()
        random.shuffle(words)

        word_display.value = words[current_index]
        user_input.value = ""
        result_text.value = ""
        score_text.value = "Score: 0"
        check_button.disabled = False

        page.update()

    restart_button = ft.ElevatedButton("Restart 💕", on_click=restart_game)

    page.add(
        word_display,
        user_input,
        result_text,
        score_text,
        check_button,
        restart_button
    )
<<<<<<< HEAD

ft.app(target=main)
=======
ft.app(target=main)
>>>>>>> 22fea2c (fixed code)
