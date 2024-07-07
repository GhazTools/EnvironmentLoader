"""
file_name = environment.py
Created On: 2024/07/07
Lasted Updated: 2024/07/07
Description: _FILL OUT HERE_
Edit Log:
2024/07/07
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from enum import Enum
from typing import Optional, Type
from os import getenv

# THIRD PARTY LIBRARY IMPORTS
from dotenv import load_dotenv

# LOCAL LIBRARY IMPORT


class Environment:
    """
    A class to handle the environment variables
    """

    _environment_keys: Type[Enum]
    _environment_path: Optional[str]
    _is_loaded = False

    @staticmethod
    def setup_environment(
        environment_keys: Type[Enum], environment_path: Optional[str] = None
    ):
        """
        Set the environment keys
        """
        Environment._environment_keys = environment_keys

        if environment_path:
            Environment._environment_path = environment_path
        else:
            Environment._environment_path = None

    @staticmethod
    def load_environment_variables() -> None:
        """
        A method to load the environment variables
        """

        if Environment._is_loaded:
            return

        if Environment._environment_path:
            load_dotenv(dotenv_path=Environment._environment_path)
        else:
            load_dotenv()

        Environment.verify_environment_variables()
        Environment._is_loaded = True

    @staticmethod
    def verify_environment_variables() -> None:
        """
        A method to verify the environment
        """

        missing_keys = []
        for key in Environment._environment_keys:
            key_value = key.value

            if getenv(key_value) is None:
                missing_keys.append(key_value)

        if missing_keys:
            raise ValueError("Missing environment variables:", ", ".join(missing_keys))

    @staticmethod
    def get_environment_variable(key: Enum) -> str:
        """
        A method to get the environment variable
        """

        Environment.load_environment_variables()

        value = getenv(key.value)
        assert value is not None, f"Missing environment variable: {key.value}"

        return value
