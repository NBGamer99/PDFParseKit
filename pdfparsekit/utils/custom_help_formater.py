import argparse

from pdfparsekit.utils.colors import Colors


class CustomHelpFormatter(argparse.HelpFormatter):
    def format_help(self):
        """Format the help text with color formatting.

        Returns:
            str: The formatted help text.

        """
        help_text = super().format_help()
        return f"{Colors.Fg.blue}Custom Help:{Colors.reset}\n{Colors.Fg.green}{help_text}{Colors.reset}"
