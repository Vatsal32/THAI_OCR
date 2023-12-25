from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from .models import OCRRecord, MyModel
from .serializers import OCRRecordSerializer
from .img_processing.main import THAI_ID_CARD

@api_view(["POST"])
def createOCRRecord(request):
    try:
        file = request.data['file']
        img = MyModel.objects.create(image_url=file)
        reader = THAI_ID_CARD()
        result = reader.readFrontImage('./' + str(img.image_url))
            
        temp = OCRRecordSerializer(data={
            "id_num": reader.cardInfo['mix']["Identification_Number"],
            "firstName": reader.cardInfo['mix']["NameEN"],
            "prefix": reader.cardInfo['mix']["PrefixEN"],
            "lastName": reader.cardInfo['mix']["LastNameEN"],
            "dateOfBirth": reader.cardInfo['mix']["BirthdayEN"],
            "expiryDate": reader.cardInfo['mix']["DateOfExpiryEN"],
            "issueDate": reader.cardInfo['mix']["DateOfIssueEN"]
        })
            
        if temp.is_valid():
            temp.save()
            return Response({"message": "Success", "result": temp.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid Image"})                 
    except KeyError:
        raise ParseError('Request has no file attached')
    except Exception as e:
        return Response({"message": "Something went wrong", "errors": e.message()})
        
@api_view(['GET'])
def getOCRRecord(request):
    if request.query_params:
        items = OCRRecord.objects.filter(**request.query_params.dict())
    else:
        items = OCRRecord.objects.all()
        
    if items:
        serializer = OCRRecordSerializer(items, many=True)
        return Response({ "message": "Success", "data": serializer.data })
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    
@api_view(['POST'])
def updateOCRRecord(request, pk):
    record = OCRRecord.objects.get(pk=pk)
    data = OCRRecordSerializer(instance=record, data=request.data.dict())
    
    if (data.is_valid()):
        data.save()
        return Response({"message": "Success", "data": data.data})
    else:
        return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def deleteOCRRecord(request, pk):
    item = get_object_or_404(OCRRecord, pk=pk)
    item.delete()
    return Response({ "message": "Success" }, status=status.HTTP_202_ACCEPTED)
