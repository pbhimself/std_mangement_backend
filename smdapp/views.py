from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import models, serializers

# Create your views here.

def testapp(request):
    return HttpResponse("Hello, this is a test app response.")

class InserData(APIView):
    @csrf_exempt
    def post(self, request):
        #sample data
        serializer = serializers.SubjectMetaDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return HttpResponse(serializer.errors, status=400)
        
class ReadCSVFile(APIView):
    @csrf_exempt
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return JsonResponse({'error': 'No file provided'}, status=400)
        print(file)
        required_columns = ['NAME', 'MARKS']  # Replace with your required column names
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file, sep=',', on_bad_lines='skip', encoding='utf-8')
        
        # Check if the DataFrame is empty
        if df.empty:
            return JsonResponse({'error': 'Empty CSV file'}, status=400)
        
        print(df.columns)
        missing_columns = [col for col in df.columns if str(col).upper() not in required_columns]
        print("missing_columns", missing_columns)
        if missing_columns:
                return JsonResponse({'error': f'Missing required columns: {missing_columns}'}, status=400)
        df.columns = [col.strip().lower() for col in df.columns]
        column_mapping = {'name': 'student_name', 'marks': 'subject_marks'}
        df.rename(columns=column_mapping, inplace=True)
        # Convert DataFrame to JSON
        data_json = df.to_json(orient='records')
        
        # Return the JSON response
        return JsonResponse(json.loads(data_json), safe=False)

class GetUploadedData(APIView):
    @csrf_exempt
    def get(self, request):
        data = models.SubjectMetaData.objects.all()
        serializer_data = serializers.SubjectMetaDataSerializer2(data, many=True)
        return JsonResponse(serializer_data.data, safe=False)
