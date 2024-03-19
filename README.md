# TranscriberAI

MP4 to SRT Transcriber

## Description

This Python project automates the transcription of audio from .mp4 files to .srt (Subtitle) files using the AssemblyAI transcription service. It scans a specified folder for .mp4 files without corresponding .srt files and generates them.

## Installation

Before running this script, ensure you have Python installed on your system. Then, follow these steps to set up the project:

1. Clone this repository to your local machine:

```
git clone https://github.com/nikolaPantelic98/TranscriberAI.git
```

2. Navigate to the directory:

```
cd TranscriberAI
```

2. Install the required packages:

```
pip install -r requirements.txt
```

3. You will need an API key from AssemblyAI. Create an account at [AssemblyAI](https://www.assemblyai.com/) to obtain your API key.

## Usage

To use this script, follow these steps:

1. Set your AssemblyAI API key as an environment variable:

- For Linux:

```
echo 'export AAI_API_KEY="your_api_key"' >> ~/.bashrc
```
```
source ~/.bashrc
```

- For Windows:

```
setx AAI_API_KEY "your_api_key"
```

- Replace `your_api_key` with real api key you got from AssemblyAI.
- It is necessary to close and reopen cmd for variables to be available on Windows.

2. Navigate to the root TranscriberAI directory and run the script using Python:

```
cd src && python3 transcriber.py
```

3. When prompted, enter the final path to the folder containing your .mp4 files.
4. The script will process each .mp4 file without an existing .srt file and generate the subtitles.

## Requirements

- Python 3.x
- An AssemblyAI API key

## Contributing

Feel free to fork this project and submit pull requests. Please open an issue first to discuss what you would like to change.
