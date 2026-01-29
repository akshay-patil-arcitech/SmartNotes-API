# Notes API with AI Integration

A comprehensive RESTful API built with FastAPI for managing notes with AI-powered features like summarization and title generation. The application includes JWT authentication, PostgreSQL database integration, and OpenAI integration for intelligent note processing.

## 🚀 Features

- **User Authentication**: Secure JWT-based authentication system with registration and login
- **CRUD Operations**: Complete Create, Read, Update, Delete operations for notes
- **AI Integration**: 
  - Automatic note summarization
  - Smart title suggestions based on content
- **User-specific Notes**: Each user can only access their own notes
- **RESTful API**: Well-structured endpoints following REST principles
- **Database**: PostgreSQL with SQLAlchemy ORM

## 📋 Table of Contents

- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Configuration](#environment-configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Postman Collection](#postman-collection)
- [Project Structure](#project-structure)

## 🛠 Technology Stack

- **Framework**: FastAPI 0.128.0
- **Database**: PostgreSQL with SQLAlchemy 2.0.46
- **Authentication**: JWT (python-jose 3.5.0)
- **Password Hashing**: bcrypt 3.2.0
- **AI Integration**: OpenAI 2.15.0
- **Server**: Uvicorn 0.40.0
- **Validation**: Pydantic 2.12.5

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.10 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- Git (optional, for cloning)

## 🔧 Installation

### 1. Clone or Extract the Project

```bash
# If using git
git clone <repository-url>
cd notes_project

# Or simply extract the zip file
unzip notes_project.zip
cd notes_project
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Environment Configuration

Create a `.env` file in the project root directory with the following variables:

```env
# Database Configuration
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
HOST=localhost
DB_NAME=notes_db

# JWT Configuration
SECRET_KEY=your_secret_key_here_use_long_random_string
ALGORITHM=HS256

# AI API Keys
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

### Environment Variables Explanation:

- **DB_USER**: PostgreSQL username
- **DB_PASSWORD**: PostgreSQL password
- **HOST**: Database host (usually `localhost` for local development)
- **DB_NAME**: Name of your PostgreSQL database
- **SECRET_KEY**: Secret key for JWT token generation (use a strong random string)
- **ALGORITHM**: Algorithm for JWT (use `HS256`)
- **OPENAI_API_KEY**: Your OpenAI API key for AI features
- **GROQ_API_KEY**: Groq API key (if using)
- **GOOGLE_API_KEY**: Google API key (if using)

### Generate a Strong Secret Key:

```python
import secrets
print(secrets.token_urlsafe(32))
```

## 🗄️ Database Setup

### 1. Create PostgreSQL Database

```sql
-- Connect to PostgreSQL
psql -U postgres

-- Create database
CREATE DATABASE notes_db;

-- Create user (optional, if not using existing user)
CREATE USER your_username WITH PASSWORD 'your_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE notes_db TO your_username;
```

### 2. Initialize Database Tables

The application will automatically create tables when you first run it, thanks to the `intitialize_database()` function in `main.py`.

## 🚀 Running the Application

### Start the Server

```bash
# Development mode with auto-reload
uvicorn main:app --reload

# Production mode
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at: `http://127.0.0.1:8000`

### Access Interactive API Documentation

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## 📖 API Documentation

### Base URL

```
http://127.0.0.1:8000/api
```

---

## 🔐 Authentication Endpoints

### 1. Register User

**Endpoint**: `POST /api/auth/register`

**Description**: Register a new user account

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "securePassword123"
}
```

**Success Response** (200 OK):
```json
{
  "Success": "User Register Successfully"
}
```

**Error Response** (400 Bad Request):
```json
{
  "detail": "User already exists"
}
```

---

### 2. Login

**Endpoint**: `POST /api/auth/login`

**Description**: Login and receive JWT access token

**Request Body** (Form Data):
```
username: john.doe@example.com
password: securePassword123
```

**Note**: The `username` field should contain the email address (OAuth2 standard format)

**Success Response** (200 OK):
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Error Response** (404 Not Found):
```json
{
  "detail": "Invalid Username or password"
}
```

---

## 📝 Notes Endpoints

**Authentication Required**: All notes endpoints require a valid JWT token in the Authorization header:

```
Authorization: Bearer <your_access_token>
```

---

### 3. Get All Notes

**Endpoint**: `GET /api/notes/`

**Description**: Retrieve all notes for the authenticated user

**Headers**:
```
Authorization: Bearer <your_access_token>
```

**Success Response** (200 OK):
```json
{
  "Success": [
    {
      "id": 1,
      "title": "Meeting Notes",
      "content": "Discussion about project timeline...",
      "owner_id": 1,
      "created_at": "2024-01-29T10:30:00",
      "updated_on": "2024-01-29T15:45:00"
    },
    {
      "id": 2,
      "title": "Ideas",
      "content": "New feature ideas for the app...",
      "owner_id": 1,
      "created_at": "2024-01-28T09:20:00",
      "updated_on": null
    }
  ]
}
```

---

### 4. Get Note by ID

**Endpoint**: `GET /api/notes/{id}`

**Description**: Retrieve a specific note by its ID

**Path Parameter**:
- `id` (integer): The ID of the note

**Headers**:
```
Authorization: Bearer <your_access_token>
```

**Example**: `GET /api/notes/1`

**Success Response** (200 OK):
```json
{
  "Success": {
    "id": 1,
    "title": "Meeting Notes",
    "content": "Discussion about project timeline...",
    "owner_id": 1,
    "created_at": "2024-01-29T10:30:00",
    "updated_on": "2024-01-29T15:45:00"
  }
}
```

**Error Response** (404 Not Found):
```json
{
  "detail": "Note with id 1 not found"
}
```

---

### 5. Create Note

**Endpoint**: `POST /api/notes/add`

**Description**: Create a new note

**Headers**:
```
Authorization: Bearer <your_access_token>
Content-Type: application/json
```

**Request Body**:
```json
{
  "title": "Project Planning",
  "content": "We need to plan the next sprint and allocate resources accordingly. Key priorities include bug fixes and new feature development."
}
```

**Success Response** (200 OK):
```json
{
  "status": 201,
  "message": "Note added Successfully"
}
```

---

### 6. Update Note

**Endpoint**: `PUT /api/notes/update/{id}`

**Description**: Update an existing note

**Path Parameter**:
- `id` (integer): The ID of the note to update

**Headers**:
```
Authorization: Bearer <your_access_token>
Content-Type: application/json
```

**Example**: `PUT /api/notes/update/1`

**Request Body**:
```json
{
  "title": "Updated Project Planning",
  "content": "Updated content with new priorities and revised timeline."
}
```

**Success Response** (200 OK):
```json
{
  "status": 200,
  "message": "Note updated sucessfully"
}
```

**Error Response** (404 Not Found):
```json
{
  "detail": "Note with id 1 not found"
}
```

---

### 7. Delete Note

**Endpoint**: `DELETE /api/notes/delete/{id}`

**Description**: Delete a note

**Path Parameter**:
- `id` (integer): The ID of the note to delete

**Headers**:
```
Authorization: Bearer <your_access_token>
```

**Example**: `DELETE /api/notes/delete/1`

**Success Response** (200 OK):
```json
{
  "status": 200,
  "message": "note with id 1 deleted successfully"
}
```

**Error Response** (404 Not Found):
```json
{
  "detail": "Note with id 1 not found"
}
```

---

## 🤖 AI-Powered Endpoints

**Authentication Required**: All AI endpoints require a valid JWT token

---

### 8. Summarize Note

**Endpoint**: `GET /api/ai/notes/{note_id}/summarize`

**Description**: Generate an AI-powered summary of a note

**Path Parameter**:
- `note_id` (integer): The ID of the note to summarize

**Headers**:
```
Authorization: Bearer <your_access_token>
```

**Example**: `GET /api/ai/notes/3/summarize`

**Success Response** (200 OK):
```json
{
  "summary": "The note discusses project planning priorities including bug fixes and feature development for the next sprint."
}
```

**Error Response** (404 Not Found):
```json
{
  "detail": "Note not found"
}
```

---

### 9. Suggest Title

**Endpoint**: `GET /api/ai/notes/{id}/suggest-title`

**Description**: Generate an AI-suggested title based on note content

**Path Parameter**:
- `id` (integer): The ID of the note

**Headers**:
```
Authorization: Bearer <your_access_token>
```

**Example**: `GET /api/ai/notes/5/suggest-title`

**Success Response** (200 OK):
```json
{
  "title": "Next Sprint Planning and Resource Allocation"
}
```

**Error Response** (404 Not Found):
```json
{
  "detail": "Note not found"
}
```

---

## 📮 Postman Collection

### Import Postman Collection

The project includes a pre-configured Postman collection: `akshay_notes_api.postman_collection.json`

#### Step-by-Step Import Guide:

1. **Open Postman Application**

2. **Import the Collection**:
   - Click on the **"Import"** button (top-left corner)
   - Select **"File"** tab
   - Click **"Choose Files"**
   - Navigate to the project folder and select `akshay_notes_api.postman_collection.json`
   - Click **"Import"**

3. **Configure Environment Variables**:
   - Click on **"Environments"** in the left sidebar
   - Click **"+"** to create a new environment
   - Name it: `Notes API Local`
   - Add the following variables:

   | Variable | Initial Value | Current Value |
   |----------|--------------|---------------|
   | `base_url` | `http://127.0.0.1:8000` | `http://127.0.0.1:8000` |
   | `access_token` | (leave empty) | (will be set automatically) |

4. **Set Active Environment**:
   - Select **"Notes API Local"** from the environment dropdown (top-right)

### Using the Collection:

#### Authentication Flow:

1. **Register a User**:
   - Open the **"register"** request
   - Modify the JSON body with your details
   - Click **"Send"**
   - Verify you receive a success response

2. **Login**:
   - Open the **"login"** request
   - The body is already configured as form-data
   - Update the `username` (email) and `password` fields
   - Click **"Send"**
   - **Important**: Copy the `access_token` from the response

3. **Set Access Token**:
   - Method 1 (Manual):
     - Go to Environments > Notes API Local
     - Paste the token into the `access_token` variable's current value
   - Method 2 (Automatic):
     - Add this script to the login request's **Tests** tab:
     ```javascript
     pm.test("Set access token", function () {
         var jsonData = pm.response.json();
         pm.environment.set("access_token", jsonData.access_token);
     });
     ```

4. **Test Protected Endpoints**:
   - All other requests are pre-configured to use `{{access_token}}`
   - Simply select any request and click **"Send"**

### Request Examples in Collection:

| Request Name | Method | Endpoint | Description |
|-------------|--------|----------|-------------|
| register | POST | `/api/auth/register` | Register new user |
| login | POST | `/api/auth/login` | Login and get token |
| get_all_notes | GET | `/api/notes/` | Get all user notes |
| get_note_by_id | GET | `/api/notes/{id}` | Get specific note |
| add_note | POST | `/api/notes/add` | Create new note |
| update_note | PUT | `/api/notes/update/{id}` | Update existing note |
| delete_note | DELETE | `/api/notes/delete/{id}` | Delete note |
| summerize_note | GET | `/api/ai/notes/{note_id}/summarize` | Summarize note with AI |
| suggest_title | GET | `/api/ai/notes/{id}/suggest-title` | Get AI title suggestion |

### Tips for Using Postman:

- **Authorization**: All requests except register and login have Bearer Token authentication pre-configured with `{{access_token}}`
- **Variables**: You can reference environment variables in the URL, headers, or body using `{{variable_name}}`
- **Testing**: Use the Tests tab to write assertions and automate token management
- **Save Responses**: Use the "Save Response" button to keep example responses for documentation

---

## 📁 Project Structure

```
notes_project/
│
├── main.py                          # Application entry point
├── requirements.txt                 # Python dependencies
├── .env                            # Environment variables (create this)
│
├── auth_jwt/                       # JWT authentication module
│   └── auth.py                     # JWT utilities and password hashing
│
├── config/                         # Configuration module
│   └── prj_config.py              # Pydantic settings configuration
│
├── models/                         # Database models
│   ├── auth.py                    # User model
│   └── notes.py                   # Note model
│
├── schemas/                        # Pydantic schemas (validation)
│   ├── auth.py                    # User schemas
│   └── notes.py                   # Note schemas
│
├── routes/                         # API route handlers
│   ├── auth.py                    # Authentication routes
│   ├── notes.py                   # Notes CRUD routes
│   └── ai.py                      # AI-powered routes
│
├── database.py                     # Database connection and session
├── init_db.py                     # Database initialization
├── chat_service.py                # AI service integration
│
└── akshay_notes_api.postman_collection.json  # Postman collection
```

### Key Files Description:

- **main.py**: FastAPI application instance and route registration
- **database.py**: SQLAlchemy engine and session configuration
- **init_db.py**: Creates database tables on startup
- **auth_jwt/auth.py**: JWT token generation, verification, and password hashing
- **models/**: SQLAlchemy ORM models defining database structure
- **schemas/**: Pydantic models for request/response validation
- **routes/**: API endpoint implementations organized by feature
- **chat_service.py**: OpenAI integration for AI features

---

## 🔒 Security Features

- **Password Hashing**: All passwords are hashed using bcrypt
- **JWT Tokens**: Secure token-based authentication
- **User Isolation**: Users can only access their own notes
- **Environment Variables**: Sensitive data stored in .env file
- **CORS**: Can be configured for production deployment

---

## 🐛 Troubleshooting

### Common Issues:

1. **Database Connection Error**:
   ```
   Solution: Verify PostgreSQL is running and .env credentials are correct
   ```

2. **Module Not Found Error**:
   ```
   Solution: Ensure all dependencies are installed: pip install -r requirements.txt
   ```

3. **JWT Token Error**:
   ```
   Solution: Check SECRET_KEY in .env and ensure token hasn't expired
   ```

4. **Port Already in Use**:
   ```
   Solution: Change port: uvicorn main:app --port 8001
   ```

5. **OpenAI API Error**:
   ```
   Solution: Verify OPENAI_API_KEY is valid and has sufficient credits
   ```

---

## 📝 Development Notes

### Adding New Endpoints:

1. Create schema in `schemas/`
2. Create/update model in `models/`
3. Implement route in `routes/`
4. Register router in `main.py`

### Database Migrations:

For production, consider using Alembic for database migrations:

```bash
pip install alembic
alembic init alembic
# Configure and create migrations
```

---

## 📄 License

This project is for educational purposes. Modify and use as needed.

---

## 👤 Author

**Akshay Patil**

For questions or support, please refer to the API documentation or Postman collection.

---

## 📚 API Response Status Codes

| Status Code | Description |
|------------|-------------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

**Happy Coding! 🚀**
