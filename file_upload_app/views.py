from django.shortcuts import render
from django.http import HttpResponse
import os
import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_name = generate_random_string(10) + '_' + uploaded_file.name
        file_path = os.path.join('media', file_name)
        with open(file_path, 'wb') as file:
            for chunk in uploaded_file.chunks():
                file.write(chunk)
        download_link = f"/download/{file_name}"
        return HttpResponse(f"File uploaded successfully! Download link: <a href='{download_link}'>{download_link}</a>")
    return render(request, 'upload.html')

def download_file(request, file_name):
    file_path = os.path.join('media', file_name)
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response

