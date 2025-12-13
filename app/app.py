from fastapi import FastAPI

app = FastAPI()

text_posts = {}

@app.get("/")
async def get_all_posts():
    return text_posts