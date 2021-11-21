def main():
    dict_list = [{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415},
                 {'name': 'inform', 'confidence': 0.9842240810394287},
                 {'name': 'inform', 'confidence': 0.9842240810394287}]

    # print(dict_list)

    answer = list(map(dict, set(tuple(sorted(sub.items())) for sub in dict_list)))
    print(answer)

if __name__ == '__main__':
    main()