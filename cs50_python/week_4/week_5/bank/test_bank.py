import bank


def test_starts_with_hello():
    assert bank.value("Hello") == 0
    assert bank.value("How") == 20
    assert bank.value("Sup") ==100
    assert bank.value("Good morning") == 100

