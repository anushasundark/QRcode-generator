import segno

link = input("Enter the link: ")
qrc = segno.make(link)
qrc.save("qrcode.png")
qrc.show()
