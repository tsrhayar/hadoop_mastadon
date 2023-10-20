#!/usr/bin/env python

import sys
import json

# Read input from standard input
for line in sys.stdin:
    try:
        record = json.loads(line)
        language = record.get("language")

        if language:
            # Emit the language and a count of 1
            print(f"{language}\t1")

    except ValueError:
        # Handle JSON parsing errors
        continue
