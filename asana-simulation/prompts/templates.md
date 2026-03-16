# Data Generation Templates & Prompts

This file contains the prompt structures and templates used to simulate LLM-generated content for the Asana dataset.

## 1. Task Name Generation Strategy

### Context: Engineering

**System Prompt:** You are a Technical Project Manager. Generate a realistic engineering task name.
**Template Pattern:** `[Verb] [Component] [Issue/Feature]`
**Examples:**

- "Refactor API Authentication flow"
- "Fix 500 Error on Login page"
- "Implement Redis Caching for search"

### Context: Marketing

**System Prompt:** You are a Marketing Lead. Create a task name for a creative deliverable.
**Template Pattern:** `[Channel] - [Content Type] - [Topic]`
**Examples:**

- "LinkedIn - Carousel - Q3 Product Launch"
- "Email - Newsletter - October Update"
- "Blog - Draft - Case Study for Client X"

## 2. Task Description Logic

**Prompt:**
"Generate a rich-text description for a [Department] task regarding [Task Name]. Include bullet points for acceptance criteria."

**Heuristic Implementation in Code:**

- **Short Descriptions (30%):** 1-2 sentences summarizing the goal.
- **Detailed Descriptions (50%):** Includes "Context", "Requirements", and "Acceptance Criteria" bullet points.
- **Empty (20%):** Simulates quick, on-the-fly task creation.

## 4. Attachment Generation Strategy

Asana tasks support file attachments. The simulation generates realistic attachments
with the following distribution:

| File Type | Extension | Probability |
|-----------|-----------|-------------|
| PDF       | .pdf      | ~40%        |
| PNG image | .png      | ~20%        |
| JPEG image| .jpg      | ~15%        |
| Word doc  | .docx     | ~10%        |
| Excel     | .xlsx     | ~8%         |
| Video     | .mp4      | ~4%         |
| Archive   | .zip      | ~3%         |

- **Coverage:** ~30% of project tasks receive 1-3 attachments.
- **Uploader:** A random workspace member is chosen as the uploader.
- **File size:** Sampled from a realistic per-type range (KB).
- **Yes, PDFs are fully supported** as the most common attachment type in the simulation.

