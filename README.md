# YouTube Video Subtitle Downloader with Flask

This Flask application allows users to download subtitles from YouTube videos.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/qobulovasror/youtube-subtitles-downloader.git
    cd youtube-subtitles-downloader
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to [http://localhost:5200](http://localhost:5200).
   
3. Enter the URL of the YouTube video for which you want to download subtitles.
   
4. Click the "Download Subtitles" button.
   
5. The subtitles will be downloaded in the SRT format.

## Project Structure
myflaskapp/\
|\
├── venv/                    # Virtual enviroment file\
│\
├── app.py                   # Main app\
│\
├── templates/               # HTML templates\
│   └── index.html\
│\
├── static/                  # Statik files (CSS, JavaScript, imgs, ...)\
│   ├── css/\
│   │   └── style.css\
│   └── js/
│\
└── README.md                # About proyekt \


## Dependencies

- Flask: Web framework for Python
- requests: HTTP library for making requests

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Muallif

Muallif: [Asror Qobulov](https://github.com/qobulovasror)
