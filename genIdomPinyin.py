import json

from getPinYin import get_pinyin



json_file = './data/dictionaries/idiom.json'
pinyin_idiom_json_f = './data/dictionaries/pinyin_idiom.json'


word_pinyin_dict = {}

if __name__ == "__main__":

    with open(json_file, 'r', encoding='utf-8') as f:  
        f_json = json.load(f)
        # print(f'{f_json = }')

        for it in f_json:
            word = it['word']
            pinyin = get_pinyin(word)

            word_pinyin_dict[word] = pinyin

            # word_pinyin_list.append([pinyin, word])
            # print(f'{word = }')
            # print(f'{pinyin = }')
            # print()

    # print(f'{word_pinyin_dict = }')

    with open(pinyin_idiom_json_f, 'w', encoding='utf-8') as f:
        json.dump(word_pinyin_dict, f, indent=4, ensure_ascii=False)
        print('Completed!')



