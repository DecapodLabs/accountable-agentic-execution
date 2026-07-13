from app import farewell, greeting


def test_greeting() -> None:
    assert greeting("researcher") == "Hello, researcher!"


def test_farewell() -> None:
    assert farewell("researcher") == "Goodbye, researcher!"
