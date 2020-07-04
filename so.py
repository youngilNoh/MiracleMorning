import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find_all("a", {"class":"s-pagination--item"})
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)

def extract_job(html):
  title = html.find("h2").find("a",{"class":"stretched-link"})["title"]
  company = html.find("h3").find("span").get_text(strip=True)
  location = html.find("h3").find("span",{"class":"fc-black-500"}).get_text(strip=True)
  print(location)
  return {
    'title': title,
    'company': company,
    'location': location
  }

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div",{"class":"-job"})
    for result in results:
      job = extract_job(result.find("div",{"class":"grid--cell fl1"}))
      # jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs