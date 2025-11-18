# Quick Start Guide - Medical Imaging Assistant

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Start Backend
```bash
python3 app.py
```
Backend runs on: http://localhost:5000

### Step 3: Start Frontend (New Terminal)
```bash
cd frontend
python3 -m http.server 8000
```
Frontend runs on: http://localhost:8000

### Step 4: Open Browser
Navigate to: **http://localhost:8000**

---

## 📸 How to Use

1. **Click** the upload area or drag & drop an image
2. **Select** a medical image (X-ray, CT scan)
3. **Click** "Analyze Image" button
4. **Review** the structured report

---

## ⚠️ Safety Reminder

**This tool does NOT diagnose medical conditions.**

All findings require confirmation by a qualified radiologist.

For educational purposes only.

---

## 🧪 Run Tests

```bash
python3 test_integration.py
```

---

## 📊 Example API Usage

### Upload Image via cURL
```bash
curl -X POST \
  -F "image=@/path/to/xray.png" \
  http://localhost:5000/upload
```

### Check Health
```bash
curl http://localhost:5000/health
```

---

## 🛠️ Troubleshooting

**Port Already in Use?**
```bash
# Backend (change port in app.py)
app.run(host='0.0.0.0', port=5001)

# Frontend (use different port)
python3 -m http.server 8080
```

**CORS Issues?**
- Ensure Flask-CORS is installed
- Backend must be running first
- Check browser console for errors

---

## 📁 Project Structure

```
/vercel/sandbox/
├── README.md              # Full documentation
├── USAGE.md              # This quick start guide
├── backend/
│   ├── app.py            # Flask API server
│   └── requirements.txt  # Python dependencies
├── frontend/
│   └── index.html        # Web interface
└── test_integration.py   # Automated tests
```

---

## ✅ Features

- ✅ Image upload (PNG, JPG, JPEG, GIF, BMP, TIFF)
- ✅ Quality assessment
- ✅ Pattern recognition
- ✅ Structured reports
- ✅ Safety disclaimers
- ✅ Non-diagnostic language
- ✅ Educational purpose

---

## 📞 Need Help?

1. Check README.md for detailed documentation
2. Run integration tests: `python3 test_integration.py`
3. Review backend logs for errors
4. Check browser console (F12) for frontend issues

---

**Version 1.0** | Educational Use Only
