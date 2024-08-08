from django.shortcuts import render
import qrcode
from django.http import HttpResponse
from io import BytesIO

import qrcode.main


def index(request):
    return render(request, 'index.html')


def qr_code_generator(request):
    if request.method == 'POST':
        data = request.POST.get('data')

        qr = qrcode.main.QRCode(
            version=1,
            error_correction=qrcode.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        data = qr.add_data(data)
        qr.make(fit=True)

        image = qr.make_image(fill='black', back_color="white")

        buffer = BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

        return HttpResponse(buffer, content_type="image/PNG")
    


