from django.shortcuts import render

# from . fixer_api import get_exchange_rate
# # Create your views here.


# def exchange_rate_view(request):
#     base_currency = 'USD'
#     target_currency = 'EUR'
#     rate = get_exchange_rate(base_currency, target_currency)
#     context={'rate':rate}
#     return render(request, 'exchange/exchange_view.html', context)
  
def exchange(request):
  
    return render(request,'exchange/exchange.html')
