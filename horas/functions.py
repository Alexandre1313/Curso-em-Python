def convert(h1, m1, h2, m2, h3, m3, h4, m4):
    lis = h1, m1, h2, m2, h3, m3, h4, m4
    lis1 = []
    try:
        if lis[0] != '':
            h11 = int(lis[0])
            lis1.append(h11)
        else:
            return 'v1', -3, -3, -3, -3, -3, -3, -3
    except (ValueError, TypeError):
        return 'inv1', -3, -3, -3, -3, -3, -3, -3
    else:
        try:
            if lis[1] != '':
                m11 = int(lis[1])
                lis1.append(m11)
            else:
                return -3, 'v2', -3, -3, -3, -3, -3, -3
        except (ValueError, TypeError):
            return -3, 'inv2', -3, -3, -3, -3, -3, -3
        else:
            try:
                if lis[2] != '':
                    h22 = int(lis[2])
                    lis1.append(h22)
                else:
                    return -3, -3, 'v3', -3, -3, -3, -3, -3
            except (ValueError, TypeError):
                return -3, -3, 'inv3', -3, -3, -3, -3, -3
            else:
                try:
                    if lis[3] != '':
                        m22 = int(lis[3])
                        lis1.append(m22)
                    else:
                        return -3, -3, -3, 'v4', -3, -3, -3, -3
                except (ValueError, TypeError):
                    return -3, -3, -3, 'inv4', -3, -3, -3, -3
                else:
                    try:
                        if lis[4] != '':
                            h33 = int(lis[4])
                            lis1.append(h33)
                        else:
                            return -3, -3, -3, -3, 'v5', -3, -3, -3
                    except (ValueError, TypeError):
                        return -3, -3, -3, -3, 'inv5', -3, -3, -3
                    else:
                        try:
                            if lis[5] != '':
                                m33 = int(lis[5])
                                lis1.append(m33)
                            else:
                                return -3, -3, -3, -3, -3, 'v6', -3, -3
                        except (ValueError, TypeError):
                            return -3, -3, -3, -3, -3, 'inv6', -3, -3
                        else:
                            try:
                                if lis[6] != '':
                                    h44 = int(lis[6])
                                    lis1.append(h44)
                                else:
                                    return -3, -3, -3, -3, -3, -3, 'v7', -3
                            except (ValueError, TypeError):
                                return -3, -3, -3, -3, -3, -3, 'inv7', -3
                            else:
                                try:
                                    if lis[7] != '':
                                        m44 = int(lis[7])
                                        lis1.append(m44)
                                    else:
                                        return -3, -3, -3, -3, -3, -3, -3, 'v8'
                                except (ValueError, TypeError):
                                    return -3, -3, -3, -3, -3, -3, -3, 'inv8'
                                else:
                                    return lis1


def calc(h1, m1, h2, m2, ap=True):
    hor = [h1, m1, h2, m2]
    totm = 0
    if ap is True:
        hi = h2 - h1
        m = m2 - m1
        hm = hi * 60
        totm = hm + m
    return totm


g = calc(3, 32, 3, 4)
print(g)
