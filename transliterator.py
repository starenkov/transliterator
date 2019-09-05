"""

Transliterator is the class consisting of only two methods: to translite language and to return translisterated text
back

On the input we will have only three languages: russian, kazakh and uzbek.


"""
class Trasnliterator:

    alcyrilic = {
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
                      'Yu': 'Ю', 'A`': 'Ә', 'О`': 'Ө', 'G`': 'F',  'N`': 'Ң',
                      'U`': 'Ү', "'": 'ь', ',': ',', '-': '-', ' ': ' '
                     }

    allatin = {
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
                     'Л': 'L', 'М': 'M',  'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
                     'С': 'S', 'T': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C',
                     'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'U`',
                     'Я': 'Ya', 'Ў': 'O`', 'Ҳ': 'H', 'Қ': 'Q', 'Ұ': 'U', 'Ғ': 'G`',
                     'Ө': 'O`', 'Ү': 'U`', 'І': 'I', 'Ң': 'N`', 'Ә': 'A`', 'Һ': 'H'
                     }

    def convertlatin(text: str):

        simple_text = ""

        for char in text:
            simple_text += Trasnliterator.allatin.get(char)

        return simple_text

    def convertcyrilic(text: str):

        simple_text = ""

        for i in range(len(text)):

            if (text[i] == 's' or text[i] == 'S') and i+2 <= len(text):
                if Trasnliterator.alcyrilic.get(text[i] + text[i + 1] + text[i + 2]) is not None:
                    simple_text += Trasnliterator.alcyrilic.get(text[i] + text[i + 1] + text[i + 2])
                    i += 2
                elif Trasnliterator.alcyrilic.get(text[i] + text[i + 1]) is not None and i+1 <= text(len):
                    simple_text += Trasnliterator.alcyrilic.get(text[i] + text[i + 1])
            else:
                simple_text += Trasnliterator.alcyrilic.get(text[i])

        return simple_text

print(Trasnliterator.convertcyrilic('Suka'))

# def convert_latin(text: str):
#     simple_text = ""
#
#     for char in text:
#         if char == 'ё':
#             simple_text += chr(121) + chr(111)
#         elif char == 'Ё':
#             simple_text += chr(89) + chr(111)
#         elif char == 'ж':
#             simple_text += chr(122) + chr(104)
#         elif char == 'Ж':
#             simple_text += chr(90) + chr(104)
#         elif char == 'ч':
#             simple_text += chr(99) + chr(104)
#         elif char == 'Ч':
#             simple_text += chr(67) + chr(104)
#         elif char == 'ш':
#             simple_text += chr(115) + chr(104)
#         elif char == 'Ш':
#             simple_text += chr(83) + chr(104)
#         elif char == 'щ':
#             simple_text += chr(115) + chr(99) + chr(104)
#         elif char == 'Щ':
#             simple_text += chr(83) + chr(99) + chr(104)
#         elif char == 'ю':
#             simple_text += chr(121) + chr(117)
#         elif char == 'Ю':
#             simple_text += chr(89) + chr(117)
#         elif char == 'я':
#             simple_text += chr(121) + chr(97)
#         elif char == 'Я':
#             simple_text += chr(89) + chr(97)
#         elif char == 'ә':
#             simple_text += chr(97) + chr(96)
#         elif char == 'Ә':
#             simple_text += chr(65) + chr(96)
#         elif char == 'ғ':
#             simple_text += chr(103) + chr(96)
#         elif char == 'Ғ':
#             simple_text += chr(71) + chr(96)
#         elif char == 'ң':
#             simple_text += chr(100) + chr(96)
#         elif char == 'Ң':
#             simple_text += chr(78) + chr(96)
#         elif char == 'ө' or char == 'ў':
#             simple_text += chr(111) + chr(96)
#         elif char == 'Ө' or char == 'Ў':
#             simple_text += chr(79) + chr(96)
#         elif char == 'ү':
#             simple_text += chr(117) + chr(96)
#         elif char == 'Ү':
#             simple_text += chr(85) + chr(96)
#         else:
#             simple_text += chr(alphabet_cyrilic[char])
#
#     return simple_text


