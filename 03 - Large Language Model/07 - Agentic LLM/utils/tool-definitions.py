# utils/tool_definitions.py
"""
Complete tool JSON schemas mirroring Claude Code's 40+ tool registry.

Claude Code's tools live in src/tools/ with one file per tool.
Each tool has:
  - A JSON schema (name, description, input_schema) sent to the LLM
  - A handler function executed locally
  - Permission metadata (which modes allow it)

This file contains the SCHEMAS only (what the LLM sees).
Handler implementations are in the main notebook for core tools;
the remaining tools here serve as a reference for extending the agent.

Tool categories:
  CORE        — BashTool, FileReadTool, FileWriteTool, FileEditTool
  SEARCH      — GlobTool, GrepTool, ToolSearchTool
  WEB         — WebFetchTool, WebSearchTool
  AGENT       — AgentTool (subagent spawning)
  PLANNING    — TodoWriteTool, TodoReadTool
  SYSTEM      — ConfigTool, StatusTool, ExitTool
  KNOWLEDGE   — SkillTool (on-demand knowledge loading)
  ADVANCED    — NotebookTool, REPLTool, MCPTool
  TEAMS       — TeamTool, TaskTool (multi-agent coordination)

Ref: Claude Code source — src/tools/*.ts (leaked March 31, 2026)
"""

# =============================================================================
# CORE TOOLS
# =============================================================================

BASH_TOOL = {
    "name": "bash",
    "description": (
        "Execute a shell command in the project's working directory. "
        "Use this for: running code, git operations, package management, "
        "file system operations, and any system command. "
        "The shell session persists across calls (cd changes stick). "
        "Commands run with the user's permissions. "
        "Long-running commands should be backgrounded with &."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "command": {
                "type": "string",
                "description": "The shell command to execute."
            },
            "timeout": {
                "type": "integer",
                "description": "Timeout in seconds. Default: 30. Use higher for builds.",
                "default": 30
            },
        },
        "required": ["command"],
    },
}

FILE_READ_TOOL = {
    "name": "file_read",
    "description": (
        "Read a file's contents. Supports reading specific line ranges. "
        "For large files, read specific sections rather than the whole file. "
        "Binary files will return a descriptive message instead of raw bytes."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "Absolute or relative path to the file."
            },
            "start_line": {
                "type": "integer",
                "description": "First line to read (1-indexed). Omit to start from beginning."
            },
            "end_line": {
                "type": "integer",
                "description": "Last line to read (inclusive). Omit to read to end."
            },
        },
        "required": ["file_path"],
    },
}

FILE_WRITE_TOOL = {
    "name": "file_write",
    "description": (
        "Create or overwrite a file with the given content. "
        "Parent directories are created automatically. "
        "For surgical edits to existing files, prefer file_edit instead."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "Path to the file to write."
            },
            "content": {
                "type": "string",
                "description": "Complete file content to write."
            },
        },
        "required": ["file_path", "content"],
    },
}

FILE_EDIT_TOOL = {
    "name": "file_edit",
    "description": (
        "Make a surgical edit to an existing file. Specify the exact text "
        "to find (old_text) and what to replace it with (new_text). "
        "The old_text must match EXACTLY (including whitespace). "
        "Only the FIRST occurrence is replaced. "
        "Use this instead of file_write when modifying existing files."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "Path to the file to edit."
            },
            "old_text": {
                "type": "string",
                "description": "Exact text to find in the file (must match precisely)."
            },
            "new_text": {
                "type": "string",
                "description": "Replacement text."
            },
        },
        "required": ["file_path", "old_text", "new_text"],
    },
}

# =============================================================================
# SEARCH TOOLS
# =============================================================================

GLOB_TOOL = {
    "name": "glob",
    "description": (
        "Find files matching a glob pattern. Supports ** for recursive matching. "
        "Examples: '**/*.py', 'src/**/*.ts', '*.json'. "
        "Use this to discover codebase structure before reading files."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "pattern": {
                "type": "string",
                "description": "Glob pattern (e.g. '**/*.py')."
            },
            "path": {
                "type": "string",
                "description": "Base directory to search from (default: project root).",
                "default": "."
            },
        },
        "required": ["pattern"],
    },
}

GREP_TOOL = {
    "name": "grep",
    "description": (
        "Search for a text pattern across files (like ripgrep). "
        "Returns matching lines with file paths and line numbers. "
        "Supports regex patterns. Use to find definitions, usages, etc."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "pattern": {
                "type": "string",
                "description": "Regex pattern to search for."
            },
            "path": {
                "type": "string",
                "description": "Directory to search in (default: project root).",
                "default": "."
            },
            "include": {
                "type": "string",
                "description": "File glob filter (e.g. '*.py' to only search Python files)."
            },
        },
        "required": ["pattern"],
    },
}

