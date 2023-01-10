import requests
from page_parser import parse

if __name__ == '__main__':
    url = "https://testing-www.codefellows.org/course-calendar/?filters=400:%20Advanced,code-python-401"
    response = requests.get(url)
    results = parse(response.text)
    print(results)
