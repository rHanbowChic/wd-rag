import re

with open("t", "r") as f:
    content = f.read()

# Extract all href values from <a href="..."> tags
pattern = re.compile(r'<a\s[^>]*href="([^"]*)"')
matches = pattern.findall(content)

# Deduplicate preserving first-seen order
seen = set()
unique = []
for link in matches:
    if link not in seen:
        seen.add(link)
        unique.append(link)

with open("o.txt", "w") as f:
    for link in unique:
        f.write(link + "\n")

print(f"Extracted {len(unique)} unique links out of {len(matches)} total.")
