When prompted, enter the YouTube URL of the video you want to download. The video will be saved in the `downloads` folder in the best available quality.

## Configuration

You can modify the following parameters in the `download_video()` function:
- `save_path`: Change the download directory (default: "downloads")
- `quality`: Modify the video quality (default: "best")

## Disclaimer

Please ensure you comply with YouTube's terms of service and only download videos that you have permission to download.

## Setup

To run this script, it's recommended to use a virtual environment. Follow these steps:

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install the required package**:
   ```bash
   pip install yt-dlp
   ```
