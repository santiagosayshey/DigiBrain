```mermaid
sequenceDiagram
    participant U as User
    participant R as React Frontend
    participant F as Flask Backend
    
    Note over U,F: Registration Process
    U->>R: Enter registration details
    R->>F: POST /register (username, password, etc.)
    F->>F: Validate input
    F->>F: Create new user
    F-->>R: Return success/failure
    R-->>U: Display registration result

    Note over U,F: Login Process
    U->>R: Enter credentials
    R->>F: POST /login (username, password)
    F->>F: Verify credentials
    F->>F: Generate JWT
    F-->>R: Return JWT
    R->>R: Store JWT (e.g., localStorage)
    
    Note over U,F: Accessing Protected Resources
    U->>R: Request protected resource
    R->>F: GET /protected (with JWT in header)
    F->>F: Validate JWT
    F-->>R: Return protected data
    R-->>U: Display protected data
    
    Note over R,F: Subsequent requests include JWT
```

```python
# backend/app/user_db.py
import hashlib
import os

USER_DATA_FILE = 'users.txt'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    hashed_password = hash_password(password)
    with open(USER_DATA_FILE, 'a') as file:
        file.write(f"{username}:{hashed_password}\n")
    print(f"User {username} registered successfully.")

def authenticate_user(username, password):
    hashed_password = hash_password(password)
    with open(USER_DATA_FILE, 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username and hashed_password == stored_password:
                return True
    return False
```


```python
# backend/app/auth.py
from flask import Blueprint, request, jsonify
from .user_db import register_user, authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # TODO: Check if username already exists

    try:
        register_user(username, password)
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```