from bs4 import BeautifulSoup
import requests


def translate_to_morse(txt):
    morse_text = []
    for letter in list(txt.upper()):
        if letter == " ":
            continue
        else:
            morse_text.append(eng_to_morse[letter])
    morse_text = " ".join(morse_text)
    return morse_text


def translate_to_english(txt):

    english_text = []
    for letter in txt.upper().split(" "):
        if letter == " ":
            continue
        else:
            english_text.append(morse_to_eng[letter])
    english_text = " ".join(english_text)
    return english_text


response = requests.get("https://morsecode.world/international/morse2.html")
data = response.text

soup = BeautifulSoup(data, "html.parser")
english = soup.select(".morse")
morse = soup.select("tr td")

english_list = [word.text for word in english]
english_list = english_list[:36]

morse_list = [word.text for word in morse]
morse_list = morse_list[1:72:2]

eng_to_morse = {}
for n in range(len(english_list)):
    eng_to_morse[english_list[n]] = morse_list[n]

morse_to_eng = {}
for n in range(len(english_list)):
    morse_to_eng[morse_list[n]] = english_list[n]


is_on = True
print("Welcome to Morse Code Translator.\nHere you can translate text (and numbers!) from English to Morse Code"
      "and vice versa.")
while is_on:
    dict_choice = input("\nTo translate text from English to Morse Code type 'M'."
                        "\nTo translate from Morse to English type 'E': ")
    if dict_choice.upper() == "M":
        text = input("Type your text: ")
        result = translate_to_morse(text)
    elif dict_choice.upper() == "E":
        text = input("Type your text: ")
        result = translate_to_english(text)
    else:
        print("Please, try again.")
        break

    choice = input(f"Here you go!\n{result}\nWant to try again? Type 'Yes': ")
    if choice.title() != "Yes":
        print("Bye-bye!")
        is_on = False
