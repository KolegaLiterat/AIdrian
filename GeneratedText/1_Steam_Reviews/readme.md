# Steam Game Reviews Analyzer

## Overview
A Python script that analyzes Steam game reviews using RAG (Retrieval Augmented Generation) and an agent workflow to provide comprehensive review summaries.

## Prerequisites
- OpenAI API key (store in `.env` file)
- Python with required dependencies

## Usage
1. Open `steam_reviews.py`
2. Set your target game's Steam URL in the `STEAMURL` variable:
```python
STEAMURL = "https://store.steampowered.com/app/294100/RimWorld/"
```
3. Run the script to generate a review summary

## How It Works
The script follows a structured workflow:
1. Retrieves the 100 most recent Steam reviews
2. Filters for high-quality, informative reviews
3. Stores filtered reviews in a vector database
4. Collects game metadata (description, tags, genres)
5. Generates a comprehensive summary using an agent with specialized tools

## Known Limitations
The Steam Reviews API may occasionally:
- Return empty JSON responses even for games with reviews
- Not function properly with demo pages

Example of API limitation:
```
API endpoint: https://store.steampowered.com/appreviews/2867690?json=1&filter=recent&num_per_page=100

Response: {"success":1,"query_summary":{"num_reviews":0,"review_score":0,"review_score_desc":"Brak recenzji użytkowników","total_positive":0,"total_negative":0,"total_reviews":0},"reviews":[],"cursor":"*"}
```