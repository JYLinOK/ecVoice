from pypinyin import pinyin, lazy_pinyin, Style



def get_pinyin(hanzi):
    result = []
    word_L= []
    pinyin_L = []
    for it in pinyin(hanzi, style=Style.TONE3, heteronym=False, strict=True):
        if it[0] not in ['de', 'zi', 'le', 'bo']:
            word_L.append(it[0][:-1])
            pinyin_L.append(it[0][-1])
        else:
            word_L.append(it[0])
            pinyin_L.append('0')
    
    result.append([word_L, pinyin_L])
    return result[0]



if __name__ == "__main__":
    print(f"{get_pinyin('拼音') = }")
    print(f"{get_pinyin('日出弎竿') = }")





