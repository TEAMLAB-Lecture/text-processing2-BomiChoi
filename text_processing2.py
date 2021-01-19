#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    digit_string = ''
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    li = []

    for i in input_string:
        if i.isdigit():
            li.append(numbers[int(i)])

    digit_string = ' '.join(li)
    return digit_string


"""
컴퓨터 프로그래밍에 많은 명명 규칙이 있지만, 두 규칙이 특히 흔히 쓰입니다. 
첫번째로는, 변수 이름을 'underscore'로 나눠준다거나, (ex. under_score_variable)
두번째로는, 변수 이름을 대소문자 구별해 구분자 (delimiter)없이 쓰는 경우가 있습니다. 
이 두번째의 경우에는 첫번째 단어는 소문자로, 그 후에 오는 단어들의 첫번째 글자들은 대문자로 쓰입니다 (ex. camelCaseVariable). 
"""


def to_camel_case(underscore_str):
    li = underscore_str.split('_')
    li_2 = []

    for l in li:
        if l != '':
            li_2.append(l)

    for i in range(len(li_2)):
        if i == 0:
            if li_2[i].isupper():
                li_2[i] = li_2[i].lower()
        else:
            li_2[i] = li_2[i].capitalize()

    camelcase_str = ''.join(li_2)
    return camelcase_str
