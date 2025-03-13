# import socket

# def get_ip_address(website_url):
#     try:
#         ip_address = socket.gethostbyname(website_url)
#         print(f"The IP address of {website_url} is {ip_address}")
#     except socket.gaierror:
#         print(f"Unable to get the IP address for {website_url}")

# # Example usage
# website = input("Enter the website URL (without 'https://'): ")
# get_ip_address(website)    

import subprocess
def tracert(domain):
    try:
        result = subprocess.run(["tracert", domain], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("tracert command not found. Make sure it's available.")
    except Exception as e: # Catching general exceptions for now
        print(f"An error occurred: {e}")

domain = input("Enter the website or IP address: ")
tracert(domain)
