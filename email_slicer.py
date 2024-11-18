# collect email from the user
# split the email using the @, save the first part as the user name, the second part is gonna be saved as domain
# split tne domain using .,

def main():
  print("Welcome to the email slicer")
  print("")

  email_input = input("Enter your email address: ")
 
  # username: Everything before the @.
  # domain: Everything after the @.
  (username, domain) = email_input.split("@")
  
  # domain: The main domain name (e.g., "gmail").
  # extension: The top-level domain (e.g., "com").
  (domain, extension) = domain.split(".")

  print("Username : ", username)
  print("Domain : ", domain)
  print("Extension : ", extension)

while True: 
  main()