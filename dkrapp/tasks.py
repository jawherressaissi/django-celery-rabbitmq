from .celery import app


@app.task(name="hello")
def hello():
    print("\nhello\n")