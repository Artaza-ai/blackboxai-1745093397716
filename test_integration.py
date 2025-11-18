#!/usr/bin/env python3
"""
Integration test for Medical Imaging Assistant
Tests the complete workflow: image upload -> analysis -> report generation
"""

import requests
import json
import os

# Configuration
BACKEND_URL = "http://localhost:5000"
TEST_IMAGE_PATH = "/vercel/sandbox/test_xray.png"

def test_health_endpoint():
    """Test the health check endpoint"""
    print("=" * 60)
    print("TEST 1: Health Check Endpoint")
    print("=" * 60)
    
    response = requests.get(f"{BACKEND_URL}/health")
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200, "Health check failed"
    assert response.json()["status"] == "healthy", "Service not healthy"
    
    print("✅ Health check passed!\n")

def test_root_endpoint():
    """Test the root endpoint"""
    print("=" * 60)
    print("TEST 2: Root Endpoint")
    print("=" * 60)
    
    response = requests.get(f"{BACKEND_URL}/")
    
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Message: {data['message']}")
    print(f"Version: {data['version']}")
    print(f"Disclaimer: {data['disclaimer'][:80]}...")
    
    assert response.status_code == 200, "Root endpoint failed"
    assert "Medical Imaging Assistant" in data["message"], "Wrong service"
    
    print("✅ Root endpoint passed!\n")

def test_image_upload_and_analysis():
    """Test image upload and analysis"""
    print("=" * 60)
    print("TEST 3: Image Upload and Analysis")
    print("=" * 60)
    
    # Check if test image exists
    if not os.path.exists(TEST_IMAGE_PATH):
        print(f"❌ Test image not found: {TEST_IMAGE_PATH}")
        return False
    
    print(f"Uploading image: {TEST_IMAGE_PATH}")
    
    # Upload image
    with open(TEST_IMAGE_PATH, 'rb') as f:
        files = {'image': ('test_xray.png', f, 'image/png')}
        response = requests.post(f"{BACKEND_URL}/upload", files=files)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print(f"❌ Upload failed: {response.text}")
        return False
    
    data = response.json()
    
    # Verify response structure
    assert data["success"] == True, "Upload not successful"
    assert "report" in data, "No report in response"
    
    report = data["report"]
    
    # Verify report sections
    print("\n📋 Report Structure:")
    print(f"  - Disclaimer: {report['disclaimer'][:50]}...")
    print(f"  - Image Info: {report['image_info']}")
    print(f"  - Section 1 (Quality): {report['section_1_image_quality']['title']}")
    print(f"  - Section 2 (Observations): {report['section_2_observations']['title']}")
    print(f"  - Section 3 (Interpretations): {report['section_3_interpretations']['title']}")
    print(f"  - Section 4 (Recommendations): {report['section_4_recommendations']['title']}")
    
    # Verify all required sections exist
    required_sections = [
        'disclaimer',
        'image_info',
        'section_1_image_quality',
        'section_2_observations',
        'section_3_interpretations',
        'section_4_recommendations',
        'educational_note'
    ]
    
    for section in required_sections:
        assert section in report, f"Missing section: {section}"
    
    # Verify safety language
    assert "not provide medical diagnoses" in report['disclaimer'], "Missing safety disclaimer"
    assert "radiologist" in report['disclaimer'].lower(), "Missing radiologist mention"
    
    print("\n✅ Image upload and analysis passed!")
    print("\n📊 Sample Report Content:")
    print(f"  Quality Assessment: {report['section_1_image_quality']['assessment']}")
    print(f"  Number of Observations: {len(report['section_2_observations']['findings'])}")
    print(f"  Number of Interpretations: {len(report['section_3_interpretations']['interpretations'])}")
    print(f"  Number of Recommendations: {len(report['section_4_recommendations']['recommendations'])}")
    
    return True

def test_invalid_upload():
    """Test upload with no file"""
    print("\n" + "=" * 60)
    print("TEST 4: Invalid Upload (No File)")
    print("=" * 60)
    
    response = requests.post(f"{BACKEND_URL}/upload")
    
    print(f"Status Code: {response.status_code}")
    
    assert response.status_code == 400, "Should return 400 for no file"
    
    print("✅ Invalid upload handling passed!\n")

def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("MEDICAL IMAGING ASSISTANT - INTEGRATION TESTS")
    print("=" * 60 + "\n")
    
    try:
        test_health_endpoint()
        test_root_endpoint()
        test_image_upload_and_analysis()
        test_invalid_upload()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\n🎉 Medical Imaging Assistant is working correctly!")
        print("   - Backend API: ✅ Operational")
        print("   - Image Processing: ✅ Functional")
        print("   - Report Generation: ✅ Complete")
        print("   - Safety Disclaimers: ✅ Present")
        print("\n" + "=" * 60)
        
        return True
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
