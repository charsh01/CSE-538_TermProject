import csv
from io import StringIO

# Parse function
def parse_custom_line(line):
    parts = []
    current = ''
    inside_pipe = False
    i = 0
    while i < len(line):
        char = line[i]
        if char == '|':
            inside_pipe = not inside_pipe
            i += 1
            continue
        elif char == ',' and not inside_pipe:
            parts.append(current)
            current = ''
        else:
            current += char
        i += 1
    parts.append(current)
    return parts

# Parse the file
parsed_rows = []
with open("D:\School\CSE-538\Term Project\political data\OpenSecrets\cmtes22.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            fields = parse_custom_line(line)
            parsed_rows.append(fields)

# Convert to DataFrame
import pandas as pd
df = pd.DataFrame(parsed_rows)

# Save as csv
print(df)
df.to_csv("D:\School\CSE-538\Term Project\political data\OpenSecrets\parsed_output.csv", index=False)


