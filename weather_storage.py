from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
    
  "type": "service_account",
  "project_id": "optimum-mode-382118",
  "private_key_id": "7174d61ba1679e58a85684784aeaf8c9251504c6",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCzSZLNeWw41+Eh\nF6Hws8IZroIpeW1drcA2LZY8Vl7AJ0s0OnEk3CM51vtCcma3JzCNloXVgCUiJHww\n+80E+vmlPzNKPc40N+6unDbAmNM7A8+l3Wa1yi9Y1kx+PCmCqJ90Vmk1pRHNqEeg\n9bCULJU/2lMwnMKE+aDeG5Xxc1RWNnMmaoUCTdJKktbOY9avI39VDDxC1JUcTmIy\nAUb0pBYGlOXG5YtH+oPPS3TK0c4DuZit50igwqcl7YvoqIuiTsFQnTDDqZuje9vB\nxQWaO0oVEgBCvEsObDnOzpZ0pwwXpBKtH0DiJlnn1yueGRHqkhJcRt+dkmhiXl0Y\nwWmJcctFAgMBAAECggEABWFRKnauV2EDEdR9DkAWtGFBlAUKJyQuVHHhxEXDP3ju\nZM7W07MCIPDhRrPa0+bf1MqOPENFhKobn/dZG6vRuge/fkbZ3USga6pRv6Mrvjr1\ntussnd/yCR8ahInsT6NycDH3o53PKaDB0C658c20sjSBspUXBpkxyU3X82Wb7kpU\ndh5U32QyrIbaTLaIzntcI9T6vGgwSsriA0v+BrgD5/GVrgX8q0QZDgey2djWngFW\n5BTwpUgjrTQw6jDk8la5EHNDYvtf0KNCwjzkiNmJafTMsR8bLAspvA3KwWvrK1Mq\nvkawWUof3ueiCCIEVPnJyBjR4pWa/iF4ei4PnSZZsQKBgQDjYVJq2FEt99KMqagD\nc4dC4xTU2wY00e3W/Gv5GjtRTrDfb3zuxwmu1rT5Sx8bieOvw5I4/JLKbHxUNV2V\nnKZCT17vX2uUCvnN4Zc7YYOqi67ns/fYsnf21HE4FgL8ZwMPH6N8U4mQEyJCX47W\nLa+VVGlv4BWOK+S3Vt9Dii0FcwKBgQDJ2plcliYG+/JBAFnp1jrgCxLW0tvSoAyc\nG6KrZVaM1mqrRhiY3pAeHBHEtpVOIrbmTO+blowSLer0OQuM8epaUWKM8dq8ndXJ\n0aUvWncckLxOziSPdEuteMcMNHcIU0wMN2KbbSQDff3bkEezGq2KfxvVWZV3UX15\nMray20J+ZwKBgQCQKvfHuOoX3EbKWxOlRI3hkft2Tnzr5qMHqbqIEeLEVcF9mcG7\n38U67vWGDuRlYJNVsQm4SiSEZi6acc+pec5Mwuhtm7GpByCGMl/iDZ0e+Dvou0oN\nQnMftGko54PzJxlgcG4G+SyChi81qEL3d7YZV5EWlxzzrM7ylAkxWJ3dEwKBgAX7\nOkwqDtpqINWYQxHQzVHSQi6ndOga4gTGNN3LVPM7b1G/8/6jqbWas1QW7PmxwaW1\nZexAW8o2Hh46ioMUsBMZEkiG6ipoquseET0D+z+Xcl0Lcr3lflCXoZ5U96oBfeFm\nyr88TrLjyt/0uIswITBXb+W0j99HROaQgCVwpdnFAoGAK0L+Itfmxg02iXapO+9q\nznLo5TozmLpNSXoicnsrPvPPHEn4FtU+ZZc3XJbzKHBvE6MqQz78tGg3fnm5vsWm\nf0klqTW8BHenO6hFM2TxIkPPFs4LCsmhxXp96B8GrGt0UxywzaLxT3oiFEVqa2u8\nkE6+HvzVdL5H/ty57lz+9kE=\n-----END PRIVATE KEY-----\n",
  "client_email": "1045252027861-compute@developer.gserviceaccount.com",
  "client_id": "107670826722721704678",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/1045252027861-compute%40developer.gserviceaccount.com"

}

try:  
    res = requests.get(
    f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Loading...")
    
    soup = BeautifulSoup(res.text, 'html.parser')
    
    info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()
    print(info)
    
    credentials = service_account.Credentials.from_service_account_info(credentials_dict)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket('weather-dataops')
    blob = bucket.blob('weather_info.txt')
    
    blob.upload_from_string(info + '\n')
     
    with open('weather_info.txt', 'a') as f:
        f.write(info + '\n')
    print("Finished.")
    
except Exception as ex: 
    print(ex)

