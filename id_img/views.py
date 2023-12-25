from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from .models import OCRRecord
from .img_processing.main import THAI_ID_CARD

@api_view(["POST"])
def createOCRRecord(request):
    try:
        file = request.data['file']
        img = OCRRecord.objects.create(image_url=file)
        reader = THAI_ID_CARD()
        result = reader.readFrontImage('./' + str(img.image_url))
        img.firstName = reader.cardInfo['mix']["NameEN"]
        img.prefix = reader.cardInfo['mix']["PrefixEN"]
        img.lastName = reader.cardInfo['mix']["LastNameEN"]
        img.dateOfBirth = reader.cardInfo['mix']["BirthdayEN"]
        img.expiryDate = reader.cardInfo['mix']["DateOfExpiryEN"]
        img.issueDate = reader.cardInfo['mix']["DateOfIssueEN"]
            
        img.save()
            
        return Response({"message": "Hello World!", "result": img.data}, status=status.HTTP_200_OK)
    except KeyError:
        raise ParseError('Request has no file attached')
    except Exception as e:
        return Response({"message": "Something went wrong", "errors": e.message()})

class Id_Img_API(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({"message": "Hello World!"}, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            file = request.data['file']
            img = OCRRecord.objects.create(image_url=file)
            reader = THAI_ID_CARD()
            result = reader.readFrontImage('./' + str(img.image_url))
            img.firstName = reader.cardInfo['mix']["NameEN"]
            img.prefix = reader.cardInfo['mix']["PrefixEN"]
            img.lastName = reader.cardInfo['mix']["LastNameEN"]
            img.dateOfBirth = reader.cardInfo['mix']["BirthdayEN"]
            img.expiryDate = reader.cardInfo['mix']["DateOfExpiryEN"]
            img.issueDate = reader.cardInfo['mix']["DateOfIssueEN"]
            
            img.save()
            
            return Response({"message": "Hello World!", "result": img.data}, status=status.HTTP_200_OK)
        except KeyError:
            raise ParseError('Request has no file attached')
        except Exception as e:
            return Response({"message": "Something went wrong", "errors": e.message()})
        
