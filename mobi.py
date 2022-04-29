from requests import get


def mobi():
    g = get(
        'https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt').text
    g = g.lower().translate(str.maketrans({',': '', '.': '', ';': ''})).replace(' ', '\n')
    f = open('moby_clean.txt', 'w')
    f.write(g)
    f.close()


mobi()
