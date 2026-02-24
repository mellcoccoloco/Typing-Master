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

    random.shuffle(word_list)

    word_display = ft.Text(word_list[0], size=30, weight="bold")
    user_input = ft.TextField(label="Type the word here ✨")
    result_text = ft.Text("")

    def check_word(e):
        if user_input.value == word_display.value:
            result_text.value = "Correct (remember mell is the best) 💖"
        else:
            result_text.value = "Try again loseeerrr 😜"

        random.shuffle(word_list)
        word_display.value = word_list[0]
        user_input.value = ""
        page.update()

    check_button = ft.ElevatedButton("Check ✨", on_click=check_word)

    page.add(
        word_display,
        user_input,
        result_text,
        check_button
    )

ft.app(target=main)