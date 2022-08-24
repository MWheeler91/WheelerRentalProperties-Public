from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person, Property, PropertyImage
from .serializers import PersonSerializer, PropertySerializer, PropertyImagesSerializers, PropertyDetailsSerializer
import datetime
# Create your views here.

# @api_view(['GET'])
# def getData(request):
#     person = Person.objects.all()
#     serializer = PersonSerializer(person, many=True)
#     return Response(serializer.data)


@api_view(['GET'])
def getProperties(request):
    properties = Property.objects.all()
    for date in properties:
        if date.available_date:
            dt_obj = date.available_date
            formatted_dt_object = dt_obj.strftime(f"%B %#d{set_suffix(dt_obj.day)} %Y")
            date.available_date = formatted_dt_object
    serializer = PropertySerializer(properties, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getImages(request, propertyID):
    images = PropertyImage.objects.all().filter(property=propertyID)
    serializer = PropertyImagesSerializers(images, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPropertyDetails(request, slug):
    property_details = Property.objects.get(slug=slug)
    print(property_details.available_date)
    # for date in property_details:
    if property_details.available_date:
        dt_obj = property_details.available_date
        formatted_dt_object = dt_obj.strftime(f"%B %#d{set_suffix(dt_obj.day)} %Y")
        property_details.available_date = formatted_dt_object
    else:
        pass
    serializer = PropertyDetailsSerializer(property_details, many=False)
    return Response(serializer.data)


# @api_view(['GET'])
# def getProperty(request):
#     properties = Property.objects.all()


# ------------------------ CUSTOM FUNCTIONS ------------------------
def set_suffix(day):
    suffix = ""
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return suffix

