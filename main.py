from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World. It is 3. Three. Hello Ankit!"}


