import qrcode

data = input("Enter the text or URL for the QR Code: ")

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

# Ask user for a filename
filename = input("Enter filename to save (without extension): ") + ".png"

# Save the QR code
img.save(filename)

print(f"QR Code saved as {filename}")