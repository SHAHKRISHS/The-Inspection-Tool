import requests
from termcolor import colored
from main import url

print((colored('Sub Domain Finder ', 'red')))

print("\nThis process will check all the possible subdomains from 200.\n")

f = open('subdomain.txt', 'r')
content = f.read()
subdomains = content.splitlines()

for subdomain in subdomains:
    url1 = f"http://{subdomain}.{url}"
    url2 = f"https://{subdomain}.{url}"
    try:
        requests.get(url1)
        print(f"Discovered URL: {url1}")
        requests.get(url2)
        print(f"Discovered URL: {url2}")
    except requests.ConnectionError:
        pass
        
print("\n")
