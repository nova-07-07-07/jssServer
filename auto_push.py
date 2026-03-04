import subprocess
import re
import time

# Start cloudflared
import subprocess

process = subprocess.Popen(
    [r"C:\Windows\System32\cloudflared.exe", "tunnel", "--url", "http://localhost:5000"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

url = None

for line in process.stdout:
    print(line.strip())
    match = re.search(r"https://.*trycloudflare.com", line)
    if match:
        url = match.group(0)
        break

if url:
    # Update file
    with open("config.js", "w") as f:
        f.write(f'export const API_URL = "{url}";\n')

    # Git commands
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Update API URL: {url}"])
    subprocess.run(["git", "push"])

    print("Updated & pushed:", url)