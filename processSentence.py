from findClosest import compareWords


def processSen(sentence, show_p=False, align=1, n=4, s=10):
    tmp_sentence = sentence
    for char_i in range(len(sentence)-n+1):
        n_char_seg = sentence[char_i:char_i+n]

        pure_words = True
        for char in n_char_seg:
            if char in ['，', '。', ',', '.']:
                pure_words = False

        if pure_words:
            closest_words = compareWords(n_char_seg)

            if show_p:
                print(f'{n_char_seg = }')
                print(f'{closest_words = }')
                print()

            if closest_words[0] != '':
                score = closest_words[1]
                if score > s:
                    tmp_sentence = tmp_sentence[:char_i] + closest_words[0] + tmp_sentence[char_i+n:]
                    # print(f'{tmp_sentence = }')

    return tmp_sentence



if __name__ == "__main__":
    # sentence = '这是实验测试，包含一个“别出心才”的句子。'
    sentence = '真是青果预览，包含一个“别出心才”的句子。'
    print(f'\n{processSen(sentence, show_p=True) = }')
















