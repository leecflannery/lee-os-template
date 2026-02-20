#!/bin/bash
# PostToolUse hook on Write|Edit
# When a file in /llm-context/ is modified, nudges Claude to check for ripple effects.
# Non-blocking — injects additionalContext, never blocks the edit.
#
# Setup: This hook is registered in .claude/settings.json under PostToolUse.
# It runs after every Write or Edit and reminds Claude to keep context in sync.

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty')

# Extract file path based on tool type
if [ "$TOOL_NAME" = "Write" ]; then
  FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
elif [ "$TOOL_NAME" = "Edit" ]; then
  FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
else
  exit 0
fi

# Only fire on /llm-context/ files
if echo "$FILE_PATH" | grep -q '/llm-context/'; then
  FILENAME=$(basename "$FILE_PATH")
  DIRNAME=$(dirname "$FILE_PATH" | sed 's|.*/llm-context/||')
  echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PostToolUse\",\"additionalContext\":\"CONTEXT SYNC: You just updated ${DIRNAME}/${FILENAME}. Quick check — are there other context files, people files, or tasks that should also be updated as a result of this change? If yes, update them now.\"}}"
fi

exit 0
