

with open('text.txt', 'r') as rf:
    with open('text2.txt', 'w') as wf:
        for line in rf:
            wf.write(line)