TOOL_SEARCH_TOOL = {
    "name": "tool_search",
    "description": (
        "Search the available tools by keyword. Use when you're unsure "
        "which tool to use for a task."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "What you're trying to do (e.g. 'search for text in files')."
            },
        },
        "required": ["query"],
    },
}

# =============================================================================
# WEB TOOLS
# =============================================================================

WEB_FETCH_TOOL = {
    "name": "web_fetch",
    "description": (
        "Fetch the contents of a URL. Returns the page text (HTML stripped). "
        "Use for reading documentation, API references, etc. "
        "Does NOT support authenticated pages or JavaScript-rendered content."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The URL to fetch."
            },
        },
        "required": ["url"],
    },
}

WEB_SEARCH_TOOL = {
    "name": "web_search",
    "description": (
        "Search the web for information. Returns top results with titles, "
        "URLs, and snippets. Use for finding documentation, solutions, etc."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query."
            },
        },
        "required": ["query"],
    },
}

# =============================================================================
# AGENT / DELEGATION TOOLS
# =============================================================================

AGENT_TOOL = {
    "name": "agent",
    "description": (
        "Spawn a subagent to handle a focused subtask. The subagent gets "
        "a fresh, clean context and the full tool set. Use for tasks that "
        "benefit from isolated execution — like investigating a bug in "
        "one part of the codebase while you work on another. "
        "The subagent runs to completion and returns its result."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "task": {
                "type": "string",
                "description": "A clear, self-contained task description."
            },
        },
        "required": ["task"],
    },
}

# =============================================================================
# PLANNING TOOLS
# =============================================================================

TODO_WRITE_TOOL = {
    "name": "todo_write",
    "description": (
        "Manage a structured todo list for tracking subtasks. "
        "Use BEFORE starting complex work to plan your approach. "
        "Actions: add (create task), update (change status), list (show all)."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["add", "update", "list"],
                "description": "'add' to create, 'update' to change status, 'list' to show all."
            },
            "description": {
                "type": "string",
                "description": "Task description (required for 'add')."
            },
            "todo_id": {
                "type": "string",
                "description": "Task ID (required for 'update')."
            },
            "status": {
                "type": "string",
                "enum": ["pending", "in_progress", "done", "blocked"],
                "description": "New status (required for 'update')."
            },
        },
        "required": ["action"],
    },
}

TODO_READ_TOOL = {
    "name": "todo_read",
    "description": "Display the current todo list with all task statuses.",
    "input_schema": {
        "type": "object",
        "properties": {},
    },
}

# =============================================================================
# KNOWLEDGE / SKILL TOOLS
# =============================================================================

SKILL_TOOL = {
    "name": "skill",
    "description": (
        "Load a skill file (SKILL.md) for on-demand domain knowledge. "
        "Skills contain specialized instructions, API references, or "
        "patterns that are loaded ONLY when needed — not in the base prompt. "
        "This keeps the base context small and loads knowledge just-in-time. "
        "Skill files are discovered from the project's skills/ directory."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "skill_name": {
                "type": "string",
                "description": "Name of the skill to load (matches SKILL.md filename)."
            },
        },
        "required": ["skill_name"],
    },
}

# =============================================================================
# SYSTEM TOOLS
# =============================================================================

CONFIG_TOOL = {
    "name": "config",
    "description": (
        "Read or modify agent configuration. Can inspect/change: "
        "permission mode, model, tool policies, MCP servers."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["get", "set"],
            },
            "key": {"type": "string", "description": "Config key to read/write."},
            "value": {"type": "string", "description": "New value (for 'set')."},
        },
        "required": ["action", "key"],
    },
}

NOTEBOOK_TOOL = {
    "name": "notebook",
    "description": (
        "Execute Python code in a persistent Jupyter-like notebook environment. "
        "Variables persist across calls. Use for data analysis, visualization, "
        "and exploratory programming. Returns text output and any generated images."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "Python code to execute."
            },
        },
        "required": ["code"],
    },
}

# =============================================================================
# FULL REGISTRY
# =============================================================================

FULL_TOOL_REGISTRY = [
    BASH_TOOL,
    FILE_READ_TOOL,
    FILE_WRITE_TOOL,
    FILE_EDIT_TOOL,
    GLOB_TOOL,
    GREP_TOOL,
    TOOL_SEARCH_TOOL,
    WEB_FETCH_TOOL,
    WEB_SEARCH_TOOL,
    AGENT_TOOL,
    TODO_WRITE_TOOL,
    TODO_READ_TOOL,
    SKILL_TOOL,
    CONFIG_TOOL,
    NOTEBOOK_TOOL,
]

# Human-readable descriptions for documentation
TOOL_DESCRIPTIONS = {t["name"]: t["description"] for t in FULL_TOOL_REGISTRY}
