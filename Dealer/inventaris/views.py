from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import inventaris
from .serializers import inventarisSerializer


@api_view(['GET', 'POST'])
def inventaris_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        inventariss = inventaris.objects.all()
        serializer = inventarisSerializer(inventariss, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = inventarisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)