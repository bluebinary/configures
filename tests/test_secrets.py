from configures import (
    Secrets,
    Configuration,
    Specification,
    SpecificationFile,
    SpecificationFileJSON,
    SpecificationFileYAML,
    SpecificationData,
)

import json


def test_secrets_instantiation():
    """Test the instantiation and functionality of the Secrets class."""

    secrets = Secrets()

    assert isinstance(secrets, Secrets)


def test_secrets_instantiation_as_singleton():
    """Test the instantiation and functionality of the Secrets class."""

    secrets_a = Secrets()

    assert isinstance(secrets_a, Secrets)

    secrets_b = Secrets()

    assert isinstance(secrets_b, Secrets)

    assert secrets_a is secrets_b


def test_secrets_instantiation_with_specification_file(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.spec")

    assert isinstance(filename, str)

    secrets = Secrets(specification=filename)

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert secrets.configuration.specification.filename == filename


def test_secrets_instantiation_with_specification_json_file(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.json")

    assert isinstance(filename, str)

    secrets = Secrets(specification=filename)

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFileJSON)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert secrets.configuration.specification.filename == filename


def test_secrets_instantiation_with_specification_yaml_file(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.yaml")

    assert isinstance(filename, str)

    secrets = Secrets(specification=filename)

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFileYAML)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert secrets.configuration.specification.filename == filename


def test_secrets_instantiation_with_specification_file_class(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.spec")

    assert isinstance(filename, str)

    secrets = Secrets(specification=SpecificationFile(filename=filename))

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert secrets.configuration.specification.filename == filename


def test_secrets_instantiation_with_specification_json_class(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.json")

    assert isinstance(filename, str)

    secrets = Secrets(specification=SpecificationFileJSON(filename=filename))

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFileJSON)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert secrets.configuration.specification.filename == filename


def test_secrets_instantiation_with_specification_yaml_class(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.yaml")

    assert isinstance(filename, str)

    secrets = Secrets(specification=SpecificationFileYAML(filename=filename))

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFileYAML)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert secrets.configuration.specification.filename == filename


def test_secrets_instantiation_with_configuration_class_with_spec_file(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.spec")

    assert isinstance(filename, str)

    secrets = Secrets(configuration=Configuration(specification=filename))

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert secrets.configuration.specification.filename == filename


def test_secrets_instantiation_with_configuration_class_with_json_file(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.json")

    assert isinstance(filename, str)

    secrets = Secrets(configuration=Configuration(specification=filename))

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFileJSON)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert secrets.configuration.specification.filename == filename


def test_secrets_instantiation_with_configuration_class_with_yaml_file(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.yaml")

    assert isinstance(filename, str)

    secrets = Secrets(configuration=Configuration(specification=filename))

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFileYAML)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert secrets.configuration.specification.filename == filename


def test_secrets_instantiation_with_configuration_class_with_spec_class(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.spec")

    assert isinstance(filename, str)

    secrets = Secrets(
        configuration=Configuration(
            specification=SpecificationFile(
                filename=filename,
            ),
        ),
    )

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert secrets.configuration.specification.filename == filename


def test_secrets_instantiation_with_configuration_class_with_json_class(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.json")

    assert isinstance(filename, str)

    secrets = Secrets(
        configuration=Configuration(
            specification=SpecificationFileJSON(
                filename=filename,
            ),
        ),
    )

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFileJSON)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert secrets.configuration.specification.filename == filename


def test_secrets_instantiation_with_configuration_class_with_yaml_class(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.yaml")

    assert isinstance(filename, str)

    secrets = Secrets(
        configuration=Configuration(
            specification=SpecificationFileYAML(
                filename=filename,
            ),
        ),
    )

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFileYAML)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert secrets.configuration.specification.filename == filename


def test_secrets_instantiation_with_configuration_class_with_data_class(path: callable):
    """Test the instantiation and functionality of the Secrets class."""

    filename: str = path("specifications/sample.json")

    assert isinstance(filename, str)

    variables: dict[str, object] = {}

    # Load the specification data from the file; data could also be generated or inlined
    with open(filename, "r") as file:
        variables = json.load(file)

    secrets = Secrets(
        configuration=Configuration(
            specification=SpecificationData(
                **variables,
            ),
        ),
    )

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationData)
    assert isinstance(secrets.configuration.specification, Specification)

    for name, variable in secrets.configuration.specification.items():
        assert name in variables

        required: bool = variables[name].get("required") is True
        optional: bool = variables[name].get("optional") is True
        nullable: bool = variables[name].get("nullable") is True
        default: object = variables[name].get("default")

        assert variable.validator.required is (required is True) or (optional is False)
        assert variable.validator.nullable is nullable
        assert variable.default is default
