def rectangle(n):
    if n == 1:
        for i in range(pow(3, n)):
            for j in range(pow(3, n)):
                print('***' * pow(3, n))
                print('* *' * pow(3, n))
                print('***' * pow(3, n))
    else:
        rectangle(n-1)

rectangle(3)