from re import findall

text = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''


arr = list(map(lambda x: findall(r'[^\s!,.-?":;0-9]+', x),
               filter(lambda x: len(x.split(" ")) > 3, text.split("\n"))))

print(arr)