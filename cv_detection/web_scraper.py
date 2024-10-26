# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.chrome.options import Options

# # class PlantInfoScraper:
# #     def _init_(self, plant_name):
# #         # Format plant name for URL compatibility
# #         formatted_plant_name = plant_name.replace(" ", "-").lower()
# #         self.url = f"https://www.thespruce.com/growing-{formatted_plant_name}-care-guide-article-4588379"
# #         self.driver = self._initialize_driver()

# #     def _initialize_driver(self):
# #         options = Options()
# #         options.add_argument("--headless")  # Run in headless mode (no UI)
# #         options.add_argument("--no-sandbox")
# #         options.add_argument("--disable-dev-shm-usage")
# #         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# #         return driver

# #     def fetch_data(self):
# #         self.driver.get(self.url)
# #         # Wait for a specific element to load on the page that typically contains plant care information
# #         try:
# #             WebDriverWait(self.driver, 10).until(
# #                 EC.presence_of_element_located((By.XPATH, "//body"))
# #             )
# #         except:
# #             print("Page loading timed out.")
# #             return None

# #     def get_water_requirements(self):
# #         try:
# #             # Target any sections or paragraphs containing "water"
# #             water_info = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Water')]")
# #             return water_info.text
# #         except:
# #             return "Watering information not found"

# #     def get_sunlight_requirements(self):
# #         try:
# #             # Target any sections or paragraphs containing "sunlight" or "light"
# #             sunlight_info = self.driver.find_element(By.XPATH, "//*[contains(text(), 'sunlight') or contains(text(), 'light')]")
# #             return sunlight_info.text
# #         except:
# #             return "Sunlight information not found"

# #     def get_plant_care_info(self):
# #         self.fetch_data()
# #         water = self.get_water_requirements()
# #         sunlight = self.get_sunlight_requirements()
# #         self.driver.quit()
# #         return {
# #             "plant_name": self.url.split('/')[-1].replace('-', ' '),
# #             "water": water,
# #             "sunlight": sunlight
# #         }

# # # Example usage
# # plant_scraper = PlantInfoScraper("aloe vera")
# # plant_info = plant_scraper.get_plant_care_info()
# # print(plant_info)























# # import requests
# # from bs4 import BeautifulSoup

# # class PlantInfoScraper:
# #     def _init_(self, plant_name):
# #         # Format plant name for URL compatibility
# #         formatted_plant_name = plant_name.replace(" ", "-").lower()
# #         self.url = f"https://www.thespruce.com/growing-{formatted_plant_name}-care-guide-article-4588379"
# #         self.headers = {
# #             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# #         }

# #     def fetch_data(self):
# #         try:
# #             response = requests.get(self.url, headers=self.headers)
# #             response.raise_for_status()
# #             return BeautifulSoup(response.text, "html.parser")
# #         except requests.RequestException as e:
# #             print(f"Error fetching data: {e}")
# #             return None

# #     def get_water_requirements(self, soup):
# #         # Extract water requirements based on specific HTML structure from The Spruce
# #         water_info = soup.find("p", string=lambda text: "water" in text.lower())
# #         return water_info.get_text() if water_info else "Watering information not found"

# #     def get_sunlight_requirements(self, soup):
# #         # Extract sunlight requirements based on specific HTML structure from The Spruce
# #         sunlight_info = soup.find("p", string=lambda text: "sun" in text.lower() or "light" in text.lower())
# #         return sunlight_info.get_text() if sunlight_info else "Sunlight information not found"

# #     def get_plant_care_info(self):
# #         soup = self.fetch_data()
# #         if soup:
# #             water = self.get_water_requirements(soup)
# #             sunlight = self.get_sunlight_requirements(soup)
# #             return {
# #                 "plant_name": self.url.split('/')[-1].replace('-',' '),
# #                 "water": water,
# #                 "sunlight": sunlight
# #             }
# #         return None

# # # Example usage
# # plant_scraper = PlantInfoScraper("aloe vera")
# # plant_info = plant_scraper.get_plant_care_info()
# # print(plant_info)
















# # import requests

# # class PlantInfoAPI:
# #     def _init_(self, plant_name, api_key):
# #         self.plant_name = plant_name
# #         self.api_key = api_key
# #         self.base_url = "https://trefle.io/api/v1/plants/search"

# #     def fetch_data(self):
# #         params = {
# #             "q": self.plant_name,
# #             "token": self.api_key
# #         }
# #         try:
# #             response = requests.get(self.base_url, params=params)
# #             response.raise_for_status()
# #             data = response.json()
# #             # Check if results exist
# #             return data["data"][0] if data["data"] else None
# #         except requests.RequestException as e:
# #             print(f"Error fetching data: {e}")
# #             return None

