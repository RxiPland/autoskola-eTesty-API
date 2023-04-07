import random

import autoskola_etesty as etesty


# Pravidla provozu na pozemních komunikacích (question_topic_id = 1)
print(etesty.get_random_question(question_topic_id=1))
print()

# Dopravní značky (question_topic_id = 2)
print(etesty.get_random_question(question_topic_id=2))
print()

# Zásady bezpečné jízdy (question_topic_id = 3)
print(etesty.get_random_question(question_topic_id=3))
print()

# Dopravní situace (question_topic_id = 4)
print(etesty.get_random_question(question_topic_id=4))
print()

# Předpisy o podmínkách provozu vozidel (question_topic_id = 5)
print(etesty.get_random_question(question_topic_id=5))
print()

# Předpisy související s provozem (question_topic_id = 6)
print(etesty.get_random_question(question_topic_id=6))
print()

# Zdravotnická příprava (question_topic_id = 7)
print(etesty.get_random_question(question_topic_id=7))
print()

# All questions urls
print(etesty.get_questions_urls(question_topic_id=7))
print()