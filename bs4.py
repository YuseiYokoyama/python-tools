import requests
from cachecontrol import CacheControl
from cachecontrol.caches import FileCache
from bs4 import BeautifulSoup

url = "https://hrmos.co/pages/pkshatech/jobs"
def get_text(url):
    session = requests.Session()
    cached_session = CacheControl(session, cache=FileCache(".webcache"))
    response = cached_session.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    tag_title = soup.find(class_="sg-corporate-name")
    tag_body = soup.find("article", class_="pg-body")
    text = tag_title.text + "\n" + tag_body.text
    return tag_title.text, text


