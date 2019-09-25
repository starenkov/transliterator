"""

Transliterator is the class consisting of only two methods: to transliterate language and vice versa

On the input we will have only three languages: russian, kazakh and uzbek.

"""

cyrillic_alphabet = {
    'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е',  # Small latin chars
    'f': 'ф', 'g': 'г', 'h': 'х', 'i': 'и', 'j': 'й',
    'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о',
    'p': 'п', 'q': 'қ', 'r': 'р', 's': 'с', 't': 'т',
    'u': 'у', 'v': 'в', 'y': 'ы', 'z': 'з', 'zh': 'ж',
    'yo': 'ё', 'ch': 'ч', 'sh': 'ш', 'sch': 'щ', 'yu': 'ю',
    'ya': 'я', 'а`': 'ә', 'o`': 'ө', 'g`': 'ғ', 'n`': 'ң',
    'u`': 'ү',

    'A': 'А', 'B': 'Б', 'C': 'Ц', 'D': 'Д', 'E': 'Е',  # Big latin chars
    'F': 'Ф', 'G': 'Ф', 'H': 'Х', 'I': 'И', 'J': 'Й',
    'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О',
    'P': 'П', 'Q': 'Қ', 'R': 'Р', 'S': 'C', 'T': 'Т',
    'U': 'У', 'V': 'В', 'Y': 'Ы', 'Z': 'З', 'Zh': 'Ж',
    'Yo': 'Ё', 'Ch': 'Ч', 'Sh': 'Ш', 'Sch': 'Щ', 'Ya': 'Я',
    'Yu': 'Ю', 'A`': 'Ә', 'О`': 'Ө', 'G`': 'F', 'N`': 'Ң',
    'U`': 'Ү', "'": 'ь', ',': ',', '-': '-', ' ': ' '
}

latin_alphabet = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
    'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k',
    'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
    'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ь': "'", 'ы': 'y', 'ъ': "'",
    'э': 'e', 'ю': 'yu', 'я': 'ya', 'ә': 'a`', 'ғ': 'g`', 'қ': 'q',
    'ң': 'n`', 'ө': 'o`', 'ұ': 'u', 'һ': 'h', 'ү': 'u`', 'і': 'i',
    'ў': 'o`', 'ҳ': 'h', ' ': ' ', ',': ',', '-': '-',

    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
    'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'J', 'К': 'К',
    'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'T': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C',
    'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'U`',
    'Я': 'Ya', 'Ў': 'O`', 'Ҳ': 'H', 'Қ': 'Q', 'Ұ': 'U', 'Ғ': 'G`',
    'Ө': 'O`', 'Ү': 'U`', 'І': 'I', 'Ң': 'N`', 'Ә': 'A`', 'Һ': 'H'
}


def convert_latin(text: str):
    # Method converts test to latin

    simple_text = ""

    for char in text:
        simple_text += latin_alphabet.get(char)

    return simple_text


def convert_cyrillic(text: str):
    # Method converts test to cyrillic
    simple_text = ""

    i = 0
    while i < len(text):
        # Cycle checks forward chars to combine into one char
        try:
            if i + 2 <= len(text) and (text[i] == 's' or text[i] == 'S') \
                    and cyrillic_alphabet.get(text[i] + text[i + 1] + text[i + 2]) is not None:
                simple_text += cyrillic_alphabet.get(text[i] + text[i + 1] + text[i + 2])
                i += 3
            elif i + 1 <= len(text) and cyrillic_alphabet.get(text[i] + text[i + 1]) is not None:
                simple_text += cyrillic_alphabet.get(text[i] + text[i + 1])
                i += 2
            else:
                simple_text += cyrillic_alphabet.get(text[i])
                i += 1
        except IndexError:
            simple_text += cyrillic_alphabet.get(text[i])
            i += 1

    return simple_text
