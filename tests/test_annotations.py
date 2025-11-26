import pytest
import testit

@testit.externalId("with_parameters_success")
@testit.displayName("with_parameters_success")
@testit.title("with_parameters_success")
@pytest.mark.parametrize('number, text', [
    (1, "string1")
])
def test_with_parameters_success(number: int, text: str):
    assert True

