from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def chat_view(request):
    messages = Message.objects.all()
    return render(request, 'chat/chat.html', {'messages': messages})

def send_message(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            message = Message(text=text)
            message.save()
            return JsonResponse({'status': 'OK'})
    return JsonResponse({'status': 'ERROR'})
