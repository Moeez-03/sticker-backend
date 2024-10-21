from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.models.category import Category
from app.db.session import SessionLocal
from app.services.storage_service import upload_to_aws_s3, upload_to_do_spaces

router = APIRouter()

@router.get("/")
def get_categories(db: SessionLocal = Depends()):
    """
    Fetch all categories from the database.
    """
    return db.query(Category).all()

@router.post("/")
def create_category(name: str, file: UploadFile = File(...), is_premium: bool = False, db: SessionLocal = Depends()):
    """
    Create a new category with an optional image upload.
    
    - name: Name of the category.
    - file: Image file to be uploaded (optional).
    - is_premium: Flag to indicate if the image should be stored in premium storage.
    """
    # Handle file upload (AWS S3 or DigitalOcean Spaces based on is_premium flag)
    content = file.file.read()
    filename = file.filename
    if is_premium:
        url = upload_to_aws_s3(content, filename)  # Upload to AWS S3
    else:
        url = upload_to_do_spaces(content, filename)  # Upload to DigitalOcean Spaces

    # Create a new category with the image URL
    new_category = Category(name=name, image_url=url)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return {
        "message": "Category created successfully",
        "category": {
            "id": new_category.id,
            "name": new_category.name,
            "image_url": new_category.image_url
        }
    }
