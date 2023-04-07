# autoskola-eTesty API

- I'am not owner of used website (https://www.autoskola-testy.cz/)
- API for getting random driving school exam questions (with answers and images/video if available)
- Script with examples -> [example.py](https://github.com/RxiPland/autoskola_eTesty_API/blob/main/example.py)

### Implementation:
```py
import autoskola_etesty as etesty

# integers must be between 1 and 7
etesty.get_random_question(question_topic_id: int)
"""
Output:
{'question_text': '"Chodec":', 'question_media': '', 'correct_text': 'Je i osoba, která se pohybuje na kolečkových bruslích nebo obdobném sportovním vybavení.', 'correct_media': '', 'wrong1_text': 'Není osoba, která se pohybuje na lyžích, kolečkových bruslích nebo obdobném sportovním vybavení.', 'wrong1_media': '', 'wrong2_text': 'Je výhradně kráčející osoba.', 'wrong2_media': '', 'question_id': '10060002', 'topic_id': 1, 'points': '2'}
"""

url = "https://www.autoskola-testy.cz/prohlizeni_otazek.php?otazka=336-tato_dopravni_znacka_upozornuje_na_misto_kde"
etesty.get_question(url: str)
"""
Output:
{'question_text': 'Tato dopravní značka:', 'question_media': 'https://www.autoskola-testy.cz/img/single/a19.jpg', 'correct_text': 'Upozorňuje na místo, kde cyklisté vjíždějí na vozovku nebo ji přejíždějí, anebo na úsek, kde se cyklisté často vyskytují.', 'correct_media': '', 'wrong1_text': 'Přikazuje cyklistům užít v daném směru takto označeného pruhu nebo stezky.', 'wrong1_media': '', 'wrong2_text': 'Zakazuje vjezd cyklistům a jízdu na jízdním kole. Vedení jízdního kola cyklistou je povoleno.', 'wrong2_media': '', 'question_id': '06050211', 'topic_id': 2, 'points': '1'}
"""

etesty.get_questions_urls(question_topic_id: int)
"""
Output:
[('06040213', 'https://www.autoskola-testy.cz/prohlizeni_otazek.php?otazka=811-zraneny_si_po_dopravni_nehode_stezuje_na_bolesti_bricha_a_pocit_zizne'), ('06050284', 'https://www.autoskola-testy.cz/prohlizeni_otazek.php?otazka=813-prvni_pomoc_je_povinen_poskytnout'), ('06060268', 'https://www.autoskola-testy.cz/prohlizeni_otazek.php?otazka=834-hrozi_trestni_postih_pokud_neposkytnete_prvni_pomoc'), ...
"""
```

<br></br>

## Question topic ID's:
1) Pravidla provozu na pozemních komunikacích
2) Dopravní značky
3) Zásady bezpečné jízdy
4) Dopravní situace
5) Předpisy o podmínkách provozu vozidel
6) Předpisy související s provozem
7) Zdravotnická příprava

<br></br>

## Example of returned dictionary/json:
```json
{
    "question_text": "Za touto dopravní značkou smíte jet rychlostí:",
    "question_media": "https://www.autoskola-testy.cz/img/single/0117.jpg",

    "correct_text": "Nejvýše 50 km/h, protože vjíždíte do obce.",
    "correct_media": "",

    "wrong1_text": "Nejvýše 60 km/h, protože vjíždíte do obce.",
    "wrong1_media": "",

    "wrong2_text": "Nejvýše 20 km/h, protože vjíždíte do obytné zóny.",
    "wrong2_media": "",

    "question_id": "06060304",
    "topic_id": 2,
    "points": "1"
}
```
<br></br>

# Question type examples:
### Text question and text answers
![image](https://user-images.githubusercontent.com/82058894/229222391-3b293da2-5160-42c9-acbe-6760db31ba75.png)
##
### Image question and text answers
![image](https://user-images.githubusercontent.com/82058894/229223445-d1571559-5314-4a6a-9c9c-972bdba6608f.png)
##
### Text question and image answers
![image](https://user-images.githubusercontent.com/82058894/229223171-c5835064-6c8d-4a3a-a5b2-b77edb00d647.png)
##
### Image question and image answers
![image](https://user-images.githubusercontent.com/82058894/230226675-3756f168-29ef-494b-8c28-43591cf6ecfd.png)
