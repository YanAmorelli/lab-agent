# Github MCP

## Available Tooling

### Repository Management
- `create_repository`
- `create_or_update_file`
- `get_file_contents`
- `push_files`

### Branch Management
- `list_branches`
- `create_branch`

### Pull Requests
- `pull_request_read`
- `pull_request_review_write`
- `update_pull_request`

### GitHub Actions
- `actions_get`
- `actions_list`
- `actions_run_trigger`
- `get_job_logs`

**Mandatory Rules**
- `create_repository` must always use `private = true` and `autoInit = true`
- Never commit to `main` or `dev`
- Always create a working branch
- Always finish with a Pull Request

---

## Workflow

### Commit file

- Push single files per time using:
- `create_or_update_file` (preferred for atomic function calls)
- Use a clear, descriptive commit message  

---

### Pull Request & Validation

- The PR description must be written in brazilian portuguese and include:
  - Description
  - Reason
  - Change Benefits
  - Files Changed


---

## How to Use the GitHub Tools
1. `create_repository`

ALWAYS `autoInit` and `private` as true.

```json
{
    "organization": "Organization to create the repository",
    "name": "eva-<product-name>-tf",
    "description": "Repository description",
    "autoInit": true,
    "private": true
}
```

2. `create_branch`
### Purpose

Creates an isolated working branch so you **never commit directly** to `main` or `dev`.

### Parameters
```json
{
  "owner": "<owner>",
  "repo": "<repo>",
  "branch": "<branch>",
  "from_branch": "<base_branch>"
}
```

### Best Practices

- Use semantic branch names:
    - `fix/<fix-made>`
    - `feat/<feat-made>`

- Always create the branch before pushing files
- `from_branch` defaults to the repository default if omitted

3. `create_or_update_file` 

Create or update file.

```json
{
    "owner": "<owner>",
    "repo": "<repo>",
    "branch": "<branch>",
    "message": "<message>",
    "path": "<Path where to create/update the file>",
    "sha": "<The blob SHA of the file being replaced. If you are creating do not fill this field>",
    "content": "<code>"
}
```

4. `push_files`

### Purpose

Atomically pushes all files in a single commit.

### Parameters
```json
{
    "owner": "<owner>",
    "repo": "<repo>",
    "branch": "<branch>",
    "message": "<message>",
    "files": [
        {
        "path": "<file>",
        "content": "<code>"
        }
    ]
}
```

### Best Practices

- Always push to the working branch
- Ensure file paths match repository structure
- Prefer `create_or_update_file` calls for atomic function calls to avoid hallucinations

## Typical Tool Flow
create_branch
   ↓
create_or_update_file multiple times
   ↓
pull_request_review_write

This ensures:
- Clean history
- Safe reviews
- No accidental production commits
