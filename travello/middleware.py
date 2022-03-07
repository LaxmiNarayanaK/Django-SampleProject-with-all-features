def CustomMiddleware(get_response):
    
    def middleware(request):
        response=get_response(request)
        print("Source of Request is: ",request.META['HTTP_USER_AGENT'])
        return response
    return middleware