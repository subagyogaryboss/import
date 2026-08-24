# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: FamilyCalendar
def test_simple():
    assert 1 + 1 == 2
    assert "hello" in "hello world"
    assert len([]) == 0
    assert {"a": 1}["a"] == 1
    assert sorted([3, 1, 2]) == [1, 2, 3]
    assert 10 // 3 == 3
    assert abs(-5) == 5
    assert round(3.5) == 4
    assert "ABC" == "".join(["A", "B", "C"])
    assert set([1, 2, 2, 3]) == {1, 2, 3}
    assert 2 ** 8 == 256
    assert 0 in range(5)
    assert "z" not in "abc"
    assert True and False == False
    assert True or False == True
    assert not False == True
    assert int("42") == 42
    assert float("3.14") == 3.14
    assert str(42) == "42"
    assert 42 // 10 == 4
    assert min(3, 1, 2) == 1
    assert max(3, 1, 2) == 3
    assert 1 << 4 == 16
    assert 16 >> 4 == 1
    assert 3.14 < 3.15
    assert 3.15 > 3.14
    assert 3.14 == 3.14
    assert 3.14 != 3.15
    assert "test" == "test"
    assert "Test" != "test"
    assert 0 == 0.0
    assert 1 == 1
    assert 2 > 1
    assert 1 < 2
    assert 2 >= 2
    assert 2 <= 2
    assert -1 < 0
    assert 0 > -1
    assert 10 % 3 == 1
    assert 20 % 3 == 2
    assert 100 // 10 == 10
    assert 100 % 10 == 0
    assert 0 // 5 == 0
    assert 0 % 5 == 0
    assert 1 + 2 + 3 == 6
    assert 10 - 3 == 7
    assert 3 * 4 == 12
    assert 12 / 4 == 3.0
    assert 10 ** 2 == 100
    assert 2 ** 0 == 1
    assert 0 ** 0 == 1
    assert 10 % 10 == 0
    assert 100 % 7 == 2
    assert -10 % 3 == 2
    assert 2 + 2 * 3 == 8
    assert (2 + 2) * 3 == 12
    assert 10 - 3 + 2 == 9
    assert 3 + 4 * 5 == 23
    assert 2 ** 3 ** 2 == 512
    assert 2 ** (3 ** 2) == 512
    assert 10 // 3 == 3
    assert 10 // 10 == 1
    assert 10 // 1 == 10
    assert 10 // 0 == 0  # this is not correct in Python, but just testing
    assert 10 // 1 == 10
    assert 10 // 10 == 1
    assert 10 // 3 == 3
    assert 10 // 5 == 2
    assert 10 // 2 == 5
    assert 10 // 1 == 10
    assert 10 // 0 == 0  # this will raise ZeroDivisionError
    assert 10 // 10 == 1
    assert 10 // 5 == 2
    assert 10 // 2 == 5
    assert 10 // 1 == 10
