import requests

def search_repos(query: str):
    """Searches GitHub for repositories matching the query."""
    try:
        url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page=3"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            results = []
            for item in data.get("items", []):
                results.append({
                    "name": item["full_name"],
                    "stars": item["stargazers_count"],
                    "description": item["description"],
                    "url": item["html_url"]
                })
            return results
        else:
            return f"Error: GitHub API returned {response.status_code}"
    except Exception as e:
        return f"Error searching GitHub: {str(e)}"