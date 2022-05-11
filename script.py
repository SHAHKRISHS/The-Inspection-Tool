import whois
from termcolor import colored
from main import url

print(colored('Whois', 'red'))
print("\n")

w = whois.whois(url)
w = w.text
print(w)
print("\n")
