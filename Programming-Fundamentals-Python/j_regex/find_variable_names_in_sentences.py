import re

some_string = input()

pattern = r"\b_([a-zA-Z-0-9]+)\b"
matches = re.findall(pattern, some_string)

print(",".join(matches))