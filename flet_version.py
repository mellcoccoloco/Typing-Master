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

    page.add(
        word_display,
        user_input,
        result_text
    )

ft.app(target=main)