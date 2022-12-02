from django.shortcuts import render
from . models import Stocks
from django.views.generic import CreateView


# Create your views here.
def index(request):
    
    print('indexin başı')
    print(request.method)
    stocks = Stocks.objects.all()
    
    stock_list = []
    for i in range(0,len(stocks)):
        stock_list.append(stocks[i].stock)
      
    stock_list = set(stock_list)
    stock_list = sorted(stock_list)
    
    print('tüm stocklar geldi')
    print(len(stock_list))

    var = request.POST.getlist('program')
    print(list(request.POST.items()))
    print(var)
    print(len(var))

    if len(var) > 0:
        print('var boş değilmiş')
        selected_stock = var
        stocks = Stocks.objects.filter(stock = selected_stock[0])
    else:
        print("var boşmuş")
        selected_stock = 'AEFES'
        stocks = Stocks.objects.filter(stock = selected_stock)
    
    #stocks = Stocks.objects.filter(stock = selected_stock[0])
    #stocks = Stocks.objects.filter(stock = 'AEFES')



    context = {
        'stocks' : stocks,
        'stock_list': stock_list,
        'selected_stock': selected_stock
    }

    return render(request, 'testdb/index.html', context)


#class My_Model_Form(ModelForm):  
#           class Meta:  
#               model = My_Model 


def gelir(request):
    
    print('indexin başı')
    print(request.method)
    stocks = Stocks.objects.all()
    
    stock_list = []
    for i in range(0,len(stocks)):
        stock_list.append(stocks[i].stock)
      
    stock_list = set(stock_list)
    stock_list = sorted(stock_list)
    
    print('tüm stocklar geldi')
    print(len(stock_list))

    var = request.POST.getlist('program')
    print(list(request.POST.items()))
    print(var)
    print(len(var))

    if len(var) > 0:
        print('var boş değilmiş')
        selected_stock = var
        stocks = Stocks.objects.filter(stock = selected_stock[0])
    else:
        print("var boşmuş")
        selected_stock = 'AEFES'
        stocks = Stocks.objects.filter(stock = selected_stock)
    
    #stocks = Stocks.objects.filter(stock = selected_stock[0])
    #stocks = Stocks.objects.filter(stock = 'AEFES')



    context = {
        'stocks' : stocks,
        'stock_list': stock_list,
        'selected_stock': selected_stock
    }

    return render(request, 'testdb/gelir.html', context)