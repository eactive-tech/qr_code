import frappe
from frappe.twofactor import get_qr_svg_code
import pyqrcode

def get_qr_code(value, scale):
    qr = pyqrcode.create(value).png_as_base64_str(scale=scale, quiet_zone=1)
    return f'<img src="data:image/png;base64,{ qr }" class="qrcode">'