# AI Learning Tracker

A small personal learning tracker for DataTalksClub AI Dev Tools Zoomcamp 2026 Homework 1. The AI-native workflow is: agree on a specification, break it into verifiable tasks, implement one task, and report actual checks.

## Exactly four product features

1. **Course management:** add and view AI courses.
2. **Progress tracking:** record course status and completion percentage.
3. **Learning notes:** add short notes for each course.
4. **Progress dashboard:** show courses and their current progress.

## Data and behavior

- Course: required title (maximum 200 characters), status (`not_started`, `in_progress`, or `completed`; default `not_started`), and integer completion percentage (0 through 100 inclusive; default 0).
- Status and percentage are recorded independently; no automatic synchronization is required.
- Duplicate course titles are allowed.
- Later, each course can have multiple short notes, each with required text up to 1,000 characters.
- The future dashboard lists each course's title, status, and completion percentage, with an empty state when no courses exist.

## Scope and technology

Use Python, Django, uv, SQLite, and Django's built-in test framework. This is a local, single-user homework project. Authentication, AI APIs, deployment, external services, deletion, and advanced analytics are outside scope.

Implement only backlog Task 1 in this iteration: project scaffolding, Course model, migration, and model tests. Product pages, forms, notes, and dashboard remain planned. Django's development welcome page is sufficient for this iteration.
