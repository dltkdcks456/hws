N = int(input())

num_list = list(map(int, input().split()))
max_num = max(num_list)

num_range = [num for num in range(2, max_num + 1)]
prime_number = [num for num in range(2, max_num + 1)]

for i in num_range:
    if i in prime_number:
        for j in prime_number:
            if j != i and j % i == 0:
                prime_number.remove(j)

cnt = 0
for k in num_list:
    if k in prime_number:
        cnt = cnt + 1

print(cnt)