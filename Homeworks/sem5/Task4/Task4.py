# я правда пытался разобраться более углублено,
# чем то, что тут накодил, но даже дойдя до лекций
# по мехмату, где мужчина очень хорошо полчаса рассказывает,
# что и откуда берется, я всё равно не понял как это реализовать


def rle(text_of_sequence):
    text_of_sequence += ' '
    k = 0
    code_of_text = ''
    for i in range(len(text_of_sequence)-1):
        if text_of_sequence[i] == text_of_sequence[i+1]:
            k += 1
        else:
            if k == 0:
                code_of_text += text_of_sequence[i]
            else:
                code_of_text += str(k+1)+text_of_sequence[i]
                k = 0
    return code_of_text


def rle_de(code_of_text):
    decode_text = ''
    val = ''
    for i in range(len(code_of_text)):
        if code_of_text[i].isdigit():
            val += code_of_text[i]
        else:
            if val != '':
                decode_text += code_of_text[i]*int(val)
                val = ''
            else:
                decode_text += code_of_text[i]
    return decode_text


def codding():
    with open('posl.txt', 'r') as sequence:
        for i in sequence:
            text_of_sequence = i
    code_of_text = rle(text_of_sequence)
    with open('shifr.txt', 'w') as code:
        code.write(code_of_text)


def decodding():
    with open('shifr.txt', 'r') as code:
        for i in code:
            text_of_code = i
    decode_text = rle_de(text_of_code)
    with open('posl.txt', 'w') as sequence:
        sequence.write(decode_text)


# в зависимости от того что нужно, другое комитится
codding()
decodding()