#!/bin/bash

# Check if xclip is installed
if ! command -v xclip &> /dev/null; then
    echo "Error: 'xclip' is not installed. Please install it first."
    exit 1
fi

# Check if a file path is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

file_path="$1"

# Check if the file exists
if [ ! -f "$file_path" ]; then
    echo "Error: File not found."
    exit 1
fi

# Copy the file content to the clipboard using xclip
cat "$file_path" | xclip -selection clipboard

echo "File content copied to clipboard."

