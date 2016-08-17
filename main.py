import re

import requests


def check_domain(domain):
    headers = {'Referer': 'https://www.ukrnames.com/domainsuggestion/generate.jsp'}
    response = requests.get(
        'https://www.ukrnames.com/domains/ajax/whois.jsp?name={domain}.com'.format(domain=domain),
        headers=headers
    )
    if 'green' in str(response.content):
        print(domain)

with open('domains.html') as f:
    content = f.read()

    domains = re.findall("""getWhois\(.*?,'(.*?)'\)""", content)

    for domain in domains:
        check_domain(domain)



