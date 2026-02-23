#!/bin/bash
# PostToolUse hook on Bash|Write
# Detects when a file lands in a meeting-notes directory and nudges Claude
# to run the process-meetings skill on it.
#
# CUSTOMIZE: Update MEETING_NOTES_DIR to your meeting notes location.

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty')

# Set this to wherever you store meeting transcripts
MEETING_NOTES_DIR="meeting-notes"

if [ "$TOOL_NAME" = "Bash" ]; then
  COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

  # Check if the bash command copies or moves a file INTO meeting-notes
  if echo "$COMMAND" | grep -qE "(cp|mv|rsync).*${MEETING_NOTES_DIR}"; then
    # Try to extract the destination filename
    DEST_FILE=$(echo "$COMMAND" | grep -oE "${MEETING_NOTES_DIR}/[^ \"']*" | head -1)
    if [ -n "$DEST_FILE" ]; then
      FILENAME=$(basename "$DEST_FILE")
    else
      FILENAME="(check meeting-notes directory)"
    fi

    echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PostToolUse\",\"additionalContext\":\"NEW TRANSCRIPT DETECTED: ${FILENAME} was just added to meeting-notes. Run the process-meetings skill on this file now -- extract decisions, action items, people updates, and route context to the appropriate domain files. Read /skills/process-meetings.md for the full workflow.\"}}"
  fi

elif [ "$TOOL_NAME" = "Write" ]; then
  FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

  # Check if the file was written directly into meeting-notes
  if echo "$FILE_PATH" | grep -q "$MEETING_NOTES_DIR"; then
    FILENAME=$(basename "$FILE_PATH")
    echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PostToolUse\",\"additionalContext\":\"NEW TRANSCRIPT DETECTED: ${FILENAME} was just written to meeting-notes. Run the process-meetings skill on this file now -- extract decisions, action items, people updates, and route context to the appropriate domain files. Read /skills/process-meetings.md for the full workflow.\"}}"
  fi
fi

exit 0
