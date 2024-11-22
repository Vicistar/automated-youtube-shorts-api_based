from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define the database schema
class ScrapedVideo(Base):
    __tablename__ = 'scraped_videos'
    id = Column(Integer, primary_key=True)
    video_url = Column(String, nullable=False)
    caption = Column(String)
    posted_at = Column(DateTime)
    downloaded_path = Column(String)
    processed = Column(Boolean, default=False)

# Initialize the database
DATABASE_URL = "sqlite:///videos.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
