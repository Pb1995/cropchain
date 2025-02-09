import logging
from colorama import init, Fore, Style

# Initialize colorama for Windows compatibility
init()

class PrettyFormatter(logging.Formatter):
    """A custom formatter for pretty-printing logs with colors."""
    
    def __init__(self):
        super().__init__()
        self.formats = {
            logging.DEBUG: Fore.BLUE + '%(asctime)s - %(levelname)-8s - %(message)s' + Style.RESET_ALL,
            logging.INFO: Fore.GREEN + '%(asctime)s - %(levelname)-8s - %(message)s' + Style.RESET_ALL,
            logging.WARNING: Fore.YELLOW + '%(asctime)s - %(levelname)-8s - %(message)s' + Style.RESET_ALL,
            logging.ERROR: Fore.RED + '%(asctime)s - %(levelname)-8s - %(message)s' + Style.RESET_ALL,
            logging.CRITICAL: Fore.RED + Style.BRIGHT + '%(asctime)s - %(levelname)-8s - %(message)s' + Style.RESET_ALL,
        }

    def format(self, record):
        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%Y-%m-%d %H:%M:%S')
        return formatter.format(record)

def setup_pretty_logging():
    """Configure logging with pretty formatting."""
    handler = logging.StreamHandler()
    handler.setFormatter(PrettyFormatter())
    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler]
    )