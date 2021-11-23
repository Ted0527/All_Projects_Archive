import json,re

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from .validation            import Validation_email, Validation_password
from .models                import User

class SignUpView(View) :
    
    def post(self, request):
        try: 
            data           = json.loads(request.body)
            email          = data['email']
            password       = data['password']
            
            Validation_email(email)
            Validation_password(password)

            User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = data['password'],
                phone    = data['phone'],
                mbti     = data.get('mbti', '')
                )    
            
            return JsonResponse({"message" : "SUCCESS"}, status = 201)        
        
        except ValidationError as e : 
            return JsonResponse({"message" : e.message }, status=400)
        except KeyError :
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

class SignInView(View) :
   def post(self, request) :
        try :
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']
            if not User.objects.filter(email=email, password=password).exists() :
                return JsonResponse({"message" : "INVALID_USER"}, status=401)
            return JsonResponse({"message" : "SUCCESS"}, status=200)
        
        except User.DoesNotExist :
            return JsonResponse({"message" : "INVALID_USER"}, status=401)
        except KeyError :
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)