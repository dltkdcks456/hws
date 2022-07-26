perc_gram = input("소금물의 농도(%)와 소금물의 양(g)을 입력하십시오:")
perc_gram = perc_gram.split('%')
perc_gram_n = []
for i in perc_gram:
    i = i.strip(' g')
    perc_gram_n.append(int(i))
print(perc_gram_n)