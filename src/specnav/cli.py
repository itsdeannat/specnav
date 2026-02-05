import typer
from .explore import explore
from .describe import describe

app = typer.Typer()


@app.callback()
def main():
    pass

app.command(name="explore")(explore)
app.command(name="describe")(describe)


if __name__ == "__main__":
    app()