import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import copy
import json
import re
import string

mapping = {
    1: 'upside down V',
    2: 'sideways T (line right)',
    3: 'blackslash 3 dots',
    4: 'upside down T',
    5: 'Skinny sideways triangle',
    6: 'backslash 2 dots + line',
    7: 'lambda',
    8: 'skinny V',
    9: 'backwards lambda',
    10: 'backwards C',
    11: 'backwards Z',
    12: 'backwards Y no middle dot',
    13: 'backwards N',
    14: 'sidways T line to left',
    15: 'forwardslash 3 dots',
    20: 'upper left corner',
    16: 'backwards y middle dot',
    17: 'triangle dot at top',
    18: 'V',
    19: '7',
    '': 'space'
}

message = [1, 2, 3, '',
           4, 5, 6, 2, 6, 7, '',
           8, 2, 9, 10, '',
           5, '',
           7, 11, 12, 13, 10, '',
           8, 13, 6, '',
           14, 1, 20, 6, 15, '',
           12, 16, 13, 15, 10, '',
           13, 2, '',
           17, 7, 4, 1, '',
           5, 8, '',
           13, 6, 8, 4, 3, 13, '',
           16, 13, 14, '',
           18, 1, 10, 7, '',
           15, 6, 8, 10, 20, '',
           8, 17, 3, 13, 4, 19]
f = open('dictionary.json')
d = json.load(f)
f.close()

newwords = ['AESTHER', 'INOX']
for word in newwords:
    d[word] = 'lorem ipsum'

oed = d.keys()

twoletterwords = []
twoletterwords_onlyai = []
threeletterwords = []
fourletterwords = []
fiveletterwords = []
sixletterwords = []
for word in oed:
    if word.find("-") != -1:
        # if there is a dash in the word throw it out it's some prefix or something
        pass
    elif len(word) == 2:
        if word[0].lower() in ['a', 'i']:
            twoletterwords_onlyai.append(word)
        else:
            twoletterwords.append(word)
    elif len(word) == 3:
        threeletterwords.append(word)
    elif len(word) == 4:
        fourletterwords.append(word)
    elif len(word) == 5:
        fiveletterwords.append(word)
    elif len(word) == 6:
        sixletterwords.append(word)

regex_base = "([" + string.ascii_uppercase + "])"

combinations = []

# for twoletterword_onlyai in twoletterwords_onlyai:
#     for threeletterword in threeletterwords:
#         if twoletterword_onlyai[1] == threeletterword[0] and threeletterword[1] != threeletterword[2]:
#             for sixletterword in sixletterwords:
#                 if re.match("." + twoletterword_onlyai[0] + threeletterword[2] + "."  + threeletterword[2] + ".",
#                             sixletterword) is not None:
#                     for twoletterword in twoletterwords:
#                         if twoletterword == threeletterword[1] + sixletterword[3]:
#                             combinations.append([twoletterword_onlyai, threeletterword, sixletterword, twoletterword])

for word_11 in twoletterwords_onlyai:
    # update regex to exclude already selected letters
    regex_level1 = regex_base
    for letter in word_11:
        regex_level1 = regex_level1.replace(letter, "")
    for word_6 in threeletterwords:
        if word_11[1] == word_6[0] and word_6[1] != word_6[2]:
            # update regex to exclude already selected letters
            regex_level2 = regex_level1
            for letter in word_6:
                regex_level2 = regex_level2.replace(letter, "")
            for word_9 in twoletterwords:
                if re.match(word_6[1] + regex_level2, word_9) is not None:
                    regex_level3 = regex_level2
                    for letter in word_9:
                        regex_level3 = regex_level3.replace(letter, "")
                    for word_3 in fourletterwords:
                        if re.match(word_6[0] + word_9[1] + regex_level3 + regex_level3, word_3) is not None and \
                                word_3[2] != word_3[3]:
                            regex_level4 = regex_level3
                            for letter in word_3:
                                regex_level4 = regex_level4.replace(letter, "")
                            for word_15 in fiveletterwords:
                                if re.match(regex_level4 + word_6[2] + word_6[0] + word_3[3] + regex_level4, word_15) \
                                        is not None and word_15[0] != word_15[4]:
                                    regex_level5 = regex_level4
                                    for letter in word_15:
                                        regex_level5 = regex_level5.replace(letter, "")
                                    for word_8 in fiveletterwords:
                                        if re.match(regex_level5 + regex_level5 + word_6[1] + word_15[0] + word_3[3],
                                                    word_8) is not None and word_8[0] != word_8[1]:
                                            regex_level6 = regex_level5
                                            for letter in word_8:
                                                regex_level6 = regex_level6.replace(letter, "")
                                            for word_13 in threeletterwords:
                                                if re.match(word_8[1] + word_6[1] + regex_level6, word_13) \
                                                        is not None:
                                                    regex_level7 = regex_level6
                                                    for letter in word_13:
                                                        regex_level7 = regex_level7.replace(letter, "")
                                                    for word_7 in fiveletterwords:
                                                        if re.match(word_13[2] + regex_level7 + word_15[4] + word_6[2] + word_8[3], word_7
                                                                    ) is not None:
                                                            regex_level8 = regex_level7
                                                            for letter in word_7:
                                                                regex_level8 = regex_level8.replace(letter, "")
                                                            for word_1 in threeletterwords:
                                                                if re.match(word_7[1] + word_9[1] + regex_level8, word_1) is not None:
                                                                    combinations.append([word_11, word_6, word_9, word_3, word_15, word_8, word_13, word_7, word_1])


print(len(combinations))
print(combinations)
message_desc = []
for char in message:
    message_desc.append(mapping[char])
message_desc = pd.Series(message_desc)

message_series = pd.Series(message)

counts = message_series.value_counts()

idea = {
    'upside down V': None,
    'sideways T (line right)': 'F',
    'blackslash 3 dots': None,
    'upside down T': None,
    'Skinny sideways triangle': 'A',
    'backslash 2 dots + line': 'N',
    'lambda': None,
    'skinny V': 'T',
    'backwards lambda': None,
    'backwards C': None,
    'backwards Z': None,
    'backwards Y no middle dot': None,
    'backwards N': 'O',
    'sidways T line to left': None,
    'forwardslash 3 dots': None,
    'upper left corner': None,
    'backwards y middle dot': None,
    'triangle dot at top': None,
    'V': None,
    '7': None,
    'space': ' '
}


message_copy = copy.deepcopy(message)
for i in range(len(message_copy)):
    if idea[mapping[message_copy[i]]] is not None:
        message_copy[i] = idea[mapping[message_copy[i]]]
    else:
        message_copy[i] = str(message_copy[i])

#print('.'.join(message_copy))

# sns.set(style='darkgrid')
# chart = sns.countplot(message_desc[message_desc != 'space'],
#                       order=message_desc[message_desc != 'space'].value_counts().index)
# chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
# chart.set(title='Overall Letter Counts')
# plt.show()
# 
# spaces = message_desc == 'space'
# endchars = message_desc.shift(1)[spaces].append(pd.Series(message_desc.iloc[-1]))
# startchars = message_desc.shift(-1)[spaces].append(pd.Series(message_desc.iloc[0]))
# 
# chart = sns.countplot(endchars,
#                       order=endchars.value_counts().index)
# chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
# chart.set(title='Final Letter Counts')
# plt.show()
# 
# chart = sns.countplot(startchars,
#                       order=startchars.value_counts().index)
# chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
# chart.set(title='Initial Letter Counts')
# plt.show()

