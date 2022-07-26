salt = []
salt_water = []

i = 0

while i < 5:
    i = i + 1
    s = input(f'{i}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오:')

    if s == 'Done':
        break
    S = int(s[:s.find('%')])
    L = int(s[s.find(' ') + 1:s.find('g'):1])

    salt.append( S * L / 100)
    salt_water.append(L)

print('{:.1f}% {:.1f}g'.format(sum(salt)/sum(salt_water) * 100, sum(salt_water)))
