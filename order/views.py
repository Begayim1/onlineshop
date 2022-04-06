from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import request


# if request.method == 'POST':
#     form = MyForm(request.POST)
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.user = request.user
#         obj.save()
#         return HttpResponseRedirect('obj_list')