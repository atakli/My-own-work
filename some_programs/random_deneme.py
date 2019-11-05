while 1:
    import random
    i_1 = 0
    i_2 = 0
    i_0 = 0
    rang = int(input("Range kaç olsun? "))
    for i in range(rang):
        x = random.randint(0,2)
        if x == 0:
            i_0 += 1
        elif x == 1:
            i_1 += 1
        else:
            i_2 += 1
    sonuç = "0'ın oranı {}\n1'in oranı: {}\n2'nin oranı {}dır."
    print(sonuç.format(i_0/rang,i_1/rang,i_2/rang))
