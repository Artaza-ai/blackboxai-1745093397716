# Medical Imaging Assistant

A web-based medical imaging analysis tool for X-ray and CT scan interpretation. This application provides educational pattern recognition and structured radiology-style reports.

## ⚠️ Important Safety Notice

**This AI does not provide medical diagnoses. All findings require radiologist confirmation. This tool is for educational and observational purposes only.**

## Features

### 🔍 Image Analysis
- Upload medical images (X-ray, CT scans)
- Automatic image quality assessment
- Pattern recognition and visual analysis
- Structured radiology-style reporting

### 📋 Report Sections
1. **Image Quality Assessment** - Resolution, contrast, and technical parameters
2. **Visual Observations** - Descriptive findings from image analysis
3. **Possible Interpretations** - Non-diagnostic pattern suggestions
4. **Recommendations** - Professional review requirements

### 🛡️ Safety Features
- Prominent safety disclaimers throughout the interface
- Non-diagnostic language ("may suggest", "could indicate")
- Mandatory radiologist review recommendations
- Educational purpose statements

## Technology Stack

### Backend
- **Python 3.9+**
- **Flask 3.1.2** - Web framework
- **Flask-CORS 6.0.1** - Cross-origin resource sharing
- **Pillow 11.3.0** - Image processing

### Frontend
- **HTML5**
- **Tailwind CSS** - Styling framework
- **Vanilla JavaScript** - Interactive functionality
- **Inter Font** - Typography

## Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or navigate to the project directory:**
   ```bash
   cd /vercel/sandbox
   ```

2. **Install Python dependencies:**
   ```bash
   cd backend
   python3 -m pip install Flask Flask-CORS Pillow
   ```

3. **No frontend dependencies needed** (uses CDN for Tailwind CSS)

## Running the Application

### Start the Backend Server

```bash
cd backend
python3 app.py
```

The backend API will start on `http://localhost:5000`

### Start the Frontend Server

In a new terminal:

```bash
cd frontend
python3 -m http.server 8000
```

The frontend will be available at `http://localhost:8000`

### Access the Application

Open your web browser and navigate to:
```
http://localhost:8000
```

## API Endpoints

### GET `/`
Returns API information and available endpoints.

**Response:**
```json
{
  "message": "Medical Imaging Assistant API",
  "version": "1.0",
  "disclaimer": "⚠️ This AI does not provide medical diagnoses...",
  "endpoints": {
    "/upload": "POST - Upload medical image for analysis",
    "/health": "GET - Health check"
  }
}
```

### GET `/health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "Medical Imaging Assistant"
}
```

### POST `/upload`
Upload and analyze a medical image.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: Form data with `image` field containing the image file

**Supported Formats:**
- PNG, JPG, JPEG, GIF, BMP, TIFF

**Response:**
```json
{
  "success": true,
  "report": {
    "disclaimer": "⚠️ This AI does not provide medical diagnoses...",
    "image_info": {
      "filename": "example.png",
      "resolution": "512x512"
    },
    "section_1_image_quality": {
      "title": "1. Image Quality Assessment",
      "assessment": "Adequate",
      "details": [...]
    },
    "section_2_observations": {
      "title": "2. Visual Observations",
      "findings": [...],
      "note": "Observations are descriptive only..."
    },
    "section_3_interpretations": {
      "title": "3. Possible Interpretations (Non-Diagnostic)",
      "interpretations": [...],
      "emphasis": "These are observational interpretations only..."
    },
    "section_4_recommendations": {
      "title": "4. Recommendations",
      "recommendations": [...]
    },
    "educational_note": "This analysis is provided for educational purposes..."
  },
  "timestamp": "Analysis completed"
}
```

## Testing

### Run Integration Tests

```bash
python3 test_integration.py
```

This will test:
- ✅ Health check endpoint
- ✅ Root endpoint
- ✅ Image upload and analysis
- ✅ Invalid upload handling
- ✅ Report structure validation
- ✅ Safety disclaimer presence

### Manual Testing with cURL

**Health Check:**
```bash
curl http://localhost:5000/health
```

**Upload Image:**
```bash
curl -X POST -F "image=@/path/to/image.png" http://localhost:5000/upload
```

## Project Structure

```
/vercel/sandbox/
├── README.md                 # This file
├── backend/
│   └── app.py               # Flask backend application
├── frontend/
│   └── index.html           # Web interface
├── test_integration.py      # Integration tests
├── create_test_image.py     # Test image generator
└── test_xray.png           # Sample test image
```

## Usage Guide

### For Users

1. **Open the Application**
   - Navigate to `http://localhost:8000` in your browser

