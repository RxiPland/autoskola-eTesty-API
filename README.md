# autoskola-eTesty API

- I'am not owner of used website (https://www.autoskola-testy.cz/)
- API for getting random driving school exam questions (with answers and images/video if available)
- Script with examples -> [example.py](https://github.com/RxiPland/autoskola_eTesty_API/blob/main/example.py)

### Implementation:
```py
import autoskola_etesty as etesty

# integers must be between 1 and 7
etesty.get_question(question_topic_id = int, previous_topic_id = int)
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
	"question_text": "Řidič motorového vozidla z výhledu v dopravní situaci:",
	"question_media": "https://www.autoskola-testy.cz/img/single/219004.mp4",
	
	"correct_text": "mohl odbočit vpravo, přičemž nesměl ohrozit a omezit vozidla jedoucí ve vyhrazeném jízdním pruhu.",
	"correct_media": "",
	
	"wrong1_text": "porušil pravidla silničního provozu tím, že odbočil přes vyhrazený jízdní pruh.",
	"wrong1_media": "",
	
	"wrong2_text": "mohl odbočit vpravo bez ohledu na vozidla jedoucí ve vyhrazeném jízdním pruhu, která nesměla ohrozit a omezit vozidla odbočující z průběžného pruhu.",
	"wrong2_media": "",
	
	"question_id": "22020002",
	"points": "4"
}
```

## Question type examples:
![image](https://user-images.githubusercontent.com/82058894/229222391-3b293da2-5160-42c9-acbe-6760db31ba75.png)
##
![image](https://user-images.githubusercontent.com/82058894/229223171-c5835064-6c8d-4a3a-a5b2-b77edb00d647.png)
##
![image](https://user-images.githubusercontent.com/82058894/229223445-d1571559-5314-4a6a-9c9c-972bdba6608f.png)
