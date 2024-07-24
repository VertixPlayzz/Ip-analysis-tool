# vertixplayz
# princeplayz

import ipaddress
import requests
import colorama
from colorama import Fore


print(Fore.RED + """prince(vertix)
._____________                                                                 
|   \______   \                                                                
|   ||     ___/                                                                
|   ||    |                                                                    
|___||____|                                                                    
                                                                               
     _____    _______      _____  .____    _____.___. _________.___  _________ 
    /  _  \   \      \    /  _  \ |    |   \__  |   |/   _____/|   |/   _____/ 
   /  /_\  \  /   |   \  /  /_\  \|    |    /   |   |\_____  \ |   |\_____  \  
  /    |    \/    |    \/    |    \    |___ \____   |/        \|   |/        \ 
  \____|__  /\____|__  /\____|__  /_______ \/ ______/_______  /|___/_______  / 
          \/         \/         \/        \/\/              \/             \/  
""")

def analyze_ip(ip):
    try:
        # Validate IP address format
        ip_obj = ipaddress.ip_address(ip)
        
        # Determine the type of IP address (IPv4 or IPv6)
        ip_type = "IPv4" if ip_obj.version == 4 else "IPv6"
        
        # Print basic information
        print(f"IP Address: {ip}")
        print(f"IP Type: {ip_type}")
        
        # Fetch additional information using ipinfo.io API
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data = response.json()
            print("Additional Information:")
            print(f"  City: {data.get('city')}")
            print(f"  Region: {data.get('region')}")
            print(f"  Country: {data.get('country')}")
            print(f"  Location: {data.get('loc')}")
            
            # Extract latitude and longitude
            latitude, longitude = data.get('loc', '').split(',')
            print(f"  Latitude: {latitude}")
            print(f"  Longitude: {longitude}")
            
            # Display a map (using a hypothetical function show_map)
            show_map(latitude, longitude)
            
            # Perform reverse DNS lookup
            print(f"  Reverse DNS: {requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}').text}")
            
            # Fetch ISP information
            print(f"  ISP: {data.get('org')}")  # Example using ipinfo.io's 'org' field
            
            # Fetch network information
            print(f"  Network: {data.get('network')}")
            
        else:
            print("Failed to fetch additional information.")
    
    except ValueError:
        print("Invalid IP address format.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def show_map(latitude, longitude):
    # Hypothetical function to show a map based on latitude and longitude
    # Replace with actual code to display a map using a mapping service (e.g., Google Maps API)
    print(f"Map Location: https://maps.google.com/maps?q={latitude},{longitude}")

# Example usage:
if __name__ == "__main__":
    ip_address = input("Enter an IP address to analyze: ")
    analyze_ip(ip_address)
