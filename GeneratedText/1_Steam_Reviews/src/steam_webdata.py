# Standard library imports
import re
import uuid

# Third-party imports
from bs4 import BeautifulSoup
import chromadb
from openai import OpenAI
import requests
from tqdm import tqdm

class SteamWebData:
    def __init__(self, steam_page_url: str, api_key) -> None:
        self.steam_page_url = steam_page_url
        self.game_id = re.findall(r'\d+', steam_page_url)
        self.client = OpenAI(api_key=api_key)

    def get_game_data(self) -> tuple:
        print("Running SteamWebData Crawler")

        web_page = requests.get(self.steam_page_url)

        if web_page.status_code == 200:
            tags, description, genres = self.__crawl_steam_page(web_page.content)
        else:
            raise Exception(f"Failed to retrieve Steam page. Status code: {web_page.status_code}")

        return tags, description, genres

    def __crawl_steam_page(self, steam_page_content: str) -> tuple:
        print("Crawling steam page")

        soup = BeautifulSoup(steam_page_content, "html.parser")

        description, tags, genres = None, None, None

        if soup.find("div", {"id": "game_area_description"}) != None:
            description = soup.find("div", {"id": "game_area_description"}).text.strip()
        if soup.find_all("a", {"class": "app_tag"}) != None:
            tags = [tag.text.strip() for tag in soup.find_all("a", {"class": "app_tag"})]
        if soup.find("span", attrs={'data-panel': '{"flow-children":"row"}'}):
            genres = soup.find("span", attrs={'data-panel': '{"flow-children":"row"}'}).text.strip()
    
        return tags, description, genres
    
    def get_reviews(self, db_collection: chromadb.Collection, reviews_prompt: str) -> list[str]:
        print("Retrieving reviews")
        
        reviews_url = f"https://store.steampowered.com/appreviews/{self.game_id[0]}?json=1&filter=recent&num_per_page=100"
        response = requests.get(reviews_url)

        if response.status_code == 200:
            steam_reviews = response.json()
            
            if len(steam_reviews["reviews"]) > 0:
                for text in tqdm(steam_reviews["reviews"], desc="Adding reviews to database", unit="text"):
                    if self.__validate_review_length(text["review"]) and self.__check_review_value(text["review"], reviews_prompt) == "VALID":
                        print(text["review"])
                        db_collection.add(
                            ids=[str(uuid.uuid4())],
                            documents=[text["review"]]
                        )
            else:
                raise Exception("No reviews found! Check the game ID. Exiting...")
        else:
            raise Exception(f"Failed to retrieve reviews. Status code: {response.status_code}")
    
    def __validate_review_length(self, review: str) -> bool:
        is_review_length_valid = False

        if len(review) > 10:
            is_review_length_valid = True
        
        return is_review_length_valid

    def __check_review_value(self, review: str, reviews_prompt: str) -> bool:
        answer = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": str(reviews_prompt)},
                {"role": "user", "content": str(review)}
            ]
        )

        return answer.choices[0].message.content