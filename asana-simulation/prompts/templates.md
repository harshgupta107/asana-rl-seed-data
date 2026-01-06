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

## 3. User Role Distribution

- **Admins (5%):** Full access privileges.
- **Members (90%):** Standard access.
- **Guests (5%):** Limited access (simulating external contractors).
