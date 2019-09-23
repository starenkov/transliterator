from Trasnliterator import transliterator
import pytest

def test_latin():

    input_text = 'Что то с чем то'
    output_text = 'Chto to s chem to'

    assert transliterator.convertlatin(input_text) == output_text

def test_cyrillic():

    input_text = 'Kakoy to primer'
    output_text = 'Какоы то пример'

    assert transliterator.convertcyrillic(input_text) == output_text
