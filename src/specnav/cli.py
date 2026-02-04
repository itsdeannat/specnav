import typer
from .explore import explore

app = typer.Typer()


@app.callback()
def main():
    pass

app.command(name="explore")(explore)


if __name__ == "__main__":
    app()