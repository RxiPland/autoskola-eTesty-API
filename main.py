import time

import autoskola_etesty as etesty


for i in range(5):
    print(etesty.get_question())
    print()

    time.sleep(0.5)