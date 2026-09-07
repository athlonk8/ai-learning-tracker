# Backlog

## Task 1

Create the Django project and learning app, then implement the Course model with migrations.

Status: Complete.

Verification: migrations applied successfully; system check found no issues; migration drift check found no changes; all 4 Django tests passed. The development server returned HTTP 200 with Django's welcome page, then was stopped.

### Goal
Provide a runnable Django foundation and persistent Course model matching spec.md.

### Acceptance Criteria
- Django project `config` and app `learning` exist.
- Course has a required title, the three specified statuses, and a completion percentage with the specified defaults.
- Model validation rejects blank titles, unsupported statuses, and percentages outside 0–100. Database constraints enforce valid statuses and percentage bounds.
- A committed initial migration creates the Course table in SQLite.
- `uv run python manage.py runserver` starts the development server.
- `uv run python manage.py test` runs meaningful model tests.
- README documents dependency installation, migrations, server startup, and tests.

### Constraints
- Use Python, Django, uv, SQLite, and Django TestCase.
- Implement no product views, forms, notes, dashboard, or admin customization.
- Keep dependencies and scaffolding minimal; commit the uv lockfile.

### Tests
- Persist and reload a course; verify defaults and string representation.
- Validate title, status, and percentage bounds, including accepted endpoints.
- Verify database constraints reject invalid status and percentage writes.
- Run migrations, system checks, migration drift check, and the full test suite.

## Task 2: Course management

Status: Planned.

### Goal
Allow adding and viewing AI courses through simple Django pages.

### Acceptance Criteria
- A course list displays saved titles and an empty state.
- A title form saves valid courses and displays validation errors.

### Constraints
- Use Django forms and templates; no editing or deletion features.
- Preserve Task 1 defaults when adding a course.

### Tests
- GET list and add pages; POST valid and blank titles; confirm persistence and errors.

## Task 3: Progress tracking

Status: Planned.

### Goal
Allow recording status and completion percentage for an existing course.

### Acceptance Criteria
- A form saves a valid status and percentage.
- Invalid values display errors without modifying stored progress.

### Constraints
- Reuse Course validation; status and percentage remain independent.
- Do not introduce scheduling or progress history.

### Tests
- Submit valid updates, invalid status, and out-of-range percentages; confirm database state.

## Task 4: Learning notes

Status: Planned.

### Goal
Allow adding and viewing short notes for each course.

### Acceptance Criteria
- Notes belong to one course and contain required text up to 1,000 characters.
- A course page lists its notes and accepts new notes.

### Constraints
- Plain text only; no attachments, editing, or deletion workflow.

### Tests
- Save and list a note; reject empty and oversized text; verify course isolation.

## Task 5: Progress dashboard

Status: Planned.

### Goal
Show all courses and their current progress at a glance.

### Acceptance Criteria
- Dashboard shows title, status, and percentage for each course.
- An empty state appears when no courses exist.

### Constraints
- Reuse Course data; no charts, aggregate analytics, or new dependencies.

### Tests
- Verify empty state and displayed values for multiple courses with different progress.
