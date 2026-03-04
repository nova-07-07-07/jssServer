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

    # Update url in index.html file const serverUrl = "https://faced-perhaps-champion-mere.trycloudflare.com";

    with open("index.html", "r") as f:
        content = f.read()

    new_content = re.sub(r'const serverUrl = ".*";', f'const serverUrl = "{url}";', content)

    with open("index.html", "w") as f:
        f.write(new_content)

    # Update API_URL in config.js file export const API_URL = "https://faced-perhaps-champion-mere.trycloudflare.com";

    with open("config.js", "w") as f:
        f.write(f'export const API_URL = "{url}";\n')

    # Git commands
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Update API URL: {url}"])
    subprocess.run(["git", "push"])

    print("Updated & pushed:", url)

while True:
    time.sleep(10)