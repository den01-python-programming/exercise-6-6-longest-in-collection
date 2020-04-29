import pytest
from src.simple_collection import SimpleCollection

def test_exercise():
    j = SimpleCollection("characters")

    assert j.longest() == None

    j.add("Harry")
    j.add("Ron")
    j.add("Hermione")

    assert j.longest() == "Hermione"
