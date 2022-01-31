def pascalize(str):
    temp = []
    if ' ' in str:
        temp = str.split()
    if '_' in str:
        temp = str.split('_')
    rst = ""
    for i in temp:
        rst += i.capitalize()
    return rst


def depascalize(str):
    pos = [i for i, e in enumerate(str + 'A') if e.isupper()]
    parts = [str[pos[j]:pos[j + 1]] for j in range(len(pos) - 1)]
    lst = ""
    for i in parts:
        lst += i.lower() + '_'
    return lst[:-1]


def camelize(str):
    lst = str[-1]
    str_t = str[:-1].replace('.', '')
    if str[:-1] == str_t:
        str_t += lst

    temp = []
    if ' ' in str_t:
        temp = str_t.split()
    elif '_' in str_t:
        temp = str_t.split('_')

    rst = ""

    for i in range(len(temp)):
        if i == 0:
            rst += temp[i].lower()
            continue
        rst += temp[i].capitalize()
    return rst


def snakecase(str):
    pos = [i for i, e in enumerate(str + 'A') if e.isupper()]
    parts = [str[pos[j]:pos[j + 1]] for j in range(len(pos) - 1)]
    rst = str[:pos[0]] + '_'
    for i in parts:
        rst += i.lower() + '_'
    return rst[:-1]


def is_pascalize(str):
    if ' ' in str or '_' in str or str[0] != str[0].upper():
        return False
    return True


def is_camelcase(str):
    if ' ' in str or '_' in str or str[0] != str[0].lower():
        return False
    return True


def is_snakecase(str):
    if ' ' in str or str != str.lower():
        return False
    return True
