#!/usr/bin/env python

import sys

current_language = None
language_count = 0

# Read input from standard input
for line in sys.stdin:
    try:
        language, count = line.strip().split('\t', 1)
        count = int(count)

        if current_language == language:
            language_count += count
        else:
            if current_language:
                # Emit language and count
                print(f"{current_language}\t{language_count}")
            current_language = language
            language_count = count

    except ValueError:
        # Handle input format errors
        continue

# Don't forget to emit the last language
if current_language:
    print(f"{current_language}\t{language_count}")
