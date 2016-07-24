from django.shortcuts import render

# returns a function render that will put together the template
def post_list(request):
	return render(request, 'blog/post_list.html',{})
