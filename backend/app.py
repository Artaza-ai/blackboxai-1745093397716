from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import base64
import os

app = Flask(__name__)
CORS(app)

# Safety disclaimer constant
SAFETY_DISCLAIMER = "⚠️ This AI does not provide medical diagnoses. All findings require radiologist confirmation. This tool is for educational and observational purposes only."

def analyze_image_quality(image):
    """Assess basic image quality parameters"""
    width, height = image.size
    mode = image.mode
    
    quality_notes = []
    
    # Check resolution
    if width < 512 or height < 512:
        quality_notes.append("Low resolution - may limit detailed analysis")
    else:
        quality_notes.append("Adequate resolution for analysis")
    
    # Check color mode
    if mode == 'L':
        quality_notes.append("Grayscale image (typical for medical imaging)")
    elif mode == 'RGB':
        quality_notes.append("Color image detected")
    else:
        quality_notes.append(f"Image mode: {mode}")
    
    # Check aspect ratio
    aspect_ratio = width / height
    if 0.8 <= aspect_ratio <= 1.2:
        quality_notes.append("Standard aspect ratio")
    else:
        quality_notes.append("Non-standard aspect ratio - image may be cropped or rotated")
    
    return {
        "resolution": f"{width}x{height}",
        "quality_assessment": "Adequate" if width >= 512 and height >= 512 else "Limited",
        "notes": quality_notes
    }

def analyze_image_patterns(image):
    """Analyze image for common patterns (simplified pattern recognition)"""
    # Convert to grayscale for analysis
    if image.mode != 'L':
        gray_image = image.convert('L')
    else:
        gray_image = image
    
    # Get basic statistics
    pixels = list(gray_image.getdata())
    avg_brightness = sum(pixels) / len(pixels)
    
    observations = []
    
    # Brightness analysis
    if avg_brightness < 50:
        observations.append("Overall dark appearance - may indicate underpenetration or dense tissue")
    elif avg_brightness > 200:
        observations.append("Overall bright appearance - may indicate overpenetration or air-filled spaces")
    else:
        observations.append("Moderate contrast levels observed")
    
    # Pattern suggestions (educational examples)
    observations.append("Visual analysis of density patterns in progress")
    observations.append("Structural elements visible for assessment")
    
    return observations

def generate_radiology_report(image, filename):
    """Generate a structured radiology-style report"""
    
    # Analyze image quality
    quality_data = analyze_image_quality(image)
    
    # Analyze patterns
    observations = analyze_image_patterns(image)
    
    # Build structured report
    report = {
        "disclaimer": SAFETY_DISCLAIMER,
        "image_info": {
            "filename": filename,
            "resolution": quality_data["resolution"]
        },
        "section_1_image_quality": {
            "title": "1. Image Quality Assessment",
            "assessment": quality_data["quality_assessment"],
            "details": quality_data["notes"]
        },
        "section_2_observations": {
            "title": "2. Visual Observations",
            "findings": observations,
            "note": "Observations are descriptive only and do not constitute diagnosis"
        },
        "section_3_interpretations": {
            "title": "3. Possible Interpretations (Non-Diagnostic)",
            "interpretations": [
                "Findings may suggest various normal or pathological patterns",
                "Visual patterns could be consistent with multiple conditions",
                "Appearance requires correlation with clinical symptoms and history"
            ],
            "emphasis": "These are observational interpretations only, not diagnoses"
        },
        "section_4_recommendations": {
            "title": "4. Recommendations",
            "recommendations": [
                "A qualified radiologist should review this image for clinical interpretation",
                "Correlate findings with patient clinical presentation",
                "Consider additional imaging modalities if clinically indicated",
                "Follow institutional protocols for image interpretation"
            ]
        },
        "educational_note": "This analysis is provided for educational purposes and pattern recognition demonstration. It does not replace professional medical evaluation."
    }
    
    return report

@app.route('/')
def home():
    return jsonify({
        "message": "Medical Imaging Assistant API",
        "version": "1.0",
        "disclaimer": SAFETY_DISCLAIMER,
        "endpoints": {
            "/upload": "POST - Upload medical image for analysis",
            "/health": "GET - Health check"
        }
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "Medical Imaging Assistant"})

@app.route('/upload', methods=['POST'])
def upload_image():
    """Handle image upload and return analysis"""
    
    # Check if image file is present
    if 'image' not in request.files:
        return jsonify({
            "error": "No image file provided",
            "message": "Please upload an image file"
        }), 400
    
    file = request.files['image']
    
    # Check if file has a filename
    if file.filename == '':
        return jsonify({
            "error": "No file selected",
            "message": "Please select a valid image file"
        }), 400
    
    # Validate file type
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}
    file_ext = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''
    
    if file_ext not in allowed_extensions:
        return jsonify({
            "error": "Invalid file type",
            "message": f"Allowed types: {', '.join(allowed_extensions)}"
        }), 400
    
    try:
        # Read and process image
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        # Generate report
        report = generate_radiology_report(image, file.filename)
        
        # Convert image to base64 for preview (optional)
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        report['image_preview'] = f"data:image/{file_ext};base64,{image_base64[:100]}..."  # Truncated for response size
        
        return jsonify({
            "success": True,
            "report": report,
            "timestamp": "Analysis completed"
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": "Image processing failed",
            "message": str(e),
            "disclaimer": SAFETY_DISCLAIMER
        }), 500

@app.route('/diagnose', methods=['POST'])
def diagnose():
    """Legacy endpoint - redirects to /upload"""
    return jsonify({
        "message": "Please use /upload endpoint for image analysis",
        "disclaimer": SAFETY_DISCLAIMER
    }), 301

if __name__ == '__main__':
    print("=" * 60)
    print("Medical Imaging Assistant API Starting...")
    print("=" * 60)
    print(f"\n{SAFETY_DISCLAIMER}\n")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5000, debug=True)
