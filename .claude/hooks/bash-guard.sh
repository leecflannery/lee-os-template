#!/bin/bash
# Blocks destructive bash commands before they execute.
# PreToolUse hook on Bash — receives tool input as JSON via stdin.
#
# Setup: This hook is registered in .claude/settings.json under PreToolUse.
# It runs before every Bash tool call and can deny dangerous commands.

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Patterns that should NEVER run without explicit human approval
DANGEROUS_PATTERNS=(
  'rm -rf'
  'rm -r /'
  'git push --force'
  'git push -f'
  'git reset --hard'
  'git clean -f'
  'git checkout \.'
  'git restore \.'
  'drop table'
  'DROP TABLE'
  'truncate table'
  'TRUNCATE TABLE'
  '> /dev/'
  'mkfs\.'
  'dd if='
  ':(){:|:&};:'
)

for pattern in "${DANGEROUS_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qE "$pattern"; then
    echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"deny\",\"permissionDecisionReason\":\"BLOCKED: Destructive command detected: $pattern. Ask for confirmation before running this.\"}}"
    exit 0
  fi
done

# Allow everything else
exit 0
