import requests
from bs4 import BeautifulSoup

def get_ips_from_udger():
    url = "https://udger.com/resources/ip-list/tor_exit_node"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', id='iptab')

    if table is None:
        print("Failed to find the IP table.")
        return []

    ips = []
    rows = table.find_all('tr')

    for row in rows[1:]:  # Skip the header row
        cells = row.find_all('td')
        if len(cells) > 1:
            ip = cells[1].text.strip()
            ips.append(ip)

    return ips

def get_ips_from_danmeuk():
    url = "https://www.dan.me.uk/torlist/?exit"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []
    
    # The content is a plain text list of IPs, so we can split by newline character
    ips = response.text.strip().split('\n')
    return ips

def get_external_tor_ips():
    ips_from_udger = get_ips_from_udger()
    ips_from_danmeuk = get_ips_from_danmeuk()
    """
    curl 'https://www.dan.me.uk/torlist/?exit' 
    this site has rate limiting 
    Umm... You can only fetch the data every 30 minutes - sorry.  It's pointless any faster as I only update every 30 minutes anyway.
    If you keep trying to download this list too often, you may get blocked from accessing it completely.
    (this is due to some people trying to download this list every minute!)
    """
    
    # Combining the two IP lists and removing duplicates by converting the list to a set
    all_ips = set(ips_from_udger + ips_from_danmeuk)
    # all_ips = set(ips_from_danmeuk)

    # all_ips = set(ips_from_udger)
    return list(all_ips)

def main():
    all_ips = get_external_tor_ips()

    print("All IPs:")
    for ip in all_ips:
        print(ip)

if __name__ == "__main__":
    main()
