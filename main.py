import requests
import random
import re
from pprint import pprint

URL = "https://www.autoskola-testy.cz/prohlizeni_otazek.php?random="
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"


PATTERN_QUESTION_TEXT = r"\"question-text\".+>(.+)\n*\t*<\/p>"
PATTERN_QUESTION_MEDIA = r"src=\"(\/img\/[a-zA-z0-9\/]+.[a-zA-Z0-9]+)"

PATTERN_CORRECT = r"\"answer otazka_spravne\".+\n*\t*.+<p>(.+)<\/p>"
PATTERN_WRONG = r"\"answer otazka_spatne\".+\n*\t*.+<p>(.+)<\/p>"


def get_question(current_id: int, previous_id: int) -> dict:

    question_text = str()
    question_media = str()
    correct_text = str()
    correct_media = str()
    wrong1_text = str()
    wrong1_media = str()
    wrong2_text = str()
    wrong2_media = str()

    response = requests.get(URL + str(current_id), headers={"User-Agent": USER_AGENT, "Referer": URL + str(previous_id)})
    response_text = response.text

    if "/img/single" in response_text:

        # QUESTION TEXT
        question_text: list[str] = re.findall(PATTERN_QUESTION_TEXT, response_text)

        if len(question_text) > 0:
            question_text = question_text[0].strip()
        else:
            question_text = str()
        
        # QUESTION MEDIA
        question_media: list[str] = re.findall(PATTERN_QUESTION_MEDIA, response_text)

        if len(question_media) > 0:
            question_media = question_media[0].strip()
        else:
            question_media = str()

        # CORRECT ANSWER
        correct_text: list[str] = re.findall(PATTERN_CORRECT, response_text)

        if len(correct_text) > 0:
            correct_text = correct_text[0].strip()
        else:
            correct_text = str()

        # WRONG ANSWER #1
        wrong1_text: list[str] = re.findall(PATTERN_WRONG, response_text)

        if len(wrong1_text) > 0:
            wrong1_text = wrong1_text[0].strip()
        else:
            wrong1_text = str()

        # WRONG ANSWER #2
        wrong2_text: list[str] = re.findall(PATTERN_WRONG, response_text)

        if len(wrong2_text) > 1:
            wrong2_text = wrong2_text[1].strip()
        else:
            wrong2_text = str()


    elif "/img/tripple/" in response_text:

        # QUESTION TEXT
        question_text: list[str] = re.findall(PATTERN_QUESTION_TEXT, response_text)

        if len(question_text) > 0:
            question_text = question_text[0].strip()
        else:
            question_text = str()

        # CORRECT ANSWER MEDIA
        correct_media: list[str] = re.findall(PATTERN_CORRECT, response_text)

        if len(correct_media) > 0:
            correct_media: str = correct_media[0].strip()
            correct_media = correct_media.lstrip("<img src=\"")
            correct_media = correct_media.rstrip("\">")

        else:
            correct_media = str()

        # WRONG ANSWER MEDIA #1
        wrong1_media: list[str] = re.findall(PATTERN_WRONG, response_text)

        if len(wrong1_media) > 0:
            wrong1_media: str = wrong1_media[0].strip()
            wrong1_media = wrong1_media.lstrip("<img src=\"")
            wrong1_media = wrong1_media.rstrip("\">")

        else:
            wrong1_media = str()

        # WRONG ANSWER MEDIA #2
        wrong2_media: list[str] = re.findall(PATTERN_WRONG, response_text)

        if len(wrong2_media) > 1:
            wrong2_media: str = wrong2_media[1].strip()
            wrong2_media = wrong2_media.lstrip("<img src=\"")
            wrong2_media = wrong2_media.rstrip("\">")

        else:
            wrong2_media = str()

    else:

        # QUESTION TEXT
        question_text: list[str] = re.findall(PATTERN_QUESTION_TEXT, response_text)

        if len(question_text) > 0:
            question_text = question_text[0].strip()
        else:
            question_text = str()

        # CORRECT ANSWER TEXT
        correct_text: list[str] = re.findall(PATTERN_CORRECT, response_text)

        if len(correct_text) > 0:
            correct_text = correct_text[0].strip()
        else:
            correct_text = str()

        # WRONG ANSWER TEXT #1
        wrong1_text: list[str] = re.findall(PATTERN_WRONG, response_text)

        if len(wrong1_text) > 0:
            wrong1_text = wrong1_text[0].strip()
        else:
            wrong1_text = str()

        # WRONG ANSWER TEXT #2
        wrong2_text: list[str] = re.findall(PATTERN_WRONG, response_text)

        if len(wrong2_text) > 1:
            wrong2_text = wrong2_text[1].strip()
        else:
            wrong2_text = str()


    return {
        "question_text": question_text,
        "question_media": question_media,

        "correct_text": correct_text,
        "correct_media": correct_media,

        "wrong1_text": wrong1_text,
        "wrong1_media": wrong1_media,

        "wrong2_text": wrong2_text,
        "wrong2_media": wrong2_media
    }

current_id = random.randint(1, 7)
previous_id = random.randint(1, 7)

while input() == "":
    
    pprint(get_question(current_id, previous_id))
    print()

    previous_id = current_id
    current_id = random.randint(1, 7)