import requests
import sys

CF_API_TOKEN = "mrHGylkkxMjcFAAKZK131eo53k_0bViQ0brIj9uy"
DOMAINS = ["deepblue.im", "*.deepblue.im"]
PROXIED = True

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org")
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching public IP: {e}")
        sys.exit(1)

def update_cloudflare(domain, ip):
    headers = {
        "Authorization": f"Bearer {CF_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # 1. Get Zone ID
    try:
        # Extract zone name from domain (assuming TLD+1)
        zone_name = ".".join(domain.replace("*.", "").split(".")[-2:])
        response = requests.get(f"https://api.cloudflare.com/client/v4/zones?name={zone_name}", headers=headers)
        response.raise_for_status()
        zones = response.json().get("result")
        if not zones:
            print(f"Zone not found for {domain}")
            return
        zone_id = zones[0]["id"]
        
        # 2. Get DNS Record ID
        response = requests.get(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?name={domain}", headers=headers)
        response.raise_for_status()
        records = response.json().get("result")
        if not records:
            # Create record if not exists
            print(f"Record not found for {domain}. Creating...")
            data = {
                "type": "A",
                "name": domain,
                "content": ip,
                "proxied": PROXIED
            }
            response = requests.post(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records", headers=headers, json=data)
        else:
            record_id = records[0]["id"]
            current_ip = records[0]["content"]
            
            if current_ip == ip:
                print(f"IP for {domain} is already up to date ({ip})")
                return
            
            # 3. Update Record
            print(f"Updating {domain} to {ip}")
            data = {
                "type": "A",
                "name": domain,
                "content": ip,
                "proxied": PROXIED
            }
            response = requests.put(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}", headers=headers, json=data)
        
        response.raise_for_status()
        print(f"Successfully updated {domain}")
        
    except Exception as e:
        print(f"Error updating {domain}: {e}")

if __name__ == "__main__":
    ip = get_public_ip()
    print(f"Current Public IP: {ip}")
    for domain in DOMAINS:
        update_cloudflare(domain, ip)
