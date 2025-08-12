# Demo Screenshot Guide - MinuteMate

## 📸 **Required Screenshots for Deliverables**

### **1. Starting Listener Screenshot**
**What to capture:**
- UI showing "Click Start Recording to begin"
- Start button enabled, Stop button disabled
- Status showing "Ready to record - Backend connected"

**Steps:**
1. Open `http://localhost:5000`
2. Wait for page to load
3. Take screenshot of the initial state

### **2. Live Indicator Screenshot**
**What to capture:**
- Red blinking LIVE indicator visible
- Status showing "Recording in progress..."
- Live transcription text appearing
- Start button disabled, Stop button enabled

**Steps:**
1. Click "🎙️ Start Recording"
2. Wait for live indicator to appear
3. Wait for some transcription text to show
4. Take screenshot of active recording state

### **3. Final Minutes Display Screenshot**
**What to capture:**
- Meeting Minutes section visible
- Action items listed with checkmarks
- Dates mentioned section
- Summary section
- Success message visible

**Steps:**
1. Click "⏹️ Stop Recording"
2. Wait for processing to complete
3. Wait for minutes to appear
4. Take screenshot of final results

## 🎯 **Screenshot Tips**

### **Best Practices:**
- **Use full browser window** - Show complete UI
- **High resolution** - At least 1920x1080
- **Clear text** - Make sure all text is readable
- **Consistent lighting** - Avoid glare or shadows
- **Professional appearance** - Clean desktop background

### **File Naming:**
```
screenshots/
├── 01_starting_listener.png
├── 02_live_indicator.png
└── 03_final_minutes.png
```

## 🚀 **Quick Demo Script**

### **Step 1: Prepare System**
```bash
# Start backend
python app.py

# Open browser to
http://localhost:5000
```

### **Step 2: Take Screenshots**
1. **Starting Listener**: Page loads, take screenshot
2. **Live Indicator**: Click Start, wait for red dot, take screenshot
3. **Final Minutes**: Click Stop, wait for results, take screenshot

### **Step 3: Save Screenshots**
- Create `screenshots/` folder
- Save with descriptive names
- Ensure high quality and readability

## 📋 **Deliverables Checklist**

- [x] Sample transcript file
- [x] Expected minutes output
- [x] Demo screenshot guide
- [ ] Sample audio file (.wav)
- [ ] Screenshot 1: Starting listener
- [ ] Screenshot 2: Live indicator
- [ ] Screenshot 3: Final minutes display

**Next: Record sample audio and take screenshots!** 🎯 