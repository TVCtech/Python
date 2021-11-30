import re

text = 'hello, world'
m = re.search(r'\b(h.)(..o)\b', text)
if m:
    print("Full match: {}".format(m.group(0))) # hello
    print("First part: {}".format(m.group(1))) # he
    print("Last part: {}".format(m.group(2))) # llo