def greeting(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('bonjour')
    else:
        print('Hello')

# return


def greeting_r(lang):
    value = ''
    if lang == 'es':
        value = 'Hola'
    elif lang == 'fr':
        value = 'bonjour'
    else:
        value = 'Hello'
    return value


# test = greeting('Ilhan')

test = greeting_r('Ilhan')

soyle = greeting_r('fr')


# multiple parameters

def dortgen_alan(kisa_k, uzun_k):
    alan = kisa_k * uzun_k
    return alan


dortgen_alan(6, 8)