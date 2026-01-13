import qrcode as qr
qr=qrcode.QRcode(
    version=15,
    box_size=10,
    border=5
    )
data="https://www.youtube.com/watch?v=It57Mjm09pk"
qr.add_data(data)
qr.make()
qr.make(fit=True)
qr.make_image(fill="blue",back_color="white")
img.save("orcode.png")
