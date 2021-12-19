from qrcodegen import *
from datetime import datetime

class QRCode(object):

	def __init__(self):
		pass

	def to_svg_str(self, qr: QrCode, border: int) -> str:
		"""Returns a string of SVG code for an image depicting the given QR Code, with the given number
		of border modules. The string always uses Unix newlines (\n), regardless of the platform."""
		if border < 0:
			raise ValueError("Border must be non-negative")
		parts: List[str] = []
		for y in range(qr.get_size()):
			for x in range(qr.get_size()):
				if qr.get_module(x, y):
					parts.append("M{},{}h1v1h-1z".format(x + border, y + border))
		return """<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
	<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {0} {0}" stroke="none">
		<rect width="100%" height="100%" fill="#FFFFFF"/>
		<path d="{1}" fill="#000000"/>
	</svg>
	""".format(qr.get_size() + border * 2, " ".join(parts))

	def genSvgFile(self, strcode:str):
		# Simple operation
		qr0 = QrCode.encode_text(strcode, QrCode.Ecc.MEDIUM)
		svg = self.to_svg_str(qr0, 4)  #See qrcodegen-demo #203 - Mahfuzur Rahman
		with open('qrcode.svg', 'w') as f:
			f.write(svg)
		#print(svg)

# Manual operation
'''
segs = QrSegment.make_segments("3141592653589793238462643383")
qr1 = QrCode.encode_segments(segs, QrCode.Ecc.HIGH, 5, 5, 2, False)
for y in range(qr1.get_size()):
    for x in range(qr1.get_size()):
        (... paint qr1.get_module(x, y) ...)
'''
