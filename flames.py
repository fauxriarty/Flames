def flames(name1, name2):
    # removing the common characters:
    s1 = ''.join(i for i in name1 if i not in name2)
    s2 = ''.join(i for i in name2 if i not in name1)
    n = len(s1) + len(s2)

    s = ['Friends', 'Lovers', 'Acquaintances', 'Marriage', 'Enemies', 'Siblings']

    while len(s) > 1:
        if n % len(s) != 0:
            t = n % len(s)
            if t > len(s):
                t = t % len(s) - 1
            else:
                t = t - 1
        else:
            t = len(s) - 1
        s.remove(s[t])
    return s[0]
