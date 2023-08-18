import pytest

def multiplicacao(x, y):
    return x*y

def teste_multiplicacao1():
    assert multiplicacao(10, 2) == 20

def teste_multiplicacao2():
    assert multiplicacao(9, 3) == 27

def teste_multiplicacao3():
    assert multiplicacao(10, 9) == 90


#                Executável        código python
# Rodar Python:  python3.10.exe    meus_testes.py
# Rodar Pytest:  pytest.exe        meus_testes.py