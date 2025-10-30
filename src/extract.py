import requests

class Extract:
    def __init__(self):
        self.base_url = "http://universities.hipolabs.com/search"

    def extract_data(self, country: str) -> list[dict]:
        """
        Faz a extração de universidades por país.
        """
        url = f"{self.base_url}?country={country}"
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            data = response.json()
            return data if isinstance(data, list) else []
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar dados de {country}: {e}")
            return []
