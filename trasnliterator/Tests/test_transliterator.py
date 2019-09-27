from trasnliterator import transliterator
import pytest

def test_latin():

    input_text = 'Серқуёш хур ўлкам, элга бахт, нажот! Сен ўзинг дўстларга йўлдош, меҳрибон!'
    output_text = 'Serquyosh hur o`lkam, elga baht, nazhot! Sen o`zing do`stlarga jo`ldosh, mehribon!'

    assert transliterator.convert_to_latin(input_text) == output_text

def test_cyrillic():

    input_text = 'Serquyosh hur oʻlkam, elga baxt, najot! Sen oʻzing doʻstlarga yoʻldosh, mehribon!'
    output_text = 'Cерқуёш хур оʻлкам, елга баxт, найот! Cен оʻзинг доʻстларга ёʻлдош, мехрибон!'

    assert transliterator.convert_to_cyrillic(input_text) == output_text
