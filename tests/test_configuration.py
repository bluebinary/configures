from configures import (
    Configuration,
    Specification,
    SpecificationFile,
    SpecificationFileJSON,
    SpecificationFileYAML,
    SpecificationData,
)

import json


def test_configuration_instantiation_with_specification_instance(path: callable):
    """Test instantiation of the Configuration class using a sample specification."""

    filename: str = path("specifications/sample.spec")

    assert isinstance(filename, str)

    configuration = Configuration(
        specification=SpecificationFile(filename=filename),
    )

    assert isinstance(configuration, Configuration)

    assert isinstance(configuration.specification, SpecificationFile)
    assert isinstance(configuration.specification, Specification)
    assert configuration.specification.filename == filename


def test_configuration_instantiation_with_specification_file(path: callable):
    """Test instantiation of the Configuration class using a sample specification."""

    filename: str = path("specifications/sample.spec")

    assert isinstance(filename, str)

    configuration = Configuration(specification=filename)

    assert isinstance(configuration, Configuration)

    assert isinstance(configuration.specification, SpecificationFile)
    assert isinstance(configuration.specification, Specification)
    assert configuration.specification.filename == filename


def test_configuration_instantiation_with_specification_file_json(path: callable):
    """Test instantiation of the Configuration class using a sample specification."""

    filename: str = path("specifications/sample.json")

    assert isinstance(filename, str)

    configuration = Configuration(specification=filename)

    assert isinstance(configuration, Configuration)

    assert isinstance(configuration.specification, SpecificationFileJSON)
    assert isinstance(configuration.specification, Specification)
    assert configuration.specification.filename == filename


def test_configuration_instantiation_with_specification_file_yaml(path: callable):
    """Test instantiation of the Configuration class using a sample specification."""

    filename: str = path("specifications/sample.yaml")

    assert isinstance(filename, str)

    configuration = Configuration(specification=filename)

    assert isinstance(configuration, Configuration)

    assert isinstance(configuration.specification, SpecificationFileYAML)
    assert isinstance(configuration.specification, Specification)
    assert configuration.specification.filename == filename


def test_configuration_instantiation_with_specification_data(path: callable):
    """Test instantiation of the Configuration class using a sample specification."""

    filename: str = path("specifications/sample.json")

    assert isinstance(filename, str)

    specification: dict[str, object] = {}

    with open(filename, "r") as file:
        specification = json.load(file)

    configuration = Configuration(specification=specification)

    assert isinstance(configuration, Configuration)

    assert isinstance(configuration.specification, SpecificationData)
    assert isinstance(configuration.specification, Specification)


def test_configuration_instantiation_with_specification_file_class(path: callable):
    """Test instantiation of the Configuration class using a sample specification."""

    filename: str = path("specifications/sample.spec")

    assert isinstance(filename, str)

    configuration = Configuration(
        specification=SpecificationFile(filename=filename),
    )

    assert isinstance(configuration, Configuration)

    assert isinstance(configuration.specification, SpecificationFile)
    assert isinstance(configuration.specification, Specification)
    assert configuration.specification.filename == filename


def test_configuration_instantiation_with_specification_json_class(path: callable):
    """Test instantiation of the Configuration class using a sample specification."""

    filename: str = path("specifications/sample.json")

    assert isinstance(filename, str)

    configuration = Configuration(
        specification=SpecificationFileJSON(filename=filename),
    )

    assert isinstance(configuration, Configuration)

    assert isinstance(configuration.specification, SpecificationFileJSON)
    assert isinstance(configuration.specification, SpecificationFile)
    assert isinstance(configuration.specification, Specification)
    assert configuration.specification.filename == filename


def test_configuration_instantiation_with_specification_yaml_class(path: callable):
    """Test instantiation of the Configuration class using a sample specification."""

    filename: str = path("specifications/sample.yaml")

    assert isinstance(filename, str)

    configuration = Configuration(
        specification=SpecificationFileYAML(filename=filename),
    )

    assert isinstance(configuration, Configuration)

    assert isinstance(configuration.specification, SpecificationFileYAML)
    assert isinstance(configuration.specification, SpecificationFile)
    assert isinstance(configuration.specification, Specification)
    assert configuration.specification.filename == filename
