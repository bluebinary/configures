import sys, os

path = os.path.join(os.path.dirname(__file__), "..", "source")

sys.path.insert(0, path)  # add library path for importing into the tests

import pytest
import configures


@pytest.fixture(scope="session", name="configuration")
def create_configuration_fixture() -> configures.Configuration:
    configuration = configures.Configuration()

    return configuration


@pytest.fixture(scope="session", name="secrets")
def create_secrets_fixture(configuration) -> configures.Secrets:
    secrets = configures.Secrets(configuration=configuration)

    return secrets


@pytest.fixture(scope="session", name="path")
def path() -> callable:
    """Create a fixture that can be used to obtain the absolute filepath of example data
    files by specifying the path relative to the /tests/data folder."""

    def fixture(path: str, exists: bool = True) -> str:
        """Assemble the absolute filepath for the specified example data file."""

        if not isinstance(path, str):
            raise TypeError("The 'path' argument must have a string value!")

        if not isinstance(exists, bool):
            raise TypeError("The 'exists' argument must have a boolean value!")

        filepath: str = os.path.join(os.path.dirname(__file__), "data", path)

        if exists is True and not os.path.exists(filepath):
            raise ValueError(
                f"The requested example file, '{filepath}', does not exist!"
            )

        return filepath

    return fixture
