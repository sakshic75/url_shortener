# url_shortener

The project is about generating a short url to the corresponding long url and also redirecting the short url to the long url whenever user hits the long url 
Project is created using Django framework of python .


#Intalling 
Assuming you have pip,virtualenv, and django installed 

(whatever dir you wanna save 'C:/' is just for reference  )

C:/>mkdir django_pro

C:/>cd django_pro

C:/django_pro>git clone https://github.com/sakshic75/url_shortener.git

C:/django_pro>cd url_shortener

C:/django_pro/url_shortener>python manage.py migrate 

C:/django_pro/url>python manage.py runserver 


Model used:

Url 
Field 1 - long_url 

Field 2 - short_url

Field 3 - num


#URLs 

#Post request

1) http://localhost:8000/url 

Post data = application/JSON

raw data
{
"long_url":"http://www.google.com"  //Any working url 
}
Response -

A Short URL(String)


2) Get request 

Enter the short url you got from the response 

response - Redirection to the long url



Thank you 
