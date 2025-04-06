import requests
import socket

def get_local_ip():
    """Get the local IP address of the device."""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        return f"Error getting local IP: {e}"

def get_public_ip():
    """Get the public IP address and details using an external API."""
    try:
        response = requests.get("https://ipinfo.io/json")  # Uses IPInfo API
        data = response.json()
        return data
    except Exception as e:
        return f"Error getting public IP: {e}"

# Get device IP details
local_ip = get_local_ip()
public_ip_data = get_public_ip()

# Display IP information
print(f"Local IP: {local_ip}")
if isinstance(public_ip_data, dict):
    print(f"🌎 Public IP: {public_ip_data.get('ip', 'N/A')}")
    print(f"📍 Location: {public_ip_data.get('city', 'Unknown')}, {public_ip_data.get('region', 'Unknown')}, {public_ip_data.get('country', 'Unknown')}")
    print(f"🏢 ISP: {public_ip_data.get('org', 'Unknown')}")
    print(f"📡 Latitude/Longitude: {public_ip_data.get('loc', 'Unknown')}")
else:
    print(public_ip_data)
