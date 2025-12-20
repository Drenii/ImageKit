from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {
    1: {"title": "new post", "content": "cool post"},
    2: {"title": "hello world", "content": "my first post"},
    3: {"title": "update", "content": "small changes today"},
    4: {"title": "announcement", "content": "big news coming soon"},
    5: {"title": "tips", "content": "useful coding tips"},
    6: {"title": "thoughts", "content": "random daily thoughts"},
    7: {"title": "review", "content": "product review"},
    8: {"title": "guide", "content": "step by step tutorial"},
    9: {"title": "question", "content": "need some help"},
    10: {"title": "wrap up", "content": "final notes"}
}

@app.get("/")
async def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail=f"post with id: {id} was not found")

    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[len(text_posts) + 1] = new_post
    return new_post
