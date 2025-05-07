import json
import requests
from bs4 import BeautifulSoup

class PoggitAPI:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = 'https://poggit.pmmp.io'
        self.common_headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
            "Origin": self.base_url,
            "Referer": f"{self.base_url}/ci/recent",
        }
        self.csrf_token = None
    
    def _get_csrf_token(self):
        try:
            csrf_response = self.session.post(f'{self.base_url}/csrf/csrf--search.ajax', headers=self.common_headers)
            csrf_response.raise_for_status()
            self.csrf_token = csrf_response.text.strip()
        except:
            pass
    
    def get_dev_builds_by_name(self, search_term):
        if not self.csrf_token:
            self._get_csrf_token()

        if not self.csrf_token:
            return {"error": "failed to retrieve CSRF token from poggit."}

        try:
            search_response = self.session.post(f'{self.base_url}/search.ajax', headers={**self.common_headers, "X-Poggit-Csrf": self.csrf_token}, data={"search": search_term})
            search_response.raise_for_status()
            results_json = search_response.json()
        except:
            return {"error": "search request failed."}

        soup = BeautifulSoup(results_json.get("html", ""), "html.parser")
        plugins = []

        for info in soup.select(".search-info"):
            link_tag = info.select_one("a")
            remark_tag = info.select_one(".remark")
            lines = list(remark_tag.stripped_strings)

            plugins.append({
                "name": link_tag.text.strip(),
                "link": self.base_url + link_tag["href"],
                "author": lines[0].split('by ')[1] if len(lines) > 0 else "",
                "type": lines[1].replace("Type: ", "").strip() if len(lines) > 1 else ""
            })

        return json.dumps(plugins, indent=4) if plugins else {"message": "No plugins found."}
    
if __name__ == "__main__":
    poggit = PoggitAPI()
    plugins = poggit.get_dev_builds_by_name('easy')
    print(plugins)
