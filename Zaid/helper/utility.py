import datetime
import math
import random
import time
import uuid
from random import randint

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    return "" if not " ".join(split[1:]).strip() else " ".join(split[1:])

def split_list(input_list, n):
    n = max(1, n)
    return [input_list[i: i + n] for i in range(0, len(input_list), n)]


def human_time(*args, **kwargs):
    secs = float(datetime.timedelta(*args, **kwargs).total_seconds())
    units = [("day", 86400), ("hour", 3600), ("minute", 60), ("second", 1)]
    parts = []
    for unit, mul in units:
        if secs / mul >= 1 or mul == 1:
            if mul > 1:
                n = int(math.floor(secs / mul))
                secs -= n * mul
            else:
                n = secs if secs != int(secs) else int(secs)
            parts.append(f'{n} {unit}{"" if n == 1 else "s"}')
    return ", ".join(parts)


def random_interval():
    rand_value = randint(14400, 43200)
    delta = (time.time() + rand_value) - time.time()
    return int(delta)


def get_random_hex(chars=4):
    return uuid.uuid4().hex[:chars]


def get_mock_text(sentence):
    new_sentence = ""
    for number, letter in enumerate(sentence.lower()):
        if len(new_sentence) < 2:
            random_number = random.randint(
                0, 1
            )
            new_sentence += letter.upper() if random_number == 0 else letter
        elif (
                    new_sentence[number - 2].isupper()
                    and new_sentence[number - 1].isupper()
                    or new_sentence[number - 2].islower()
                    and new_sentence[number - 1].islower()
            ):
            new_sentence += (
                letter.lower()
                if new_sentence[number - 1].isupper()
                else letter.upper()
            )
        else:
            random_number = random.randint(0, 1)
            new_sentence += letter.upper() if random_number == 0 else letter
    return new_sentence
