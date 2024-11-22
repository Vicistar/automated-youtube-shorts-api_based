import asyncio
from instagram_scraper import fetch_videos
from video_compiler import curate_videos, compile_videos
from youtube_uploader import upload_to_youtube
from cleanup import cleanup_files
from db_setup import Session, ScrapedVideo

def main():
    # Step 1: Scrape Instagram videos
    api_url = "https://graph.instagram.com"
    access_token = "YOUR_ACCESS_TOKEN"
    user_ids = ["USER_ID_1", "USER_ID_2"]
    asyncio.run(fetch_videos(api_url, access_token, user_ids))
    
    # Step 2: Curate videos
    session = Session()
    videos = session.query(ScrapedVideo).filter_by(processed=False).all()
    curated_videos = curate_videos(videos)
    
    # Step 3: Compile videos
    video_paths = [video.downloaded_path for video in curated_videos]
    output_path = "./compiled/final_compilation.mp4"
    compile_videos(video_paths, output_path)
    
    # Step 4: Upload to YouTube
    title = "Daily Meme Compilation"
    description = "The best memes compiled daily!"
    tags = ["memes", "funny", "daily compilation"]
    upload_to_youtube(output_path, title, description, tags)
    
    # Step 5: Cleanup
    cleanup_files('./videos')
    cleanup_files('./compiled')

if __name__ == "__main__":
    main()
