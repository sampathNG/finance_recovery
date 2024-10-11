# from django.shortcuts import render

# Create your views here.
import PyPDF2
# from PyPDF2 import PdfReader

import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse
from .models import BalanceSheet, PLStatement

def upload_pdf(request):
    if request.method == 'POST':
        pdf_file = request.FILES['file']
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ""
        for page_num in range(pdf_reader.getNumPages()):
            text += pdf_reader.getPage(page_num).extractText()

        # Parse the extracted text and save it to the database
        # Placeholder code: You will need to adjust this based on your data structure
        # Example parsing logic
        balance_data = {'company_name': 'Company ABC', 'total_assets': 100000, 'total_liabilities': 50000, 'equity': 50000, 'date': '2023-01-01'}
        pl_data = {'company_name': 'Company ABC', 'revenue': 120000, 'expenses': 60000, 'net_income': 60000, 'date': '2023-01-01'}

        # Save data to database
        BalanceSheet.objects.create(**balance_data)
        PLStatement.objects.create(**pl_data)

        return JsonResponse({'message': 'PDF processed successfully', 'text': text})
    
    return render(request, 'upload.html')
