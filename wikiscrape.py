import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

all_pages = set()
start_page = None

# if True:
while start_page not in all_pages:
    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "allpages",
        "apfrom": start_page,
        "aplimit": 500
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    PAGES = DATA["query"]["allpages"]

    for i, page in enumerate(PAGES):
        title = page["title"]

        # Is it the last page? Ignore it this time around, and start on it next
        if i == len(PAGES) - 1:
            start_page = title

        # It's not the last page (and the title isn't in the set already); output it, and add it to all_pages
        elif title not in all_pages:
            print(title)
            all_pages.add(title)

    # We reached the end (probably???)
    if len(PAGES) <= 1:
        break