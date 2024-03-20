import os
import time

import assemblyai as aai
from tqdm import tqdm
from moviepy.editor import VideoFileClip


aai.settings.api_key = os.getenv('AAI_API_KEY')
FOLDER_PATH = input("Enter path to folder: ")

try:
    transcriber = aai.Transcriber()

    print()
    mp4_files_all = [f for f in os.listdir(FOLDER_PATH) if f.endswith('.mp4')]
    print(f"- {len(mp4_files_all)} total .mp4 files found.")

    mp4_files_raw = [f for f in mp4_files_all if not os.path.exists(os.path.join(FOLDER_PATH, os.path.splitext(f)[0] + '.srt'))]
    print(f"- {len(mp4_files_raw)} .mp4 files found without .srt")
    mp4_files = sorted(mp4_files_raw)
    print()

    transcribed_files = 0

    for mp4_file in tqdm(mp4_files, desc="- Transcribing files"):
        clip = VideoFileClip(os.path.join(FOLDER_PATH, mp4_file))
        duration_in_sec = clip.duration
        minutes = int(duration_in_sec // 60)
        seconds = int(duration_in_sec % 60)
        print(f"- Transcribing '{mp4_file}' ({minutes}min {seconds}sec)")

        start_time = time.time()
        FILE_URL = os.path.join(FOLDER_PATH, mp4_file)
        transcript = transcriber.transcribe(FILE_URL)

        while transcript.status != "completed":
            time.sleep(5)

        srt = transcript.export_subtitles_srt(chars_per_caption=32)

        srt_file_name = os.path.splitext(mp4_file)[0] + '.srt'
        srt_file_path = os.path.join(FOLDER_PATH, srt_file_name)

        with open(srt_file_path, "w") as f:
            f.write(srt)

        transcribed_files += 1
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"- '{mp4_file}' transcribed to '{srt_file_name}' in {round(elapsed_time)} seconds.")
        print("---------------")
except FileNotFoundError:
    print("- No folder found.")
