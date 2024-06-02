import csv
import time
from geopy.geocoders import Nominatim
from io import StringIO

# funkce pro získání názvu ulice ze zadaných souřadnic
def get_address(latitude, longitude):
    geolocator = Nominatim(user_agent="kavarny")
    location = geolocator.reverse((latitude, longitude), language="en")

    if location and location.address:
        address_components = location.raw.get("address", {})
        
        return address_components

with open('Google_maps_all.csv', 'r', encoding='utf-8') as inputfile:
    kavarny = inputfile.read().splitlines()

# vytvořím si novou tabulku
for podnik in kavarny[1:9000]:
    kavarna = csv.reader(StringIO(podnik))
    kavarna_split = next(kavarna)
    latitude = kavarna_split[3]   
    longitude = kavarna_split[4]
    kavarna_adresa = get_address(latitude, longitude)
    ulice = kavarna_adresa.get("road", None)
    cislo_popisne = kavarna_adresa.get("house_number", None)
    psc = kavarna_adresa.get("postcode", None)
    city = kavarna_adresa.get("city", None)
    okres = kavarna_adresa.get("municipality", None)
    okres_kod = kavarna_adresa.get("ISO3166-2-lvl7")
    suburb = kavarna_adresa.get("suburb", None)
    kraj = kavarna_adresa.get("county", None)
    region = kavarna_adresa.get("state_district")
    
# {'house_number': '225/3', 'road': 'Univerzitní', 'neighbourhood': 'Envelopa', 'suburb': 'Olomouc-město', 'city': 'Olomouc', 'municipality': 'okres Olomouc', 'ISO3166-2-lvl7': 'CZ-712', 'county': 'Olomouc Region', 'ISO3166-2-lvl6': 'CZ-71', 'state': 'Central Moravia', 'postcode': '779 00', 'country': 'Czechia', 'country_code': 'cz'}
    novy_zaznam = [kavarna_split[0], kavarna_split[7], latitude, longitude, ulice, cislo_popisne, psc, mesto, okres, okres_kod, predmesti, kraj, region, kavarna_split[8]]

    with open('google_maps.csv', mode='a', encoding= 'UTF-8', newline='') as output_file:
            csv_zapis = csv.writer(output_file)
            csv_zapis.writerow(novy_zaznam)
    time.sleep(1) # Časová prodleva pro odesílání requestu na server nominatim





