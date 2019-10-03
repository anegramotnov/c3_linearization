import pytest


c3 = lambda d, o: []


dependencies = {
    "O": [],
    "A": ["O"],
    "B": ["O"],
    "C": ["O"],
    "D": ["O"],
    "E": ["O"],
    "K1": ["A", "B", "C"],
    "K2": ["D", "B", "E"],
    "K3": ["D", "A"],
    "Z": ["K1", "K2", "K3"],
}


mro_pairs = [
    ("O", ["O"]),
    ("A", ["A", "O"]),
    ("B", ["B", "O"]),
    ("C", ["C", "O"]),
    ("D", ["D", "O"]),
    ("E", ["E", "O"]),
    ("K1", ["K1", "A", "B", "C", "O"]),
    ("K2", ["K2", "D", "B", "E", "O"]),
    ("K3", ["K3", "D", "A", "O"]),
    ("Z", ["Z", "K1", "K2", "K3", "D", "A", "B", "C", "E", "O"]),
]


@pytest.mark.parametrize("klass, mro", mro_pairs)
def test_c3(klass, mro):
    assert c3(dependencies, klass) == mro
