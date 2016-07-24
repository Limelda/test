from django.shortcuts import render

def post_list(request):
    return render(request, 'plist/post_list.html', {})
