choice = int(input("\n Please select from the below options: \n 1. Port Scanning \n 2. Whois \n 3. SubDomain Finder \n 4. Perform all the above mentioned scan \n Enter your choice: "))
print("\n")
url = input("Enter the name of the url: ")
if choice == 1:
    import portscanner

elif choice == 2:
    import script

elif choice == 3:
    import subdomainscanner

elif choice == 4:
    import portscanner
    import script
    import subdomainscanner

else:
    print("invalid Choice")
