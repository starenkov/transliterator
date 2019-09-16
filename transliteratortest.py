import pytest
import transliterator

def test_transliterator_latin():
    text = 'Что то с чем то'
    assert transliterator.Trasnliterator.convertlatin(text) == 'Chto to s chem to'

def test_transliterator_cyrilic():
    text = 'Kakoy to primer'
    assert transliterator.Trasnliterator.convertcyrilic(text) == 'Какоы то пример'
