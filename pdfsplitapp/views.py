from django.shortcuts import render
from PyPDF2 import PdfWriter, PdfReader
import os
from django.conf import settings
def home(request):
    return render(request, 'home.html')
def split_pdf(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        try:
            pdf_file = request.FILES['pdf_file']
            split_type = request.POST.get('split_type')
            pdf_reader = PdfReader(pdf_file)
            total_pages = len(pdf_reader.pages)
            output_pdf = PdfWriter()
            if split_type == 'even':
                pages = range(1, total_pages, 2)
            elif split_type == 'odd':
                pages = range(0, total_pages, 2)
            for page_number in pages:
                output_pdf.add_page(pdf_reader.pages[page_number])
            output_filename = f'{split_type}_split.pdf'
            output_filepath = os.path.join(settings.MEDIA_ROOT, output_filename)
            with open(output_filepath, 'wb') as output_file:
                output_pdf.write(output_file)
            output_url = os.path.join(settings.MEDIA_URL, output_filename)
            context = {
                'output_url': output_url,
                'output_filename': output_filename,
            }
            return render(request, 'split.html', context)        
        except Exception as e:
            error_message = f"Error splitting PDF: {str(e)}"
            return render(request, 'split.html', {'error_message': error_message})
    return render(request, 'home.html')