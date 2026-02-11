from configures import (
    Validator,
    ValidatorOption,
    ValidatorRegex,
    Variable,
)

import re


def test_validator_option_instantiation_with_defaults():
    """Test the instantiation and functionality of the ValidatorOption subclass."""

    options: list[object] = [1, 2, 3]

    validator = ValidatorOption(options=options)

    assert isinstance(validator, ValidatorOption)
    assert isinstance(validator, Validator)

    assert validator.options == options

    assert validator.required is True
    assert validator.nullable is False
    assert validator.typecast is False

    assert validator.typed is int


def test_validator_option_instantiation_with_overrides():
    """Test the instantiation and functionality of the ValidatorOption subclass."""

    options: list[object] = [1, 2, 3]

    validator = ValidatorOption(
        options=options,
        required=False,
        nullable=True,
        typecast=True,
    )

    assert isinstance(validator, ValidatorOption)
    assert isinstance(validator, Validator)

    assert validator.options == options

    assert validator.required is False
    assert validator.nullable is True
    assert validator.typecast is True

    assert validator.typed is int


def test_validator_option_casting():
    """Test the instantiation and functionality of the ValidatorOption subclass."""

    options: list[object] = [1, 2, 3]

    validator = ValidatorOption(options=options)

    assert isinstance(validator, ValidatorOption)
    assert isinstance(validator, Validator)

    assert validator.cast("1") == 1
    assert validator.cast(1) == 1
    assert validator.cast(1.0) == 1


def test_validator_option_valid_without_typecasting():
    """Test the instantiation and functionality of the ValidatorOption subclass."""

    options: list[object] = [1, 2, 3]

    validator = ValidatorOption(options=options)

    assert isinstance(validator, ValidatorOption)
    assert isinstance(validator, Validator)

    variable = Variable(name="TEST", value=2, validator=validator)

    assert isinstance(variable, Variable)
    assert variable.name == "TEST"
    assert variable.value == 2
    assert variable.validator is validator

    assert validator.valid(variable=variable) is True

    variable = Variable(name="TEST", value="2", validator=validator)

    assert isinstance(variable, Variable)

    assert variable.name == "TEST"
    assert variable.value == "2"
    assert variable.validator is validator

    assert validator.valid(variable=variable) is False


def test_validator_option_valid_with_typecasting():
    """Test the instantiation and functionality of the ValidatorOption subclass."""

    options: list[object] = [1, 2, 3]

    validator = ValidatorOption(options=options, typecast=True)

    assert isinstance(validator, ValidatorOption)
    assert isinstance(validator, Validator)

    variable = Variable(name="TEST", value="2", validator=validator)

    assert isinstance(variable, Variable)

    assert variable.name == "TEST"
    assert variable.value == "2"
    assert variable.validator is validator
    assert variable.validate() is True


def test_validator_regex_instantiation_with_string_pattern():
    """Test the instantiation and functionality of the ValidatorRegex subclass."""

    pattern: str = r"(YES|NO)"

    assert isinstance(pattern, str)

    validator = ValidatorRegex(pattern=pattern)

    assert isinstance(validator, ValidatorRegex)
    assert isinstance(validator, Validator)

    assert validator.pattern == re.compile(pattern)
    assert validator.required is True
    assert validator.nullable is False


def test_validator_regex_instantiation_with_regex_pattern():
    """Test the instantiation and functionality of the ValidatorRegex subclass."""

    pattern: re.Pattern = re.compile(r"(YES|NO)")

    assert isinstance(pattern, re.Pattern)

    validator = ValidatorRegex(pattern=pattern)

    assert isinstance(validator, ValidatorRegex)
    assert isinstance(validator, Validator)

    assert validator.pattern is pattern
    assert validator.required is True
    assert validator.nullable is False


def test_validator_regex_with_valid_option_yes():
    """Test the instantiation and functionality of the ValidatorRegex subclass."""

    pattern: str = r"(YES|NO)"

    validator = ValidatorRegex(pattern=pattern)

    assert isinstance(validator, ValidatorRegex)
    assert isinstance(validator, Validator)

    assert validator.pattern == re.compile(pattern)
    assert validator.required is True
    assert validator.nullable is False

    variable = Variable(name="TEST", value="YES", validator=validator)

    assert isinstance(variable, Variable)

    assert variable.name == "TEST"
    assert variable.value == "YES"
    assert variable.validator is validator
    assert variable.validate() is True  # YES is one of the regex matching values


def test_validator_regex_with_valid_option_no():
    """Test the instantiation and functionality of the ValidatorRegex subclass."""

    pattern: str = r"(YES|NO)"

    validator = ValidatorRegex(pattern=pattern)

    assert isinstance(validator, ValidatorRegex)
    assert isinstance(validator, Validator)

    assert validator.pattern == re.compile(pattern)
    assert validator.required is True
    assert validator.nullable is False

    variable = Variable(name="TEST", value="NO", validator=validator)

    assert isinstance(variable, Variable)

    assert variable.name == "TEST"
    assert variable.value == "NO"
    assert variable.validator is validator
    assert variable.validate() is True  # NO is one of the regex matching values


def test_validator_regex_with_invalid_option_maybe():
    """Test the instantiation and functionality of the ValidatorRegex subclass."""

    pattern: str = r"(YES|NO)"

    validator = ValidatorRegex(pattern=pattern)

    assert isinstance(validator, ValidatorRegex)
    assert isinstance(validator, Validator)

    assert validator.pattern == re.compile(pattern)
    assert validator.required is True
    assert validator.nullable is False

    variable = Variable(name="TEST", value="MAYBE", validator=validator)

    assert isinstance(variable, Variable)

    assert variable.name == "TEST"
    assert variable.value == "MAYBE"
    assert variable.validator is validator
    assert variable.validate() is False  # MAYBE is not one of the regex matching values
