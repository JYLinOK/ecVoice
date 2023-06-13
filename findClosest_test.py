import json
import time
import csv


from findClosest import compareWords, writeCSV
from processSentence import processSen

from data.test.data_1 import test_list_word_1, test_list_word_2, test_list_word_3, test_list_word_4, test_list_word_1_2, test_list_word_3_4
from data.test.data_1 import test_list_tone_1_2, test_list_tone_3_4
from data.test.data_2 import sentence_1


def test_word(test_list, word_error_index, group_n=3, t_round=3):
    T2 = time.time()
    r_list = []
    record_list = []
    correct = 0
    correct_word = test_list[0]
    for it_i in range(len(test_list)):
        word = test_list[it_i]
        w_r_i = compareWords(word)
        r_list.append(w_r_i[1])
        n = len(r_list)

        print(str(it_i+1) + ' ' + word + ': ', f'{w_r_i = }')

        # print(f'{w_r_i[0] = }')
        # print(f'{correct_word = }')

        if w_r_i[0] == correct_word:
            correct += 1

        # print(f'{correct = }')
        # print()


        if (it_i+1) % group_n == 0:
            if it_i < len(test_list)-1:
                correct_word = test_list[it_i+1]

            T1 = T2 
            T2 = time.time()
            t = T2-T1

            list_row = [w_r_i[0], word_error_index, group_n, correct, round(t, t_round), r_list[0], r_list[1], r_list[2], round(sum(r_list[1:])/(n-1), 1)] 
            record_list.append(list_row)
            r_list = []
            correct = 0

            print(f'{list_row = }')
            # # print(f'{t = }')
            # print(f'{round(t, t_round) = }')
            print()

    # print(f'{record_list = }')
    return record_list



def test_sentence(test_list):
    for it_i in range(len(test_list)):
        wild_sen = test_list[it_i][0]
        correct_sen = test_list[it_i][1]
        processed_sen = processSen(wild_sen)

        print(f'{wild_sen = }')
        print(f'{correct_sen = }')
        print(f'{processed_sen = }')

        print()






# Test the fourth charater of the idiom
if __name__ == "__main__":

    word_process = True
    word_process = False

    if word_process: 

        title_W_list = [
            ['word', 'word error', 'group_n', 'correct', 'time', 'r1', 'r2', 'r3', 'ra']
        ]

        title_T_list = [
            ['word', 'tone error', 'group_n', 'correct', 'time', 'r1', 'r2', 'r3', 'ra']
        ]

        # title_T_list = [
        #     ['word', 'word error', 'group_n', 'correct', 'time', 'r1', 'r2', 'r3', 'ra']
        # ]


        # test_list = test_list_word_4
        # test_list = test_list_word_3
        # test_list = test_list_word_2
        # test_list = test_list_word_1

        # test_list = test_list_word_1_2
        # test_list = test_list_word_3_4

        # test_list = test_list_tone_3_4
        test_list = test_list_tone_1_2


        word_error_index = [1, 2]

        # test_name = 'test_list_word_' + str(word_error_index)
        test_name = 'test_list_tone_' + str(word_error_index)


        test_L = test_word(test_list, word_error_index, group_n=3, t_round=3)
        # print(f'{test_L = }')

        # title_T_list = title_W_list + test_L

        title_T_list = title_T_list + test_L

        print(f'{title_T_list = }')

        writeCSV('./data/test/results/'+test_name+'.csv', title_T_list, encode='utf-8-sig')

    else:
        pass

        test_sentence(sentence_1)



