import json

import requests

url = "https://linkedin-data-scraper.p.rapidapi.com/company_jobs"

headers = {
    "Content-Type": "application/json",
    "x-rapidapi-host": "linkedin-data-scraper.p.rapidapi.com",
    "x-rapidapi-key": "0443d83d4dmsh92e89bd423ce76fp1d2d1bjsn6c17c89f24d4",
}

payload = {"company_url": "http://www.linkedin.com/company/google", "count": 100}

try:
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        jobs = response.json()
        with open("company_jobs.json", "w") as f:
            json.dump(jobs, f, indent=4)
        print("Data stored in company_jobs.json successfully")
    else:
        print(f"Request failed with status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
