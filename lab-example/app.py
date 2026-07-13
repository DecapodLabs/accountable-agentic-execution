"""Tiny fake application used by the contained proof fixture."""


def greeting(name: str) -> str:
    return f"Hello, {name}!"


def farewell(name: str) -> str:
    return f"Goodbye, {name}!"