2. **Upload an Image**
   - Click the upload area or drag and drop an image
   - Supported formats: PNG, JPG, JPEG, GIF, BMP, TIFF
   - Maximum file size: 10MB

3. **View Analysis**
   - Click "Analyze Image" button
   - Wait for processing (usually 1-2 seconds)
   - Review the structured report

4. **Understand the Report**
   - Read all sections carefully
   - Note the safety disclaimers
   - Remember: This is NOT a medical diagnosis

### For Developers

**Adding New Analysis Features:**

Edit `backend/app.py` and modify the `analyze_image_patterns()` function:

```python
def analyze_image_patterns(image):
    # Add your custom analysis logic here
    observations = []
    # ... your code ...
    return observations
```

**Customizing the Frontend:**

Edit `frontend/index.html` to modify the UI, styling, or behavior.

**Adding New Endpoints:**

```python
@app.route('/your-endpoint', methods=['GET', 'POST'])
def your_function():
    # Your logic here
    return jsonify({"result": "data"})
```

## Safety and Compliance

### Non-Diagnostic Language
All outputs use phrases like:
- "May suggest"
- "Could indicate"
- "Appears consistent with"
- "Requires correlation with clinical symptoms"

### Mandatory Disclaimers
Every report includes:
- Safety warning at the top
- Non-diagnostic emphasis in each section
- Radiologist review requirement
- Educational purpose statement

### Limitations
- This tool does NOT diagnose medical conditions
- It does NOT provide treatment recommendations
- It does NOT replace professional medical evaluation
- All findings must be confirmed by qualified radiologists

## Educational Use Cases

✅ **Appropriate Uses:**
- Learning radiology terminology
- Understanding image analysis concepts
- Demonstrating pattern recognition
- Educational demonstrations
- Research and development

❌ **Inappropriate Uses:**
- Clinical diagnosis
- Treatment decisions
- Patient care without radiologist review
- Replacing professional medical evaluation

## Troubleshooting

### Backend Won't Start
```bash
# Check if port 5000 is already in use
lsof -i :5000

# Install dependencies again
python3 -m pip install --upgrade Flask Flask-CORS Pillow
```

### Frontend Won't Load
```bash
# Check if port 8000 is already in use
lsof -i :8000

# Try a different port
python3 -m http.server 8080
```

### CORS Errors
- Ensure Flask-CORS is installed
- Check that backend is running on port 5000
- Verify frontend is accessing `http://localhost:5000`

### Image Upload Fails
- Check file format (must be PNG, JPG, JPEG, GIF, BMP, or TIFF)
- Verify file size is under 10MB
- Ensure backend server is running

## Performance

- **Image Processing:** ~1-2 seconds for typical medical images
- **Supported Resolution:** Up to 4096x4096 pixels
- **Memory Usage:** ~100-200MB for typical operations

## Future Enhancements

Potential features for future development:
- DICOM file format support
- Advanced pattern recognition algorithms
- Multi-image comparison
- Report export (PDF, JSON)
- User authentication
- Image annotation tools
- Integration with PACS systems

## License

This project is for educational purposes only. Not intended for clinical use.

## Support

For issues, questions, or contributions:
- Review the code in `backend/app.py` and `frontend/index.html`
- Run integration tests: `python3 test_integration.py`
- Check console logs for errors

## Version History

### v1.0 (Current)
- Initial release
- Basic image upload and analysis
- Structured radiology-style reports
- Safety disclaimers and non-diagnostic language
- Web-based interface
- Integration tests

---

**Remember:** This tool is for educational purposes only. Always consult qualified medical professionals for actual medical imaging interpretation and diagnosis.
