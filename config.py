import os

class Config:
    TEST_VARIABLE = "Config"
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    TEST_VARIABLE = "Dev Config"
    DEBUG = True

class TestConfig(Config):
    TEST_VARIABLE = "Test Config"
    TESTING = True

def runtime_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    if env == "TEST":
        return TestConfig
    else:
        return Config