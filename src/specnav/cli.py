import typer
from .explore import explore
from .describe import describe
from .generate import generate

app = typer.Typer()


@app.callback()
def main():
    pass

app.command(name="explore")(explore)
app.command(name="describe")(describe)
app.command(name="generate")(generate)


if __name__ == "__main__":
    app()