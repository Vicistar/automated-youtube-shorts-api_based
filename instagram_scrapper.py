import asyncio
import aiohttp
from db_setup import ScrapedVideo, Session

# Fetch Instagram media asynchronously
access_token = "IGQWROajc4Sk83MWlGQVVYVHFRTG1qSXhEWktyVTJ6Q2FWQWI4aHp3bzdKbEcyTXROTVktYXN0NU9ERXRTRkJ5SS1RdVduNjA2MTRNWkJyUnYzaUpicjh5VHhhVWhWQmlNWEp3WGtQQUNVaUk5RzIwcUhoRzFaZAzQZD"
async def fetch_videos(api_url, user_ids):
    session = Session()
    async with aiohttp.ClientSession() as client:
        for user_id in user_ids:
            url = f"{api_url}/{user_id}/media?fields=media_type,media_url,caption,timestamp&access_token={access_token}"
            async with client.get(url) as response:
                data = await response.json()
                for media in data.get('data', []):
                    if media['media_type'] == 'VIDEO':
                        video = ScrapedVideo(
                            video_url=media['media_url'],
                            caption=media.get('caption'),
                            posted_at=media.get('timestamp')
                        )
                        session.add(video)
    session.commit()
