import json 
import pytube 
import whisper 


url_list = json.load(open('Data.json', 'r'))


def transcribe_youtube(youtube_url, output_filename="transcript.txt", model="base"):
    """Transcribes a YouTube video using OpenAI Whisper and saves the transcript to a file.

    Args:
        youtube_url (str): The URL of the YouTube video to transcribe.
        output_filename (str, optional): The filename to save the transcript to. Defaults to "transcript.txt".
        model (str, optional): The Whisper model to use. Defaults to "base" (smaller, faster).
            Valid options include "base", "medium", "large". Larger models are more accurate but slower.

    Returns:
        str: The transcribed text, or None if an error occurs.
    """

    try:
        # Create a PyTube object to access the video
        yt = pytube.YouTube(youtube_url)

        # Extract the audio stream (only audio)
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio stream and save it to a temporary file
        audio_filename = "audio.mp3"  # Temporary audio file
        audio_stream.download(filename=audio_filename)

        # Load the Whisper model
        model = whisper.load_model(model)

        # Transcribe the audio file
        result = model.transcribe(audio_filename)

        # Extract the transcribed text
        transcript = result["text"]

        # Save the transcript to the specified file
        with open(output_filename, "w") as f:
            f.write(transcript)

        # Clean up the temporary audio file
        import os
        os.remove(audio_filename)

        return transcript

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with the actual YouTube URL
transcript = transcribe_youtube(youtube_url)

if transcript:
    print(f"Transcript saved to: {output_filename}")
else:
    print("Transcription failed.")


def get_video_urls_from_playlist(playlist_url):
    """Extracts video URLs from a YouTube playlist URL.

    Args:
        playlist_url (str): The URL of the YouTube playlist.

    Returns:
        list: A list of video URLs in the playlist.
    """

    try:
        # Create a Playlist object using pytube
        playlist = pytube.Playlist(playlist_url)

        # Extract and return video URLs
        video_urls = playlist.video_urls
        return video_urls

    except Exception as e:
        print(f"An error occurred while getting video URLs: {e}")
        return []



# Example usage
playlist_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PL-Jc9JyrGxT8QbbNrqs7dPzYtOcjRXJwY"  # Replace with the actual playlist URL
video_urls = get_video_urls_from_playlist(playlist_url)

if video_urls:
    print(f"Extracted {len(video_urls)} video URLs from the playlist.")
    for video_url in video_urls:
        transcribe_youtube(video_url)  # Transcribe each video in the playlist
else:
    print("Failed to extract video URLs from playlist.")

