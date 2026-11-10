"""Exercise 11: data persistence.

Topics: open and close, write, readline, JSON, pickle, data that survives between runs.
Check your work:
    python check.py ex11
"""

import json
import pickle


def read_first_line(path):
    """Return the first line without the newline.
    Return "" if the file does not exist.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readline().rstrip("\n")
    except FileNotFoundError:
        return ""


def save_settings(path, settings):
    """Save dictionary settings as JSON."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)


def load_settings(path):
    """Load JSON settings or return an empty dictionary."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_object(path, value):
    """Save any Python value using pickle."""
    with open(path, "wb") as file:
        pickle.dump(value, file)


def load_object(path):
    """Load a Python value using pickle."""
    with open(path, "rb") as file:
        return pickle.load(file)


def record_visit(path):
    """Increase the saved visit count by one."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            count = int(file.read())
    except FileNotFoundError:
        count = 0

    count += 1

    with open(path, "w", encoding="utf-8") as file:
        file.write(str(count))

    return count
