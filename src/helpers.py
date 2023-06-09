from typer import prompt
from rich.console import Console
from rich.table import Table

console = Console()


def table_data(mode: str, lang: str) -> None:
    """Print table data"""
    table = Table("Mode", "Language")
    table.add_row(mode, lang)

    console.print(table)


def get_user_input(question: str = "What's your question?") -> str:
    """"Get user input / Interactive mode"""
    return prompt(question)
