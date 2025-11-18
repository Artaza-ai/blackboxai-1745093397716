from PIL import Image

# Create a simple test medical-like image (grayscale)
img = Image.new('L', (512, 512), color=128)

# Add some patterns to simulate medical imaging
for i in range(100, 400):
    for j in range(100, 400):
        img.putpixel((i, j), 180)

img.save('/vercel/sandbox/test_xray.png')
print("Test image created: /vercel/sandbox/test_xray.png")
