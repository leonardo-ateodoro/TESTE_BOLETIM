import pytest
from boletim.calculos import calcular_media 

def test_inteiros():
    assert calcular_media ([8,10]) == 9.0