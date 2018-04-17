import shodan
import os 

def how_to():
  print("[+]Syntax: 'filter:value' ")
  print("[+]For example the following will search for apach webservers loacted in Germany")
  print("   'apache country:DE'")
  #Showing all the filters avaiable 
  print("The following filters are avaiable: ")
  print("")
  print("[+]'after' --- Only show results that were collected after the given date (dd/mm/yyyy).")
  print("[+]'asn' --- The Autonomous System Number that identifies the network the device is on.")
  print("[+]'before' --- Only show results that were collected before the given date (dd/mm/yyyy.")
  print("[+]'city' --- Show results that are located in the given city.")
  print("[+]'country' --- Show results that are located within the given country.")
  print("[+]'geo' --- There are 2 modes to the geo filter: radius and bounding box. To limit results based on a radius around a pair of latitude/ longitude, provide 3 parameters; ex: geo:50,50,100. If you want to find all results within a bounding box, supply the top left and bottom right coordinates for the region; ex: geo:10,10,50,50.")
  print("[+]'hash' --- Hash of the 'data' property")
  print("[+]'has_ipv6' --- If 'true' only show results that were discovered on IPv6.")
  print("[+]'has_screenshot' --- If 'true' only show results that have a screenshot available.")
  print("[+]'hostname' --- Search for hosts that contain the given value in their hostname.")
  print("[+]'isp --- Find devices based on the upstream owner of the IP netblock.")
  print("[+]'link' --- Find devices depending on their connection to the Internet.")
  print("[+]'net' --- Search by netblock using CIDR notation; ex: net:69.84.207.0/24")
  print("[+]'org' --- Find devices based on the owner of the IP netblock.")
  print("[+]'os' --- Filter results based on the operating system of the device.")
  print("[+]'port' --- Find devices based on the services/ ports that are publicly exposed on the Internet.")
  print("[+]'postal' --- Search by postal code.")
  print("[+]'product' --- Filter using the name of the software/ product; ex: product:Apache")
  print("[+]'state' --- Search for devices based on the state/ region they are located in.")
  print("[+]'version --- Filter the results to include only products of the given version; ex: product:apache version:1.3.37")
  print("")
  print("[+]'bitcoin.ip --- Find Bitcoin servers that had the given IP in their list of peers.")
  print("[+]'bitcoin.ip_count' --- Find Bitcoin servers that return the given number of IPs in the list of peers.")
  print("[+]'bitcoin.port --- Find Bitcoin servers that had IPs with the given port in their list of peers.")
  print("[+]'bitcoin.version' --- Filter results based on the Bitcoin protocol version.")
  print("")
  print("[+]'http.component' --- Name of web technology used on the website")
  print("[+]'http.component_category' --- Category of web components used on the website")
  print("[+]'http.html' --- Search the HTML of the website for the given value.")
  print("[+]'http.html_hash' --- Hash of the website HTML")
  print("[+]'http.status' --- Response status code")
  print("[+]'http.title' --- Search the title of the website")
  print("")
  print("[+]'ntp.ip' --- Find NTP servers that had the given IP in their monlist.")
  print("[+]'ntp.ip_count' --- Find NTP servers that return the given number of IPs in the initial monlist response.")
  print("[+]'ntp.more' --- Whether or not more IPs were available for the given NTP server.")
  print("[+]'ntp.port' --- Find NTP servers that had IPs with the given port in their monlist.")
  print("")
  print("[+]'ssl' --- Search all SSL data")
  print("[+]'ssl.alpn' --- Application layer protocols such as HTTP/2 ('h2')")
  print("[+]'ssl.chain_count' --- Number of certificates in the chain")
  print("[+]'ssl.version' --- Possible values: SSLv2, SSLv3, TLSv1, TLSv1.1, TLSv1.2")
  print("[+]'ssl.cert.alg' --- Certificate algorithm")
  print("[+]'ssl.cert.expired' --- Whether the SSL certificate is expired or not; True/ False")
  print("[+]'ssl.cert.extension' --- Names of extensions in the certificate")
  print("[+]'ssl.cert.serial' --- Serial number as an integer or hexadecimal string")
  print("[+]'ssl.cert.pubkey.bits' --- Number of bits in the public key")
  print("[+]'ssl.cert.pubkey.type' --- Public key type")
  print("[+]'ssl.cipher.version' --- SSL version of the preferred cipher")
  print("[+]'ssl.cipher.bits' --- Number of bits in the preferred cipher")
  print("[+]'ssl.cipher.name' --- Name of the preferred cipher")
  print("")
  print("[+]'telnet.option' --- Search all the options")
  print("[+]'telnet.do' --- The server requests the client to support these options")
  print("[+]'telnet.dont' --- The server requests the client to not support these options")
  print("[+]'telnet.will' --- The server supports these options")
  print("[+]'telnet.wont' --- The server doesnt support these options")
  
  
  
  
# Main Menu
def main_menu():
  SHODAN_API_KEY = raw_input("Enter your API key for shodan: ")
  api = shodan.Shodan(SHODAN_API_KEY)
  
  while True:
    print("Choose an option.")
    print("1. Help")
    print("2. Start")
    menu_choice = raw_input(">> ")
    #os.system('clear')
    if menu_choice == '1':
      how_to()
      raw_input("Press Enter to continue...")
      #os.system('clear')
    elif menu_choice == '2':
      print("Shodan Search: ")
      print("---------------")
      search_term = raw_input("Search: ")
      file_name = raw_input("Enter a file name where info will be written to: ")
      try:
        # Search Shodan
        results = api.search(search_term)
        # doc. only the IPs into .txt file 
        ip_only = open(file_name + "_ip_only.txt", "w")
        for result in results['matches']:
          print >> ip_only, ("%s") % result['ip_str']
        ip_only.close()
        # doc. full info on IPs found
        full = open(file_name + "_full_info.txt", "w")
        for result1 in results['matches']:
          print >> full, ("IP: %s") % result1['ip_str']
          print >> full, result1['data']
          print >> full, ("")
      except shodan.APIError, e:
        print("Error: %s") % e 
