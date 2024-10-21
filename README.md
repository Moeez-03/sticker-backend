# WhatsApp Sticker Backend

This project provides the backend infrastructure for managing WhatsApp stickers using **FastAPI**. The backend supports different functionalities including sticker management, categorization, handling free and premium stickers, and user authentication.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

1. **Sticker Categories**: Manage various categories of stickers.
2. **Free vs Premium Stickers**: Differentiate between premium and free sticker collections.
3. **User Management**:
   - Free users: Access free stickers hosted on Digital Ocean.
   - Premium users: Access premium stickers hosted on AWS.
4. **Admin Panel**: Secure admin credentials to manage sticker categories, users, and backend functionalities.

## Technologies

- **Python 3.x**
- **FastAPI**
- **PostgreSQL/MySQL** (or any database)
- **AWS S3** (for premium stickers)
- **Digital Ocean** (for free stickers)
- **JWT Authentication**
- **Docker** (Optional)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/HussnainC/WhatsAppStickerMaker.git
cd WhatsAppStickerMaker

## install dependencies
pip install -r requirements.txt

## Setup Environments variable
DATABASE_URL="your_database_url"
SECRET_KEY="your_secret_key"
ALGORITHM="HS256"
AWS_ACCESS_KEY_ID="your_aws_key"
AWS_SECRET_ACCESS_KEY="your_aws_secret"

## Run the appllication
uvicorn app.main:app --reload

## Api Endpoints
Here is a list of some important endpoints. Full documentation will be available at /docs.

### Sticker Management

GET /api/sticker-categories/: Retrieve all sticker categories.
POST /api/stickers/upload/: Upload a new sticker (Admin only).
GET /api/stickers/: Retrieve all stickers (both free and premium).

### User Management

POST /api/users/register/: Register a new user.
POST /api/users/login/: Log in a user and obtain a JWT token.

## Usage 

Admin Panel: Admins can log in to manage users and stickers via secure credentials.
Free Users: Free users can access stickers hosted on Digital Ocean.
Premium Users: Premium users can access stickers via AWS storage.

## Countributing

Contributions are welcome! Please create a fork and submit a pull request for review.

# LINCENSE

This project is licensed under the MIT License. See the LICENSE file for details.