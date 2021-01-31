def sequenciar(h=0, k=0):
    if h - k <= 991:
        if h > k:
            n = h
            print(f'{n}')
            n -= 1
            if n < k:
                return
            sequenciar(n, k)
        else:
            n = h
            print(f'{n}')
            n += 1
            if n > k:
                return
            sequenciar(n, k)


sequenciar(560, -500)
