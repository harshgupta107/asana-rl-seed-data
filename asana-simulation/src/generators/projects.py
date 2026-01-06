from datetime import datetime
from src.utils.helpers import get_uuid
from faker import Faker

fake = Faker()

def generate_workspace(cursor):
    print("Creating Workspace...")
    ws_id = get_uuid()
    cursor.execute("INSERT INTO workspaces VALUES (?, ?, ?)", 
                   (ws_id, "TechFlow Corp", "techflow.io"))
    return ws_id

def generate_teams(cursor, workspace_id):
    print("Creating Teams...")
    teams_map = {
        "Engineering": ["Platform", "Product", "SRE"],
        "Marketing": ["Brand", "Growth"],
        "Sales": ["Enterprise"],
        "Design": ["UX Research", "UI System"]
    }
    
    team_ids = []
    for dept, subs in teams_map.items():
        for sub in subs:
            tid = get_uuid()
            name = f"{dept} - {sub}"
            cursor.execute("INSERT INTO teams VALUES (?, ?, ?)", (tid, workspace_id, name))
            team_ids.append((tid, name)) # Return ID and Name for context
    return team_ids

def generate_projects(cursor, team_ids):
    print("Creating Projects and Sections...")
    project_data = [] # List of (project_id, team_name)
    
    for tid, team_name in team_ids:
        # Create 3-5 projects per team
        for _ in range(3):
            pid = get_uuid()
            pname = f"{team_name}: {fake.catch_phrase()}"
            cursor.execute("INSERT INTO projects VALUES (?, ?, ?, ?, ?)", 
                           (pid, tid, pname, "On Track", datetime.now()))
            
            # Create Default Sections
            for sec in ["To Do", "In Progress", "Review", "Done"]:
                sid = get_uuid()
                cursor.execute("INSERT INTO sections VALUES (?, ?, ?)", (sid, pid, sec))
                
            project_data.append((pid, team_name))
            
    return project_data