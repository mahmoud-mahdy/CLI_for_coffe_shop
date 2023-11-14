sentence = "Hey fellow warriors"

new_sentence = ""
sentence = sentence.split()
for i in sentence:
    if len(i) < 4:
        new_sentence += i + " "
    elif len(i) > 4:
        new_sentence += i[::-1] + " "
print(new_sentence)