def top_k_words(text, k):
    text = text.lower()
    words = text.split()
    dct = {}
    
    for i in words:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] += 1

    answer_dop = []

    for i in dct:
        answer_dop.append((dct[i], i))

    answer_dop = sorted(answer_dop, reverse=True)
    answer = []

    for i in range(k):
        answer.append((answer_dop[i][1], answer_dop[i][0]))

    return answer