from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    pass

    """
    Verifica se exceção é lançada caso os parâmetros
    não possuam os tipos de dados corretos
    """

    with pytest.raises(TypeError):
        encrypt_message(12345, "12345")

    with pytest.raises(TypeError):
        encrypt_message("12345", "12345")

    """
    Verifica se retorna a mensagem invertida caso key não seja
    um índice positivo de message
    """

    assert encrypt_message("python", 9) == "nohtyp"

    """
    Verifica se inverte os caracteres de cada parte e
    retorna a união das partes com "_" entre elas
    """

    assert encrypt_message("python", 3) == "typ_noh"

    """
    Verifica se inverte a posição das partes, inverte os caracteres de cada
    parte, e retorna a união das partes com "_" entre elas
    """

    assert encrypt_message("python", 4) == "no_htyp"
