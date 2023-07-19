from django.shortcuts import render, get_object_or_404
from .models import Conversation, Message

def conversation_view(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    messages = conversation.messages.all()
    return render(request, 'messaging/conversation.html', {'conversation': conversation, 'messages': messages})
