from functools import lru_cache
import logging

from pydantic import BaseSettings


class Config(BaseSettings):
    app_name: str = "MongoDB API"
    db_path: str
    db_name: str

    class Config:
        env_file = ".envrc"


@lru_cache()
def get_config():
    return Config()
