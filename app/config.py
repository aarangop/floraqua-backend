from functools import lru_cache
import logging

from pydantic import BaseSettings, SecretStr


class Config(BaseSettings):
    app_name: str = "MongoDB API"
    # db_path: str
    db_protocol: str
    db_url: str
    db_opts: str
    db_name: str
    db_username: str
    db_password: SecretStr

    def get_connstr(self):
        if self.db_password and self.db_username:
            return f"{self.db_protocol}://{self.db_username}:{self.db_password.get_secret_value()}@{self.db_url}/{self.db_opts}"
        else:
            return f"{self.db_protocol}://{self.db_url}/{self.db_opts}"

    class Config:
        env_file = ".envrc"
        secrets_dir = "./.secrets"


@lru_cache()
def get_config():
    return Config()
