
text="The quick brown fox jumps over a lazy dog"

alphabets="abcedfghijklmnopqrstuvwxyz"

text=text.casefold()

is_panagram=True

for ch in alphabets:

    if text.count(ch)==0:

        is_panagram=False

        break

print(is_panagram)




#print vowel_count