# #     def get_plant_care_info(self):
# #         plant_data = self.fetch_data()
# #         if plant_data:
# #             care_info = {
# #                 "plant_name": plant_data.get("common_name", "N/A"),
# #                 "scientific_name": plant_data.get("scientific_name", "N/A"),
# #                 "sunlight": plant_data.get("sunlight", "N/A"),
# #                 "water": plant_data.get("watering", "N/A"),
# #                 "other_requirements": plant_data.get("growth", {}).get("description", "No additional care details available")
# #             }
# #             return care_info
# #         else:
# #             return {"error": "Plant not found or no data available"}

# # # Example usage
# # api_key = "EXDswXkcKxtyzoiK1Gyc26pzuSWe5tdHiBNhoLFVfOM"  # Replace with your actual Trefle API key
# # plant_scraper = PlantInfoAPI("tulip", api_key)
# # plant_info = plant_scraper.get_plant_care_info()
# # print(plant_info)



# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.chrome.options import Options
# # import time

# # class MissouriPlantScraper:
# #     def _init_(self, plant_name):
# #         self.plant_name = plant_name
# #         self.search_url = f"https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderListResults.aspx?commonname={plant_name.replace(' ', '+')}"
# #         self.driver = self._initialize_driver()

# #     def _initialize_driver(self):
# #         options = Options()
# #         # options.add_argument("--headless")  # Run in headless mode (no UI)
# #         options.add_argument("--no-sandbox")
# #         options.add_argument("--disable-dev-shm-usage")
# #         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# #         return driver

# #     def fetch_search_result(self):
# #         self.driver.get(self.search_url)
# #         try:
# #             # Wait until the search results table is visible
# #             WebDriverWait(self.driver, 10).until(
# #                 EC.presence_of_element_located((By.CSS_SELECTOR, "table.table"))  # Adjust the selector if necessary
# #             )
# #             # Click on the first plant link in the search result table
# #             first_result = self.driver.find_element(By.CSS_SELECTOR, "table.table tbody tr td a")
# #             first_result.click()
# #         except Exception as e:
# #             print("Error finding search results:", e)
# #             return None

# #     def get_plant_care_info(self):
# #         self.fetch_search_result()
# #         time.sleep(3)  # Wait for the plant details page to load

# #         try:
# #             # Extract care information (example fields, adjust based on actual page structure)
# #             water = self._get_text_by_label("Water")
# #             sunlight = self._get_text_by_label("Sun")
# #             soil_type = self._get_text_by_label("Soil")
# #             description = self._get_text_by_label("Description")

# #             care_info = {
# #                 "plant_name": self.plant_name,
# #                 "water": water,
# #                 "sunlight": sunlight,
# #                 "soil_type": soil_type,
# #                 "description": description
# #             }
# #         except Exception as e:
# #             print("Error extracting care information:", e)
# #             care_info = None
# #         finally:
# #             self.driver.quit()
        
# #         return care_info

# #     def _get_text_by_label(self, label):
# #         try:
# #             # Locate the label by its text, then get the following sibling text
# #             element = self.driver.find_element(By.XPATH, f"//td[contains(text(), '{label}')]/following-sibling::td")
# #             return element.text
# #         except:
# #             return f"{label} information not found"

# # # Example usage
# # plant_scraper = MissouriPlantScraper("aloe vera")
# # plant_info = plant_scraper.get_plant_care_info()
# # print(plant_info)


# import requests
# import json

# class PlantIDAPI:
#     def _init_(self, api_key):
#         self.api_key = api_key
#         self.base_url = "https://api.plant.id/v2/identify"

#     def identify_plant(self, image_path):
#         headers = {
#             'Content-Type': 'application/json',
#             'Api-Key': self.api_key
#         }
        
#         with open(image_path, 'rb') as image_file:
#             image_data = image_file.read()
        
#         data = {
#             "images": [image_data],
#             "organs": ["leaf"]
#         }
        
#         response = requests.post(self.base_url, headers=headers, data=json.dumps(data))
        
#         if response.status_code == 200:
#             result = response.json()
#             return result
#         else:
#             return f"Error: {response.status_code} - {response.text}"

# # Example usage
# api_key = "YOUR_API_KEY"  # Replace with your actual API key
# plant_id_api = PlantIDAPI(api_key)

# # Path to an image of the plant (you must have a valid image for this method)
# image_path = "./testingImages/testing.jpg"
# result = plant_id_api.identify_plant(image_path)

# print(result)



























import json

class PlantCare:
    def __init__(self, json_file):
        with open(json_file, 'r') as file:
            self.plant_data = json.load(file)['plants']

    def get_plant_info(self, plant_name):
        for plant in self.plant_data:
            if plant['name'].lower() == plant_name.lower():
                return plant
        return None  

    def print_info(self, info, plant_name):
        if info:
            print(f"Plant Name: {info['name']}")
            print(f"Sunlight Requirements: {info['sunlight']}")
            print(f"Soil Quality: {info['soil']}")
            print(f"Weather Required: {info['weather']}")
            print(f"Water Requirements: {info['water']}")
        else:
            print(f"Plant '{plant_name}' not found.")
