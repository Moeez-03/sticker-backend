from fastapi import FastAPI
from app.api.endpoints import users, stickers, categories
from app.db.session import engine
from app.db.base import Base
from core.config import settings  # Import the core settings

app = FastAPI()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(users.router, prefix="/api/users")
app.include_router(stickers.router, prefix="/api/stickers")
app.include_router(categories.router, prefix="/api/categories")

# Access settings (core configuration)
print(f"Database URL: {settings.DATABASE_URL}")
print(f"JWT Secret Key: {settings.JWT_SECRET_KEY}")

# Example of middleware or other logic using the core settings
@app.on_event("startup")
async def startup_event():
    # You could initialize something like database connection here using settings
    print(f"App starting with AWS bucket: {settings.AWS_BUCKET_NAME}")

async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })
