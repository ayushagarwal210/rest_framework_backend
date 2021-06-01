from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.


@api_view(['GET'])
def get_book(request):
    book_obj = Book.objects.all()
    serializer = BookSerializer(book_obj, many=True)
    return Response({'status': 200, 'payload': serializer.data})


class StudentAPI(APIView):
    def get(self, request):
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.errors,  'message': 'Something went wrong'})

        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'You sent'})

    def put(self, request):
        pass

    def patch(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])

            serializer = StudentSerializer(
                student_obj, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response({'status': 403, 'error': serializer.errors,  'message': 'Something went wrong'})

            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'You sent'})

        except Exception as e:
            return Response({'status': 403, 'message': 'invalid id'})

    def delete(self, request):
        try:
            id = request.GET.get('id')
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({'status': 200, 'message': 'deleted'})

        except Exception as e:
            return Response({'status': 403, 'message': 'invalid id'})


# @api_view(['GET'])
# def index(request):
#     student_obj = Student.objects.all()
#     serializer = StudentSerializer(student_obj, many=True)
#     return Response({'status': 200, 'payload': serializer.data})


# @api_view(['POST'])
# def post_student(request):
#     serializer = StudentSerializer(data=request.data)

#     if not serializer.is_valid():
#         return Response({'status': 403, 'error': serializer.errors,  'message': 'Something went wrong'})

#     serializer.save()
#     return Response({'status': 200, 'payload': serializer.data, 'message': 'You sent'})


# @api_view(['PATCH'])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)

#         serializer = StudentSerializer(
#             student_obj, data=request.data, partial=True)

#         if not serializer.is_valid():
#             return Response({'status': 403, 'error': serializer.errors,  'message': 'Something went wrong'})

#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data, 'message': 'You sent'})

#     except Exception as e:
#         return Response({'status': 403, 'message': 'invalid id'})


# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status': 200, 'message': 'deleted'})

#     except Exception as e:
#         return Response({'status': 403, 'message': 'invalid id'})
