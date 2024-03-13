import logging.config
import os

import yaml


class Logger:
    """
    A Logger class that provides logging functionality.

    Args:
        config_path (str): The path to the logging configuration file.

    Raises:
        FileNotFoundError: If the logging configuration file is not found.

    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "is_configured"):
            self.configure_logger("./logger_conf.yml")
        self.logger = logging.getLogger("root")

    def configure_logger(self, config_path):
        """
        Configures the logger using the provided configuration file.

        Args:
            config_path (str): The path to the logging configuration file.

        Raises:
            FileNotFoundError: If the logging configuration file is not found.

        """
        if os.path.exists(config_path):
            with open(config_path, "rt", encoding="utf-8") as f:
                config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
            self.is_configured = True
        else:
            raise FileNotFoundError(f"Logging configuration file not found at {config_path}")
