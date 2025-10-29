# AI Assistant (Nexa)

A voice-controlled AI assistant similar to Jarvis from Iron Man, built with Python. This intelligent assistant can respond to voice commands, answer questions using OpenAI's GPT API, perform web searches, take screenshots, and provide various utilities through natural voice interaction.

## Features

- **Voice Recognition**: Listen and respond to voice commands using speech recognition
- **Text-to-Speech**: Natural voice responses using pyttsx3
- **AI-Powered Responses**: Integration with OpenAI's GPT API for intelligent conversations
- **Screen Capture**: Take screenshots on command and save them automatically
- **Live Screen Monitoring**: Real-time screen capture with OCR text detection
- **Wikipedia Search**: Quick Wikipedia lookups through voice commands
- **Web Navigation**: Open websites like YouTube and Google
- **Time Announcements**: Get current time on request
- **Jokes**: Entertainment with built-in joke functionality
- **OCR Capabilities**: Extract text from screen captures using Tesseract

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- Tesseract OCR (for text extraction from images)
- A working microphone (for voice commands)
- OpenAI API key (for AI-powered responses)

### Installing Tesseract OCR

**macOS:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt-get install tesseract-ocr
```

**Windows:**
Download and install from: https://github.com/UB-Mannheim/tesseract/wiki

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CaymanMaragh/AI-Assistant.git
   cd AI-Assistant
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set up OpenAI API Key:**
   
   Create a `.env` file in the project root directory:
   ```bash
   touch .env
   ```

   Add your OpenAI API key to the `.env` file:
   ```
   OPEN_AI_SECRET_KEY=your_openai_api_key_here
   ```

   You can obtain an API key from [OpenAI's platform](https://platform.openai.com/api-keys).

## Usage

### Running the Voice Assistant

To start the main voice assistant:

```bash
python tts.py
```

The assistant will greet you and wait for voice commands. Available commands include:

- **"Wikipedia [topic]"** - Search Wikipedia for information
- **"Open YouTube"** - Opens YouTube in your browser
- **"Open Google"** - Opens Google in your browser
- **"What time is it"** or **"time"** - Announces current time
- **"Tell me a joke"** - Get a random joke
- **"Take screenshot"** - Captures and saves a screenshot
- **"Ask [your question]"** - Ask the AI assistant anything
- **"Exit"** or **"Bye"** - Close the assistant

### Other Utilities

**Live Screen Capture with OCR:**
```bash
python screen.py
```
- Press `ESC` to exit
- Automatically detects and prints text from your screen

**Manual Screenshot Tool:**
```bash
python savescreen.py
```
- Press `S` to save a screenshot
- Press `ESC` to exit

**Test Voice Settings:**
```bash
python voicetest.py
```

**Ask AI Directly (without voice):**
```bash
python askAI.py
```

## Project Structure

```
AI-Assistant/
├── tts.py              # Main voice assistant program
├── askAI.py            # OpenAI GPT integration
├── screen.py           # Live screen capture with OCR
├── savescreen.py       # Manual screenshot capture tool
├── screenview.py       # Screen sharing utilities
├── voicetest.py        # Voice configuration tester
├── cam.py              # Camera/image utilities
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (API keys)
├── .gitignore         # Git ignore rules
└── screenshots/        # Saved screenshots directory
```

## Key Dependencies

- **openai**: Interface with OpenAI's GPT models
- **pyttsx3**: Text-to-speech conversion
- **SpeechRecognition**: Convert speech to text
- **opencv-python**: Computer vision and image processing
- **mss**: Fast screen capture
- **pytesseract**: OCR text extraction
- **wikipedia**: Wikipedia API wrapper
- **pyjokes**: Joke generation

## Troubleshooting

### Voice Recognition Issues
- Ensure your microphone is properly connected and configured
- Check microphone permissions in your system settings
- Adjust ambient noise duration in `tts.py` if recognition is poor

### Tesseract Not Found
- Verify Tesseract is installed: `tesseract --version`
- Set the Tesseract path explicitly in your code if needed:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'
  ```

### OpenAI API Errors
- Verify your API key is correctly set in the `.env` file
- Check your OpenAI account has available credits
- Ensure you have access to the model specified in `askAI.py`

### Screen Capture Issues
- On macOS, grant screen recording permissions in System Preferences > Security & Privacy
- On Linux, ensure X11 is properly configured

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Inspired by Jarvis from Iron Man
- Built with Python and various open-source libraries
- Powered by OpenAI's GPT technology

## Disclaimer

This project requires an active OpenAI API key and will incur costs based on API usage. Please monitor your API usage and costs through the OpenAI dashboard.
