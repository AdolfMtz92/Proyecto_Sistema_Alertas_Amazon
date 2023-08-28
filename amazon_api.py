import requests
from bs4 import BeautifulSoup


class AmazonAPI:
    def get_product_price(self, product_url):
        headers = {
            'Accept-Language': 'en-US,en;q=0.5',
            'User-Agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 "
                           "Edg/107.0.1418.52")
        }
        response = requests.get(product_url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            # Encuentra el elemento que contiene el precio en la página de Amazon
            price_element = soup.find('span', {'class': 'a-offscreen'})
            if price_element:
                price_str = price_element.get_text()
                # Convierte el precio a un valor numérico con formateo adecuado
                price_str = price_str.replace(",", "").replace("$", "")
                try:
                    price = float(price_str)
                    return price
                except ValueError:
                    print(f"No se pudo convertir el precio '{price_str}' a un valor numérico.")
            else:
                print("No se pudo encontrar el precio en la página.")
        else:
            print(f"Error al obtener la página del producto. Código de estado: {response.status_code}")

        return None
