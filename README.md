# EnvironmentLoader

## Why I Made This?
It's often hard to find the right place to load your environment or ensure that there are no typos in your environment varaibles. This makes it so that you no longer have to worry about typos and on the first call of getting your environment variables the environment is loaded. Two birds one stone.

Description
The Environment class provides a structured way to manage environment variables in your Python application. By defining an enumeration of required environment keys, you can easily load, verify, and access these variables from a .env file or your system environment. This ensures that all necessary environment variables are available and properly set before your application runs.

Features
Setup Environment Keys: Define the required environment keys using an enumeration.
Load Environment Variables: Load environment variables from a .env file or system environment.
Verify Environment Variables: Ensure all required environment variables are present.
Access Environment Variables: Safely access the values of environment variables.
Installation
Install the environment-loader package:

bash
Copy code
python3 -m pip install environment-loader
Save the environment.py file in your project directory.

Usage
Define your environment keys:

python
Copy code
from enum import Enum

class EnvironmentKeys(Enum):
    DATABASE_URL = "DATABASE_URL"
    SECRET_KEY = "SECRET_KEY"
    API_KEY = "API_KEY"
Setup and load environment variables:

python
Copy code
from environment import Environment

# Set up environment with keys and optional path to .env file
Environment.setup_environment(environment_keys=EnvironmentKeys)

# Load environment variables
Environment.load_environment_variables()
Access environment variables:

python
Copy code
# Access a specific environment variable
database_url = Environment.get_environment_variable(EnvironmentKeys.DATABASE_URL)
secret_key = Environment.get_environment_variable(EnvironmentKeys.SECRET_KEY)
api_key = Environment.get_environment_variable(EnvironmentKeys.API_KEY)

print(f"Database URL: {database_url}")
print(f"Secret Key: {secret_key}")
print(f"API Key: {api_key}")
Example
.env file

Create a .env file in your project root with the following content:

env
Copy code
DATABASE_URL=postgres://user:password@localhost:5432/mydatabase
SECRET_KEY=supersecretkey
API_KEY=1234567890abcdef
main.py

python
Copy code
from enum import Enum
from environment import Environment

# Define your environment keys
class EnvironmentKeys(Enum):
    DATABASE_URL = "DATABASE_URL"
    SECRET_KEY = "SECRET_KEY"
    API_KEY = "API_KEY"

# Set up the environment keys and path to .env file
Environment.setup_environment(environment_keys=EnvironmentKeys, environment_path=".env")

# Load the environment variables
Environment.load_environment_variables()

# Access and use the environment variables
database_url = Environment.get_environment_variable(EnvironmentKeys.DATABASE_URL)
secret_key = Environment.get_environment_variable(EnvironmentKeys.SECRET_KEY)
api_key = Environment.get_environment_variable(EnvironmentKeys.API_KEY)

print(f"Database URL: {database_url}")
print(f"Secret Key: {secret_key}")
print(f"API Key: {api_key}")
Conclusion
The Environment class simplifies the management of environment variables in your Python application. By defining required keys and verifying their presence, you can ensure that your application has all the necessary configuration before it runs.





