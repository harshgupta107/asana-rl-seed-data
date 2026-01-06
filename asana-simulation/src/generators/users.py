import random
from faker import Faker
from src.utils.helpers import get_uuid

fake = Faker()

def generate_users(cursor, workspace_id, count=50):
    print(f"Generating {count} Users...")
    user_ids = []
    
    for _ in range(count):
        uid = get_uuid()
        name = fake.name()
        # Realistic corporate email pattern
        email = f"{name.replace(' ', '.').lower()}@techflow.io"
        
        # Simple logic for Roles (Member, Admin, Guest)
        role = "Member"
        rand_val = random.random()
        if rand_val < 0.05:
            role = "Admin"
        elif rand_val > 0.95:
            role = "Guest"
        
        # UPDATED SQL: Added 'role' column and value
        cursor.execute("""
            INSERT INTO users (user_id, workspace_id, email, full_name, role) 
            VALUES (?, ?, ?, ?, ?)
        """, (uid, workspace_id, email, name, role))
        
        user_ids.append(uid)
        
    return user_ids