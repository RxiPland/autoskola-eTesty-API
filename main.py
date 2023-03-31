import time
import random

import autoskola_etesty as etesty


for i in range(5):
    print(etesty.get_question(random.randint(1, 7), random.randint(1, 7)))
    print()

    time.sleep(0.4)