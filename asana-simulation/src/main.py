import sys
import os

# Fix path to ensure imports work when running from root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.db import DatabaseManager
from src.generators import users, projects, tasks

DB_PATH = "output/asana_simulation.sqlite"
SCHEMA_PATH = "schema.sql"

def main():
    print("--- Starting Asana Simulation ---")
    
    # 1. Initialize Database
    db = DatabaseManager(DB_PATH, SCHEMA_PATH)
    db.connect()
    # Always start fresh for the assignment
    if os.path.exists(DB_PATH):
        db.init_schema()

    # 2. Run Generators
    # A. Workspace
    ws_id = projects.generate_workspace(db.cursor)
    
    # B. Users
    user_ids = users.generate_users(db.cursor, ws_id, count=100)
    
    # C. Teams & Projects
    team_ids = projects.generate_teams(db.cursor, ws_id)
    project_data = projects.generate_projects(db.cursor, team_ids)
    
    # D. Tasks
    tasks.generate_tasks(db.cursor, project_data, user_ids)

    # 3. Finish
    db.commit()
    db.close()
    print(f"\n[SUCCESS] Simulation Complete. Database at: {DB_PATH}")

if __name__ == "__main__":
    main()