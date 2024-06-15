import qrcode 
features = qrcode.QRCode(version=1, box_size=40, border=3)

features.add_data("https://www.youtube.com")
features.make(fit=True)

generate_image = features.make_image(fill_colour="black", back_colour="white")
generate_image.save("image2.png")
