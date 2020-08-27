import pytest

# Пометьте первый тест параметром, который в случае неожиданного прохождения теста,
# помеченного как xfail, отметит в отчете этот тест как упавший.


@pytest.mark.xfail(strict=True)  # strict=True
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
