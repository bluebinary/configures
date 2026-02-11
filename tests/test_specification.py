from configures import (
    Secrets,
    Configuration,
    Specification,
    SpecificationFile,
    SpecificationFileJSON,
    SpecificationFileYAML,
    SpecificationData,
)


def test_configures_with_file_specification(path: callable):
    """Test the library with a plain-text specification file."""

    specification = path("specifications/sample.spec")

    assert isinstance(specification, str)

    secrets = Secrets(
        configuration=Configuration(
            specification=SpecificationFile(
                filename=specification,
            ),
        ),
    )

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFile)
    assert isinstance(secrets.configuration.specification, Specification)

    assert "TZ" in secrets
    assert isinstance(secrets["TZ"], str)
    assert secrets["TZ"] == "Somewhere/There"


def test_configures_with_json_specification(path: callable):
    """Test the library with a JSON-serialised specification file."""

    specification = path("specifications/sample.json")

    assert isinstance(specification, str)

    secrets = Secrets(
        configuration=Configuration(
            specification=SpecificationFileJSON(
                filename=specification,
            ),
        ),
    )

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFileJSON)
    assert isinstance(secrets.configuration.specification, Specification)

    assert "TZ" in secrets
    assert isinstance(secrets["TZ"], str)
    assert secrets["TZ"] == "Somewhere/There"


def test_configures_with_yaml_specification(path: callable):
    """Test the library with a YAML-serialised specification file."""

    specification = path("specifications/sample.yaml")

    assert isinstance(specification, str)

    secrets = Secrets(
        configuration=Configuration(
            specification=SpecificationFileYAML(
                filename=specification,
            ),
        ),
    )

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationFileYAML)
    assert isinstance(secrets.configuration.specification, Specification)

    assert "TZ" in secrets
    assert isinstance(secrets["TZ"], str)
    assert secrets["TZ"] == "Somewhere/There"


def test_configures_with_data_specification(path: callable):
    """Test the library with specification data."""

    specification = path("specifications/sample.spec")

    assert isinstance(specification, str)

    secrets = Secrets(
        configuration=Configuration(
            specification=SpecificationData(
                TZ=dict(
                    required=True,
                    nullable=False,
                    pattern=r"[A-Za-z\\_]+\/[A-Za-z\\_]",
                    default="America/Los_Angeles",
                ),
            ),
        ),
    )

    assert isinstance(secrets, Secrets)
    assert isinstance(secrets.configuration, Configuration)
    assert isinstance(secrets.configuration.specification, SpecificationData)
    assert isinstance(secrets.configuration.specification, Specification)

    assert "TZ" in secrets
    assert isinstance(secrets["TZ"], str)
    assert secrets["TZ"] == "Somewhere/There"
