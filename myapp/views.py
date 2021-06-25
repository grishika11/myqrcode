from django.shortcuts import render
from qrcode import*


data = None
# Create your views here.
def Home(request):
	global data
	if request.method == 'POST':
		data = request.POST['data']
		
		img =  make(data)
		img.save("myapp/static/images/test.png")
        
	else:
		pass
	return render(request,'home_qr.html',{'data':data})