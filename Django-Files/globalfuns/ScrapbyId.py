import os

def scrapNdump(data,model,serializer):
    # print(data,model.__name__,serializer.__name__)
    snippet = model.objects.get(id=data['id'])
    serializer = serializer(snippet)
    filename=serializer.data['filename']+'.py'
    exec(open("E:\Zigram\Training\Django-Files\Data\\"+filename).read())

