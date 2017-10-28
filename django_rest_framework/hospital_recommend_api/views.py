from django.shortcuts import render

from django.views import generic

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# # Create your views here.
# class IndexView(generic.ListView):
# 	template_name = 'hospital_recommend_api/index.html' # plugin template
# 	# context_object_name = 'all_albums' # overide default get_queryset return variable name: 
# 	# 								   # 'object_list' to 'all_albums' that pass to template_name('hospital_recommend_api/index.html') 

# 	def get_queryset(self):
# 		return null=True

def index(request):
	return render(request, 'hospital_recommend_api/index.html')

	#all_albums = Album.objects.all()	# Use api to get all object in Album database 
	#return render(request, 'hospital_recommend_api/index.html', {'all_albums': all_albums,})		

	#### same as
	# all_albums = Album.objects.all()	# Use api to get all object in Album database 
	# template = loader.get_template('hospital_recommend_api/index.html')
	# context = {
	# 	'all_albums': all_albums,
	# }
	# return HttpResponse(template.render(context, request))


class HospitalRecommend(APIView):
    def get(self, request, *args, **kw):
        print("calling get method of HospitalRecommend")
        # Any URL parameters get passed in **kw
        result = {"hello": "123456"}
        response = Response(result, status=status.HTTP_200_OK)
        return response

    def post(self, request, *args, **kw):
        print("calling post method of HospitalRecommend")
        data = request.data
        pred = data
        result = {"result": pred}
        response = Response(result, status=status.HTTP_200_OK)
        return response  

