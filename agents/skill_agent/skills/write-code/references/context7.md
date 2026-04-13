# Workflow

## 1. Search for the library

Use the adk tool `resolve_library_id` to get the library documentation ID.

Returns library metadata including the `id` field needed for step 2.

## 2. Fetch documentation context

Use the adk tool `get_library_docs` to get the library context

## When to Use

- Before implementing any library-dependent feature
- When unsure about current API signatures
- For library version-specific behavior
- To verify best practices and patterns