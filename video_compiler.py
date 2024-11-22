from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def curate_videos(videos, n_clusters=5):
    captions = [video.caption for video in videos]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(captions)
    kmeans = KMeans(n_clusters=n_clusters)
    labels = kmeans.fit_predict(X)
    curated_videos = [videos[i] for i in range(len(videos)) if labels[i] == 0]
    return curated_videos

from moviepy.editor import VideoFileClip, concatenate_videoclips

def compile_videos(video_paths, output_path):
    clips = [VideoFileClip(path).subclip(0, 10) for path in video_paths]
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
