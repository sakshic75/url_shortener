from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from app.models import Url
import json


# GET  API to handle the short url redirection to the long url
# Redirection
@csrf_exempt
def redirection(request, unique_key):
    url_objects = Url.objects.filter(unique_key=unique_key)
    # check if the short url is present or not
    exists = ""
    if len(url_objects) > 0:
        if url_objects[0].unique_key == unique_key:
            long_url = url_objects[0].long_url
            exists += "exists"
            return HttpResponseRedirect(long_url)
        else:
            exists += "not exists"

    return HttpResponse("Short url you entered is not correct")


# Post API to get the long url entered by the user
@csrf_exempt
def url(request):
    if request.method == "POST":
        # Get the post data
        json_data = json.loads(request.body)
        long_url_string = json_data["long_url"]
        # For storing short url
        result = ""

        # Checking if long url exists in tha database
        url_object = Url.objects.filter(long_url=long_url_string)
        if len(url_object) > 0:
            print(len(url_object))
            result += request.build_absolute_uri() + "/" + str(url_object[0].unique_key)
            # If long url did not exists in the database, returns the short url
        else:
            count = Url.objects.all().count()
            # Getting the short url from the method
            short_url = generate_url(request.build_absolute_uri(), count+1)
            url_object = Url()

            url_object.long_url = long_url_string
            url_object.num = count+1
            url_object.unique_key = generate_key(count+1)

            # Saving data to the database
            url_object.save()
            result += short_url
        return HttpResponse(result)


# Method to generate the short url
# Alog:
# getting the count of the objects in the Url Model
# (this will show the number of urls in the database)
# converting it into a base 62 unique id
# and hence creating a unique url by incrementing the count by 1 everytime
def generate_url(link, count):
    # scaling the base
    base_key = ""
    array_rem = []
    while count > 0:
        r = count % 62
        count = count//62
        array_rem.append(r)

    for i in range(len(array_rem)-1, -1, -1):
        base_key = base_key + str(get_char(array_rem[i]))

    return link + "/" + base_key


# Create a list of key and value based on 62 base
def create_list_of_62():
    list_62_base = {}
    short_char = 97
    long_char = 65
    integer_num = 0
    for i in range(0, 25):
        list_62_base[i] = chr(short_char)
        short_char += 1
    for i in range(26, 52):
        list_62_base[i] = chr(long_char)
        long_char += 1
    for i in range(52, 62):
        list_62_base[i] = integer_num
        integer_num += 1
    return list_62_base


# Return the value corresponding to the key
def get_char(r):
    list_of_62 = create_list_of_62()
    for i in list_of_62:
        if i == r:
            return list_of_62[i]


def generate_key(count):
    # scaling the base
    base_key = ""
    array_rem = []
    while count > 0:
        r = count % 62
        count = count//62
        base_key = base_key + str(get_char(r))
        array_rem.append(r)

    for i in range(len(array_rem)-1, -1, -1):
        base_key = base_key + str(get_char(array_rem[i]))

    return base_key
