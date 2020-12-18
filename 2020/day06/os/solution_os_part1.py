#!/usr/bin/env python
import re
import sys

questions_answered_count = 0
with open(sys.argv[1]) as f:
    questions_answered = set()
    for row in f:
        row = row.strip()
        if row:
            questions_answered.update({letter for letter in row})
        else:
            questions_answered_count += len(questions_answered)
            questions_answered.clear()
    questions_answered_count += len(questions_answered)
    print(questions_answered_count)
