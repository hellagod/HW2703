from requests import get
from statistics import mean


def temp():
    g = get(
        'https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat').text.split(
        '\n')
    g.remove('')
    h = list(map(lambda item: float(item), g))
    print(max(h), min(h), mean(h))
    print(len(h), len(set(h)))


temp()
