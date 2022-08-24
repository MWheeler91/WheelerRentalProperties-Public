from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.generics import GenericAPIView


from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserCreateSerializer


# from .filters import PropertyFilter
# Create your views here.


# class AccountHomeView(TemplateView):
#     template_name = 'account/account_home.html'


class RegisterView(GenericAPIView):
    serializer_class = UserCreateSerializer
    authentication_classes = []

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'message': "User created!",
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            print(serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request: Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user=authenticate(email=email, password=password)

        if user is not None:
            response = {
                'message': 'Login Success',
                'token': user.auth_token.key,
                'first_name': str(request.user.first_name),
                'last_name': str(request.user.last_name),
                'is_admin': str(request.user.is_admin)
            }
            print(response)
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data={'message':  'invalid user'}, status=status.HTTP_200_OK)

    def get(self, request: Request):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
            'first_name': str(request.user.first_name),
            'last_name': str(request.user.last_name),
            'is_admin': str(request.user.is_admin)
        }
        return Response(data=content, status=status.HTTP_200_OK)
# def registerPage(request):
#     form = CreateUserForm()
#
#     if request.method == "POST":
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             new_user = authenticate(username=form.cleaned_data['email'],
#                                     password=form.cleaned_data['password1'],)
#             login(request, new_user)
#
#             return redirect('base:home')
#         # return redirect('account:login')
#     context = {'form': form}
#     return render(request, 'auth/register.html', context)
#

# class ResetPasswordView(PasswordResetView):
#     email_template_name = 'auth/password_reset_email.html'
#     success_url = reverse_lazy('password_reset_done')
#
#
# class ResetPasswordDoneView(PasswordResetDoneView):
#     template_name = 'auth/password_reset_done.html'

