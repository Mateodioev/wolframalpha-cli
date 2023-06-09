import os
import json

DEFAULT_PATH = os.path.expanduser("~/.config/wolframalpha/config.json")


def config_path() -> str:
    """
    Returns the default config path, create if it doesn't exist
    """
    path = DEFAULT_PATH
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def read_config(path: str) -> dict:
    """
    Read the config FILE_NAME at the given path
    """
    with open(path, "r") as f:
        return json.load(f)


def get_app_id(path: str = DEFAULT_PATH) -> [str, None]:
    try:
        return read_config(path)['app_id']
    except FileNotFoundError as e:
        print(e)
        return None


def save_config(path: str, data: dict) -> None:
    """
    Save the config FILE_NAME at the given path
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
