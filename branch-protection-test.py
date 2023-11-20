import requests
import os



def protect_branch(github_token, username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/branches/main/protection"

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"

    }

    data = {
        "required_status_checks": {
            "strict": True,
            "contexts": ["Python package / build"]
        },
        "enforce_admins": True,
        "required_pull_request_reviews": {
            "required_approving_review_count": 1
        },
        "restrictions": None
    }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Branch protection enabled for {repo_name}")
    else:
        print(f"Failed to enable branch protection for {repo_name}: {response.content}")
def main():
    github_token = os.getenv("GITHUB_TOKEN")
    username = "redat97"
    repo_name = "test-repo"
    protect_branch(github_token, username, repo_name)

if __name__ == "__main__":
    main()