import os
import time

import assemblyai as aai


aai.settings.api_key = os.getenv('AAI_API_KEY')
FOLDER_PATH = input("Enter path to folder: ")

try:
    transcriber = aai.Transcriber()

    mp4_files_all = [f for f in os.listdir(FOLDER_PATH) if f.endswith('.mp4')]
    print(f"- {len(mp4_files_all)} total .mp4 files found.")

    mp4_files_raw = [f for f in mp4_files_all if not os.path.exists(os.path.join(FOLDER_PATH, os.path.splitext(f)[0] + '.srt'))]
    print(f"- {len(mp4_files_raw)} .mp4 files found without srt.")
    mp4_files = sorted(mp4_files_raw)

    transcribed_files = 0

    for mp4_file in mp4_files:
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
        print(f"Srt file for {mp4_file} is generated and saved as {srt_file_name}.")
        print(f"{transcribed_files}/{len(mp4_files)}")
except FileNotFoundError:
    print("No folder found.")
