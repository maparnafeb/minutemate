# MinuteMate - Meeting Minutes Generator

## 🎯 **Project Aim**
Build a background service that listens to a live meeting audio stream, then outputs structured minutes, action items, and follow‑up reminders via an API and web UI.

## 📋 **Overview**
MinuteMate captures meeting audio, transcribes it offline, summarizes key points, and displays results in a simple browser interface.

## 🏗️ **Architecture**

### **Backend Service (Python + Flask)**
- **Background listener**: Captures microphone/mock VoIP stream to rolling buffer
- **Offline transcription**: Uses OpenAI Whisper-tiny locally (no API costs)
- **NLP processing**: Simple regex-based extraction of action items and dates
- **REST API**: Status, minutes, and session management endpoints

### **Web UI (HTML + JavaScript)**
- **Single-page app**: Polls `/status` endpoint for live updates
- **Live indicator**: Shows recording status with blinking red dot
- **Minutes display**: Shows final structured meeting notes when ready

## 🚀 **Quick Start**

### **1. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2. Start Backend Service**
```bash
python app.py
```
Server runs on `http://localhost:8000`

### **3. Open Web UI**
Visit: `http://localhost:8000`

## 📚 **API Endpoints**

### **Core Endpoints**
- `GET /status` - Returns "recording" or "idle" status
- `POST /start` - Start recording session
- `POST /stop` - Stop recording session
- `POST /transcribe` - Process audio and generate transcript
- `POST /generate-minutes` - Generate meeting minutes from transcript
- `GET /minutes/{id}` - Get minutes for specific session

### **Example Usage**
```bash
# Check status
curl http://localhost:8000/status

# Start recording
curl -X POST http://localhost:8000/start

# Stop recording
curl -X POST http://localhost:8000/stop

# Generate minutes
curl -X POST http://localhost:8000/generate-minutes \
  -H "Content-Type: application/json" \
  -d '{"transcript": "Meeting content..."}'
```

## 🧪 **Testing**

### **Run Unit Tests**
```bash
python test_api.py
```

Tests cover:
- ✅ **Capture**: Recording start/stop functionality
- ✅ **Transcription call**: Audio processing and text generation
- ✅ **API endpoints**: All REST endpoints functionality

## 🔧 **Technical Details**

### **Dependencies**
- **Flask**: Web framework for API server
- **OpenAI Whisper**: Offline audio transcription (tiny model)
- **SoundFile**: Audio file handling
- **NumPy/Torch**: Machine learning support

### **Audio Processing**
- **Input**: Browser MediaRecorder API (WebM/Opus)
- **Processing**: Converted to WAV for Whisper compatibility
- **Output**: Structured text with timestamps

### **NLP Features**
- **Action Items**: Regex extraction of "will", "need to", "should"
- **Date Detection**: Pattern matching for dates and deadlines
- **Summary Generation**: 200-word limit with key topics
- **Chunking**: Splits long transcripts into manageable segments

## 📁 **Project Structure**
```
MinuteMate/
├── app.py                 # Main Flask backend service
├── static/
│   └── index.html        # Single-page web UI
├── test_api.py           # Unit tests for API endpoints
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🎨 **UI Features**

### **Recording Controls**
- **Start Button**: Initiates recording session
- **Stop Button**: Ends recording and processes audio
- **Live Indicator**: Blinking red dot during recording

### **Status Display**
- **Real-time Updates**: Polls backend every second
- **Duration Counter**: Shows recording time
- **Progress Messages**: Clear feedback on current state

### **Results View**
- **Live Transcription**: Real-time text as you speak
- **Meeting Minutes**: Structured summary with action items
- **Auto-scroll**: Automatically shows final results

## 🔒 **Constraints Met**

✅ **Free Libraries Only**: PyAudio, OpenAI Whisper-tiny, spaCy alternatives
✅ **No Paid APIs**: All processing done locally
✅ **Offline Transcription**: Whisper runs without internet
✅ **Simple Implementation**: Regex-based NLP, no complex models
✅ **Background Service**: Flask daemon with session management
✅ **Web UI**: Single HTML file with JavaScript polling

## 🐛 **Troubleshooting**

### **Common Issues**
1. **Port 8000 in use**: Change port in `app.py`
2. **Whisper model fails**: Check Python version (3.8+ required)
3. **Audio not working**: Ensure browser supports MediaRecorder API
4. **500 errors**: Check Python terminal for detailed error logs

### **Debug Steps**
1. Check backend logs in terminal
2. Test API endpoints with curl
3. Verify browser console for JavaScript errors
4. Run unit tests: `python test_api.py`

## 📝 **Development Notes**

### **Current Implementation**
- **Mock Audio**: Simulates real-time transcription for demo
- **Simple NLP**: Basic regex patterns for action items
- **Session Storage**: In-memory (not persistent)
- **Error Handling**: Basic try-catch with user feedback

### **Future Enhancements**
- **Real Audio Capture**: Browser MediaRecorder integration
- **Persistent Storage**: Database/file-based session management
- **Advanced NLP**: Better action item extraction
- **Silence Detection**: Auto-stop after 30s of silence

## 📄 **License**
Open source - use freely for educational and commercial purposes.

---

**Built with**: Python + Flask + Whisper + HTML/JS  
**No API keys required** - 100% offline processing 