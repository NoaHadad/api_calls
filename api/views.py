from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import QuoteSerializer
from .models import Quote,QuoteLog 

from django.db.models import Q

from threading import Lock
log_lock=Lock()

#errors dictionary
errors={1:"quote with this name already exists",
        2:"input is not valid",
        3:"quote does not exist"}

#the function gets log and writes it to the err_log file
def write_log(new_log):

    global log_lock
    log_lock.acquire(timeout=30)
    file=open("err_logs.txt","a")
    file.write(str(new_log)+"\n")
    log_lock.release()

#the function gets index of error, writes the error to log_file and returns the error
def err(index):

    error={"errorCode": index,"description": errors[index], "level": "error"}
    write_log(error)
    return error


# Create your views here.


#api options
@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/quote-list/',
        'Detail View':'/quote-detail/<str:pk>/',
        'Create':'/quote-create/',
        'update':'/quote-update/',
        'Delete':'/quote-delete/<str:pk>/',
        }
    return Response(api_urls)


#returning the quotes which are not deleted
@api_view(['GET'])
@permission_classes((IsAuthenticated,))     
def quotesList(request):

    quotes=Quote.objects.filter(deleted=0).all()
    serializer=QuoteSerializer(quotes,many=True)
    return Response(serializer.data)


#returning quote with specific name
@api_view(['GET'])
@permission_classes((IsAuthenticated,))     
def quoteDetail(request,pk):

    try:
       quote=Quote.objects.get(Q(name=pk) & Q(deleted=0))
    except:
       return Response("Quote doesn't exist")

    serializer=QuoteSerializer(quote)
    return Response(serializer.data)


#creating quote
@api_view(['POST'])
@permission_classes((IsAuthenticated,))     
def quoteCreate(request):

    #getting data
    serializer=QuoteSerializer(data=request.data)

    #checkng validation
    if serializer.is_valid():

       #checking if the quote already exists
       try:

            exists=Quote.objects.get(name=serializer.data['name'])

            #check if the quote was deleted
            if (exists.deleted==1):
                 exists.price=serializer.data['price']
                 exists.deleted=0
                 exists.items=serializer.data['items']  
                 exists.save()
                 QuoteLog.objects.create(message=["Quote has been created"],operation=0,quote_id=exists.id)
                 return Response("Quote has been created")

            #quote was not deleted
            else:
                 QuoteLog.objects.create(message=[errors[1]],error_code=[1],operation=0,quote_id=exists.id)
                 return Response(err(1))

       #quote does not exist
       except:
            
            q=Quote.objects.create(name=serializer.data['name'],price=serializer.data['price'],items=serializer.data['items'])
            QuoteLog.objects.create(message=["Quote has been created"],operation=0,quote_id=q.id)
            return Response("Quote has been created")

    #data is not valid

    #quote with this name already exists
    try:
          exists=Quote.objects.get(Q(name=serializer.data['name']) & Q(deleted=0))
          QuoteLog.objects.create(error_code=[1,2],message=[errors[1],errors[2]],operation=0,quote_id=exists.id)
          errs=[err(1),err(2)]
          return Response(errs)

    #quote with this name doesn't exist
    except:
          QuoteLog.objects.create(error_code=[2],message=[errors[2]],operation=0)
          return Response(err(2))


#deleting quote
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))     
def quoteDelete(request,pk):

    #checking if quote exists
    try:
       quote=Quote.objects.get(Q(name=pk) & Q(deleted=0))

    #quote does not exist
    except:
       QuoteLog.objects.create(message=[errors[3]],error_code=[3],operation=2)
       return Response(err(3))

    #soft deletion
    quote.deleted=1
    quote.save()

    QuoteLog.objects.create(message=["Quote has been deleted"],operation=2,quote_id=quote.id)
    return Response("Quote has been deleted")


#updating quote
@api_view(['POST'])
@permission_classes((IsAuthenticated,))     
def quoteUpdate(request):

    serializer=QuoteSerializer(data=request.data)

    #checkng validation
    if serializer.is_valid():

        #checking if the quote exists
        try:
            exists=Quote.objects.get(Q(name=serializer.data['name']) & Q(deleted=0))

        #if the quote does not exist
        except:
            QuoteLog.objects.create(message=[errors[3]],error_code=[3],operation=1)
            return Response(err(3))

        #if the quote exists
        exists.price=serializer.data['price'] 
        exists.items=serializer.data['items']
        exists.save()
        QuoteLog.objects.create(message=["Quote has been updated"],operation=1,quote_id=exists.id)
        return Response("Quote has been updated")

    #not valid

    #quote exists
    try:
            exists=Quote.objects.get(Q(name=serializer.data['name']) & Q(deleted=0))
            QuoteLog.objects.create(message=[errors[2]],operation=1,error_code=[2],quote_id=exists.id)
            return Response(err(2))

    #quote doesn't exist
    except:
            QuoteLog.objects.create(message=[errors[2],errors[3]],operation=1,error_code=[2,3])
            errs=[err(2),err(3)]
            return Response(errs)

