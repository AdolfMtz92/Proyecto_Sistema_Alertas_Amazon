import pytest
from amazon_api import AmazonAPI


@pytest.fixture
def amazon_api_instance():

    instance = AmazonAPI()
    return instance


@pytest.mark.parametrize(
    "entry",
    [
        ('https://www.amazon.com.mx/SAMSUNG-Galaxy-A04-4GB_64GB-Blanco/dp/\
B0BJN6WRG9'),
        ('https://www.amazon.com.mx/SAMSUNG-pulgadas-1920x1080-FreeSync-LC2\
7R500FHLXZX/dp/B07Z8PNWZT/'),
        ('https://www.amazon.com.mx/Godel-Escher-Bach-Eternal-Golden/dp/046\
5026567/')
    ]
)
def test_get_product_price(amazon_api_instance, entry):
    # Probar que sí encuentra precios
    assert isinstance(amazon_api_instance.get_product_price(entry), float)
