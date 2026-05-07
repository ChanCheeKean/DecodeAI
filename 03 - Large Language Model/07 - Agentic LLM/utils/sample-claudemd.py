# utils/sample_claudemd.py
"""
Example CLAUDE.md and MEMORY.md content for reference and testing.

CLAUDE.md is the primary mechanism for giving the agent project-specific
instructions. It works like a README but for the AI — telling it about
your project's conventions, architecture, and preferences.

MEMORY.md is the agent's self-maintained index of what it has learned
about the project. The model creates and updates this file itself.

In Claude Code's hierarchy:
  ~/.claude/CLAUDE.md          → user-global preferences (your personal style)
  ~/project/CLAUDE.md          → project-level instructions (team conventions)
  ~/project/subdir/CLAUDE.md   → directory-level overrides (module-specific)

Each level is discovered and merged into the system prompt at startup.
More specific files override more general ones.
"""

# =============================================================================
# SAMPLE CLAUDE.md — PROJECT LEVEL
# =============================================================================

SAMPLE_CLAUDE_MD = """# CLAUDE.md — Project Instructions

## Project Overview
This is a Python web API built with FastAPI. The project follows a clean
architecture pattern with separate layers for routing, service logic,
and data access.

## Architecture
- `src/api/` — FastAPI route handlers (thin controllers)
- `src/services/` — Business logic (pure functions where possible)
- `src/models/` — Pydantic models for request/response schemas
- `src/db/` — Database access layer (SQLAlchemy + async)
- `tests/` — Pytest test suite (mirrors src/ structure)

## Code Conventions
- Python 3.11+, type hints on all function signatures
- Use `ruff` for linting (config in pyproject.toml)
- Async everywhere — all route handlers and DB calls are async
- Error handling: raise HTTPException with appropriate status codes
- Logging: use structlog, not print()

## Testing
- Run tests: `pytest tests/ -v`
- Run with coverage: `pytest --cov=src tests/`
- All new features must have tests before merging
- Use factory_boy for test data generation

## Git Conventions
- Branch naming: `feature/xxx`, `fix/xxx`, `refactor/xxx`
- Commit messages: conventional commits (feat:, fix:, docs:, etc.)
- Always rebase on main before creating a PR
- Never push directly to main

## Common Pitfalls
- The database uses UTC timestamps everywhere. Don't use naive datetimes.
- Authentication middleware expects a Bearer token in the Authorization header.
- Rate limiting is per-user, configured in src/middleware/rate_limit.py.
- The CI pipeline runs ruff + pytest + mypy. All three must pass.

## Environment
- Python 3.11.8 (managed with pyenv)
- PostgreSQL 16 (Docker: `docker compose up -d db`)
- Redis for caching (Docker: `docker compose up -d redis`)
- `.env.example` has all required environment variables
"""

# =============================================================================
# SAMPLE CLAUDE.md — USER GLOBAL (personal preferences)
# =============================================================================

SAMPLE_GLOBAL_CLAUDE_MD = """# CLAUDE.md — Personal Preferences (global)

## My Preferences
- I prefer concise responses — don't over-explain obvious things
- Always use type hints in Python
- Use early returns instead of deeply nested if/else
- Prefer composition over inheritance
- I use vim keybindings, so references to editor shortcuts should use vim

## My Common Commands
- Run project: `make dev`
- Run tests: `make test`
- Format code: `make fmt`
- Deploy: `make deploy-staging`

## Things I Don't Want
- Don't add comments that just restate the code
- Don't add try/except blocks that silently swallow errors
- Don't suggest using global variables
- Don't refactor code I didn't ask you to change
"""

# =============================================================================
# SAMPLE MEMORY.md
# =============================================================================
# This is what the MEMORY.md file looks like after the agent has been
# working on a project for a while. Each line is a ~150 char pointer
# to where detailed information lives.

SAMPLE_MEMORY_MD = """# Agent Memory Index
# Auto-maintained — one pointer per line

- Auth: JWT-based with refresh tokens, implementation in src/auth/jwt.py, config in src/auth/config.py
- DB: PostgreSQL 16, async with SQLAlchemy 2.0, migrations in alembic/versions/
- API versioning: /api/v1/ prefix, defined in src/api/router.py
- User model: src/models/user.py, has email uniqueness constraint + soft delete
- Rate limiting: per-user, 100 req/min, configured in src/middleware/rate_limit.py
- Test fixtures: shared fixtures in tests/conftest.py, factory in tests/factories/
- CI: GitHub Actions, runs ruff+pytest+mypy, config in .github/workflows/ci.yml
- Deployment: Docker-based, Dockerfile at root, compose for local dev
- Known issue: the search endpoint (GET /api/v1/search) is slow for >10k results, needs pagination
- Recent change (2026-03-28): migrated from Pydantic v1 to v2, all models updated
- Background jobs: Celery + Redis, task definitions in src/tasks/
- Websocket: real-time notifications via /ws/notifications, impl in src/api/websocket.py
"""

# =============================================================================
# SAMPLE SKILL FILE (SKILL.md)
# =============================================================================
# Skills are loaded on-demand via the SkillTool. They contain specialized
# knowledge that the agent doesn't need in every session.

SAMPLE_SKILL_MD = """# SKILL.md — FastAPI Error Handling Patterns

## When to Use This Skill
Load this skill when working on error handling, middleware, or API responses.

## Standard Error Response Format
All API errors must use this JSON structure:
```json
{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Human-readable description",
        "details": [{"field": "email", "issue": "invalid format"}]
    }
}
```

## Exception Classes
```python
# src/exceptions.py
class AppError(Exception):
    def __init__(self, code: str, message: str, status: int = 400, details: list = None):
        self.code = code
        self.message = message
        self.status = status
        self.details = details or []

class NotFoundError(AppError):
    def __init__(self, resource: str, id: str):
        super().__init__("NOT_FOUND", f"{resource} {id} not found", 404)

class AuthError(AppError):
    def __init__(self, message: str = "Authentication required"):
        super().__init__("AUTH_ERROR", message, 401)
```

## Middleware Registration Order
1. CORSMiddleware (outermost)
2. RateLimitMiddleware
3. AuthMiddleware
4. ErrorHandlerMiddleware (innermost — catches all exceptions)
"""
