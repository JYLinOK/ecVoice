import json

from getPinYin import get_pinyin



def computeScore(pinyin_L1, pinyin_L2, words1, words2, a=1, b=1, c=2, pp=1, pt=1, ppl=1, align=2):
    if len(pinyin_L1[0]) > len(pinyin_L2[0]):
        return None
    else:
        align_score = 0
        pinyin_score = 0
        pinyin_L_score = 0
        tone_score = 0

        # print(f'{words1 = }')
        # print(f'{words2 = }')

        if len(words1) >= len(words2):
            max_L1 = True
        else:
            max_L1 = False

        # print(f'{max_L1 = }')

        # align_score
        return_ok = True
        if max_L1:
            for word_i in range(len(words2)):
                if words1[word_i] == words2[word_i]:
                    align_score += a

            if align_score < int(len(words2) / align):
                return_ok = False
        else:
            for word_i in range(len(words1)):
                if words1[word_i] == words2[word_i]:
                    align_score += a

            if align_score < int(len(words1) / align):
                return_ok = False 

        # print(f'{return_ok = }')
        # print()

        # pinyin_score + tone_score
        if max_L1:
            for pinyin_i in range(len(pinyin_L2[0])):

                # print(f'{len(pinyin_L2[0][pinyin_i]) = }')
                # print(f'{len(pinyin_L2[0][pinyin_i]) = }')

                if pinyin_L2[0][pinyin_i] == pinyin_L1[0][pinyin_i]:
                    pinyin_L_score += c
                else:
                    pinyin_L_score -= c

                if len(pinyin_L2[0][pinyin_i]) <= len(pinyin_L1[0][pinyin_i]):
                    for char_i in range(len(pinyin_L2[0][pinyin_i])):
                        if pinyin_L1[0][pinyin_i][char_i] == pinyin_L2[0][pinyin_i][char_i]:
                            pinyin_score += b
                else:
                    for char_i in range(len(pinyin_L1[0][pinyin_i])):
                        if pinyin_L1[0][pinyin_i][char_i] == pinyin_L2[0][pinyin_i][char_i]:
                            pinyin_score += b

            for tone_i in range(len(pinyin_L2[1])):
                if pinyin_L1[1][tone_i].isdigit() and pinyin_L2[1][tone_i].isdigit():
                    tone_score += (int(pinyin_L1[1][tone_i]) - int(pinyin_L2[1][tone_i])) ** 2

        else:
            for pinyin_i in range(len(pinyin_L1[0])):
                if pinyin_L2[0][pinyin_i] == pinyin_L1[0][pinyin_i]:
                    pinyin_L_score += c
                else:
                    pinyin_L_score -= c

                if len(pinyin_L2[0][pinyin_i]) <= len(pinyin_L1[0][pinyin_i]):
                        for char_i in range(len(pinyin_L2[0][pinyin_i])):
                            if pinyin_L1[0][pinyin_i][char_i] == pinyin_L2[0][pinyin_i][char_i]:
                                pinyin_score += 1
                else:
                    for char_i in range(len(pinyin_L1[0][pinyin_i])):
                        if pinyin_L1[0][pinyin_i][char_i] == pinyin_L2[0][pinyin_i][char_i]:
                            pinyin_score += 1

                for tone_i in range(len(pinyin_L1[1])):
                    if pinyin_L1[1][tone_i].isdigit() and pinyin_L2[1][tone_i].isdigit():
                        tone_score += (int(pinyin_L1[1][tone_i]) - int(pinyin_L2[1][tone_i])) ** 2
        
        tone_score = tone_score / len(pinyin_L1[1])

        # Final score
        score = pinyin_score * pp - tone_score * pt + pinyin_L_score * ppl

        if return_ok:
            return score
        else: 
            return None



pinyin_idiom_f = './data/dictionaries/pinyin_idiom.json'


def compareWords(words, pinyin_idiom_f = pinyin_idiom_f):
    words_pinyin = get_pinyin(words)
    # print(f'{words_pinyin = }')

    max_score = 0
    closest_words = ''

    with open(pinyin_idiom_f, 'r', encoding='utf-8') as f:
        json_dict = json.load(f)
        # print(f'{type(json_dict) = }')

        for d_it in json_dict:
            d_it_pinyin = json_dict[d_it]
            # print(f'{d_it_pinyin = }')
            # print(f'{words_pinyin = }')
            score = computeScore(words_pinyin, d_it_pinyin, words, d_it)
            # print(f'{score = }')

            if score: 
                if max_score < score: 
                    max_score = score
                    closest_words = d_it
         
        # print(f'{max_score = }')
        # print(f'{closest_words = }')
        return closest_words, max_score



if __name__ == "__main__":
    idom = '与出三竿'
    print(f'{compareWords(idom) = }')


