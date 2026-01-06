import random
from faker import Faker
from src.utils.helpers import get_uuid, random_date, get_completion_status

fake = Faker()

def _get_task_name_heuristic(team_name):
    """Simulates LLM generation using templates based on department."""
    if "Engineering" in team_name:
        verbs = ["Fix", "Refactor", "Implement", "Test", "Deploy"]
        nouns = ["API Endpoint", "Login Flow", "DB Schema", "Cache"]
        return f"{random.choice(verbs)}: {random.choice(nouns)}"
    elif "Marketing" in team_name:
        verbs = ["Draft", "Review", "Publish", "Design"]
        nouns = ["Blog Post", "Social Ad", "Email Campaign", "Case Study"]
        return f"{random.choice(verbs)} - {random.choice(nouns)}"
    else:
        return fake.bs().title()

def generate_tasks(cursor, project_data, user_ids):
    print("Generating Tasks (Heavy workload)...")
    
    for pid, team_name in project_data:
        # Get sections for this project
        cursor.execute("SELECT section_id FROM sections WHERE project_id = ?", (pid,))
        sections = [row[0] for row in cursor.fetchall()]
        
        # Create 10-20 tasks per project
        for _ in range(random.randint(10, 20)):
            tid = get_uuid()
            sid = random.choice(sections)
            assignee = random.choice(user_ids) if random.random() > 0.1 else None
            
            name = _get_task_name_heuristic(team_name)
            desc = fake.paragraph()
            created = random_date(start_days_ago=100, end_days_ahead=0)
            due = random_date()
            completed = get_completion_status(created)
            
            cursor.execute("""
                INSERT INTO tasks (task_id, project_id, section_id, assignee_id, name, description, due_date, completed, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (tid, pid, sid, assignee, name, desc, due, completed, created))
            
            # 15% Chance of Subtask
            if random.random() < 0.15:
                sub_id = get_uuid()
                cursor.execute("""
                    INSERT INTO tasks (task_id, parent_task_id, name, created_at)
                    VALUES (?, ?, ?, ?)
                """, (sub_id, tid, f"Subtask: {name}", created))