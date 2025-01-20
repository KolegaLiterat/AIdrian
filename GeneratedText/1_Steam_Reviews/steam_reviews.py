# Standard library imports
from dataclasses import dataclass

# Third-party imports
import chromadb
from chromadb.utils import embedding_functions
from dynaconf import Dynaconf
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from tqdm import tqdm

# Local imports
from src.helper import File, PromptReader
from src.steam_webdata import SteamWebData
### SteamWeb page to parse
STEAMURL = "https://store.steampowered.com/sssapp/2377110/Pocket_Waifu_Rekindled/"

### Context Deps

@dataclass
class SteamAgentData:
    description: str
    genres: list[str]
    tags: list[str]
    database: chromadb.Collection
    answers: list[str]
    question: str
    results: int

### Api Keys
api_keys = Dynaconf(load_dotenv=True, envvar_prefix="KEY")

### Chroma Init
chroma_client = chromadb.Client()
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=api_keys.OPENAI,
    model_name="text-embedding-ada-002"
)

collection = chroma_client.create_collection(name="steam_reviews", embedding_function=openai_ef)

### Agent Init
prompts = PromptReader("prompts\\steam_reviews_prompts.yaml").read_file()

gpt_4o = OpenAIModel("gpt-4o", api_key=api_keys.OPENAI)

steam_game_agent = Agent(
    gpt_4o,
    result_type=list[str],
    system_prompt=(prompts["main_prompt"])
)

### Agent Tools
@steam_game_agent.tool
async def get_game_description(ctx: RunContext[SteamAgentData]):
    """check game description"""
    return ctx.deps.description

@steam_game_agent.tool
async def get_game_tags(ctx: RunContext[SteamAgentData]):
    """check game tags"""
    return ctx.deps.tags

@steam_game_agent.tool
async def get_game_genres(ctx: RunContext[SteamAgentData]):
    """check game genres"""
    return ctx.deps.genres

@steam_game_agent.tool
async def find_reviews_fragments(ctx: RunContext[SteamAgentData]):
    """retrive reviews fragments based on question"""
    answer = ctx.deps.database.query(
            query_texts=ctx.deps.question,
            n_results=ctx.deps.results,
    )
    
    return answer

@steam_game_agent.tool
async def read_reviews_summary(ctx: RunContext[SteamAgentData]):
    """read reviews summary"""
    return ctx.deps.answers

@steam_game_agent.tool
async def change_number_of_results(ctx: RunContext[SteamAgentData]):
    """change number of results"""
    return ctx.deps.results

@steam_game_agent.tool
async def additional_question(ctx: RunContext[SteamAgentData]):
    """change question"""
    return ctx.deps.question

def validate_steam_url(url: str) -> bool:
    if not url.startswith("https://store.steampowered.com/app/"):
        raise ValueError("Invalid Steam URL format. Exiting...")

def main():
    if validate_steam_url(STEAMURL):
        steam_web_data = SteamWebData(STEAMURL, api_keys.OPENAI)
        tags, description, genres = steam_web_data.get_game_data()
        steam_web_data.get_reviews(collection, prompts["check_reviews"])
   
        agent_deps = SteamAgentData(description=description, genres=genres, tags=tags, database=collection, answers=[], question="None", results=5)

        print("Running Steam Game Agent")

        questions = steam_game_agent.run_sync(prompts["task_questions"], deps=agent_deps)

        for question in tqdm(questions.data, desc="Processing questions", unit="question"):
            agent_deps.question = question

            answers = steam_game_agent.run_sync(prompts["task_fragments_summary"], deps=agent_deps)

            agent_deps.answers.append(answers.data)
    
        reviews_summary = steam_game_agent.run_sync(prompts["task_create_review"], deps=agent_deps)

        File("steam_reviews_summary.md").save(reviews_summary.data[0])
    
if __name__ == "__main__":
    main()




