from configures import (
    Variable,
    Validator,
    ValidatorOption,
)


def test_variable_instantiation():
    """Test the instantiation and functionality of the Variable class."""

    validator = ValidatorOption(options=[1, 2, 3])

    assert isinstance(validator, ValidatorOption)
    assert isinstance(validator, Validator)

    variable = Variable(
        name="TEST",
        value=3,
        default=1,
        validator=validator,
    )

    assert isinstance(variable, Variable)

    assert variable.name == "TEST"
    assert variable.value == 3
    assert variable.default == 1
    assert variable.validator is validator

    assert variable.validate() is True
