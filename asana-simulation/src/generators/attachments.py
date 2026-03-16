import random
from src.utils.helpers import get_uuid, random_date

# Realistic file types that can be attached to Asana tasks, including PDFs
FILE_TYPES = [
    {"ext": "pdf",  "mime": "application/pdf",          "weight": 40},
    {"ext": "png",  "mime": "image/png",                "weight": 20},
    {"ext": "jpg",  "mime": "image/jpeg",               "weight": 15},
    {"ext": "docx", "mime": "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "weight": 10},
    {"ext": "xlsx", "mime": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",       "weight": 8},
    {"ext": "mp4",  "mime": "video/mp4",                "weight": 4},
    {"ext": "zip",  "mime": "application/zip",          "weight": 3},
]

_WEIGHTS = [f["weight"] for f in FILE_TYPES]

# Realistic file-name stems per extension
_NAMES = {
    "pdf":  ["Brief", "Report", "Spec", "Design_Doc", "Requirements", "Invoice", "Contract", "Proposal"],
    "png":  ["Screenshot", "Mockup", "Diagram", "Logo", "Banner"],
    "jpg":  ["Photo", "Reference", "Asset", "Cover"],
    "docx": ["Notes", "Draft", "Minutes", "Outline"],
    "xlsx": ["Budget", "Tracker", "Metrics", "Roadmap"],
    "mp4":  ["Demo", "Walkthrough", "Recording"],
    "zip":  ["Assets", "Exports", "Archive"],
}


def _random_file(ext: str) -> tuple[str, int]:
    """Return (file_name, size_kb) for the given extension."""
    stem = random.choice(_NAMES[ext])
    version = random.randint(1, 5)
    file_name = f"{stem}_v{version}.{ext}"
    # Plausible size ranges per type (KB)
    size_ranges = {
        "pdf":  (50,  5000),
        "png":  (20,  2000),
        "jpg":  (30,  3000),
        "docx": (10,  500),
        "xlsx": (10,  300),
        "mp4":  (5000, 50000),
        "zip":  (100, 20000),
    }
    lo, hi = size_ranges[ext]
    return file_name, random.randint(lo, hi)


def generate_attachments(cursor, user_ids: list[str]):
    """Attach files (including PDFs) to a random subset of tasks.

    Approximately 30% of tasks receive 1-3 attachments.
    """
    print("Generating Attachments (including PDFs)...")

    cursor.execute("SELECT task_id, created_at FROM tasks WHERE project_id IS NOT NULL")
    tasks = cursor.fetchall()

    attachment_count = 0
    for task_id, created_at in tasks:
        if random.random() > 0.30:
            continue  # skip ~70% of tasks

        num_attachments = random.randint(1, 3)
        for _ in range(num_attachments):
            chosen = random.choices(FILE_TYPES, weights=_WEIGHTS, k=1)[0]
            ext = chosen["ext"]
            file_name, size_kb = _random_file(ext)
            uploader = random.choice(user_ids)
            att_id = get_uuid()

            cursor.execute(
                """
                INSERT INTO attachments
                    (attachment_id, task_id, uploaded_by, file_name, file_type, file_size_kb, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (att_id, task_id, uploader, file_name, ext, size_kb, created_at),
            )
            attachment_count += 1

    print(f"  Created {attachment_count} attachments across tasks.")
