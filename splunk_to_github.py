import splunklib.client as client
import os
import git

# Splunk connection details
SPLUNK_HOST = "localhost"
SPLUNK_PORT = 8089
SPLUNK_USERNAME = "admin"
SPLUNK_PASSWORD = "your_password"

# GitHub repository details
REPO_PATH = "/Users/ajayiabayomi/splunk-monitoring/splunk-infrastructure-monitoring"
GIT_REMOTE = "origin"
GIT_BRANCH = "main"

# Splunk search query
SEARCH_QUERY = "search index=main source='train_SS.csv'"

# Output file
OUTPUT_FILE = os.path.join(REPO_PATH, "exported_data.csv")

# Connect to Splunk
try:
    service = client.connect(
        host=SPLUNK_HOST,
        port=SPLUNK_PORT,
        username=SPLUNK_USERNAME,
        password=SPLUNK_PASSWORD
    )
    print("Connected to Splunk.")
except Exception as e:
    print(f"Failed to connect to Splunk: {e}")
    exit(1)

# Run the search query
try:
    job = service.jobs.create(SEARCH_QUERY)
    print("Search query executed.")
except Exception as e:
    print(f"Failed to run search query: {e}")
    exit(1)

# Export results to a file
try:
    with open(OUTPUT_FILE, "w") as f:
        for result in job.results():
            f.write(result)
    print(f"Data exported to {OUTPUT_FILE}.")
except Exception as e:
    print(f"Failed to export data: {e}")
    exit(1)

# Commit and push to GitHub
try:
    repo = git.Repo(REPO_PATH)
    repo.git.add(OUTPUT_FILE)
    repo.git.commit("-m", "Automated commit: Exported data from Splunk")
    repo.git.push(GIT_REMOTE, GIT_BRANCH)
    print("Changes committed and pushed to GitHub.")
except Exception as e:
    print(f"Failed to commit/push to GitHub: {e}")
    exit(1)