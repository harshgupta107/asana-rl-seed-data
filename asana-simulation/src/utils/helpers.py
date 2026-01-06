import uuid
import random
from datetime import datetime, timedelta

def get_uuid():
    """Generates a unique ID similar to Asana GID."""
    return str(uuid.uuid4())

def random_date(start_days_ago=90, end_days_ahead=30):
    """Generates a random date within a window."""
    start = datetime.now() - timedelta(days=start_days_ago)
    end = datetime.now() + timedelta(days=end_days_ahead)
    return start + (end - start) * random.random()

def get_completion_status(created_at_date):
    """Heuristic: Older tasks are more likely to be completed."""
    days_old = (datetime.now() - created_at_date).days
    if days_old > 30:
        return 1 if random.random() < 0.85 else 0
    elif days_old > 7:
        return 1 if random.random() < 0.40 else 0
    else:
        return 0