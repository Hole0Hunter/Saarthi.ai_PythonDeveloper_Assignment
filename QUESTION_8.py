def main():
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'d': 400, 'e': 500, 'f': 600}

    dAns = dict()
    for key2 in d2:
        dAns[key2] = d2.get(key2) + d1.get(key2, 0)

    for key1 in d1:
        if not key1 in dAns:
            dAns[key1] = d1.get(key1)

    print(dAns)


if __name__ == '__main__':
    main()