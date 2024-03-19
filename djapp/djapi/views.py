from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Expense, Budget
from .serializers import ExpenseSerializer, BudgetSerializer
from rest_framework.decorators import api_view




# Create your views here.

class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    def get_permissions(self):
        return []
   

    
class ExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    def get_permissions(self):
        return []
   

class BudgetListCreateView(generics.ListCreateAPIView):
    queryset = Budget.objects.filter(user=None)
    serializer_class = BudgetSerializer
    def get_permissions(self):
        return []
    

class BudgetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer 
    def get_permissions(self):
        return []

