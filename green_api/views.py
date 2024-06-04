from django.shortcuts import render

import requests


API_URL = 'https://1103.api.green-api.com/waInstance'
title = "GREEN-API"


    
def make_requests(request, method, url, payload, headers):

    response = requests.request(method, url, headers=headers, data = payload)

    if response.status_code == 200:
        data = response.text
    else:
        data = {
            "Error": response.status_code, 
            "Reason": response.reason
        }
    
    context = {
        'title': title,
        'data': data
    }
    return render(request, 'index.html', context)

def index(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        idInstance = request.POST.get('idInstance')
        apiTokenInstance = request.POST.get('ApiTokenInstance')

        url = f"{API_URL}{idInstance}/{action}/{apiTokenInstance}"


        if action == 'getSettings':

            method = "GET"
            return make_requests(request, method, url, payload = {}, headers= {})
        

        elif action == 'getStateInstance':

            method = "GET"
            return make_requests(request, method, url, payload = {}, headers= {})
        
        
        elif action == 'sendMessage':

            method = "POST"

            chat_id = request.POST.get('chatIdSendMessage')
            mes = request.POST.get('message')

            payload = "{\r\n\t\"chatId\": \"%s\",\r\n\t\"message\": \"%s\"\r\n}" % (chat_id, mes)

            headers = {
                'Content-Type': 'application/json'
            }

            return make_requests(request, method, url, payload, headers)
        

        elif action == 'sendFileByUrl':

            method = "POST"

            chat_id = request.POST.get('chatIdSendFileByUrl')
            mes = request.POST.get('urlFile')
            
            payload = "{\r\n   \t\"chatId\": \"%s\",\r\n\t\"urlFile\": \"%s\",\r\n\t\"fileName\": \"%s\"\r\n}" % (chat_id, mes, mes)

            headers = {
                'Content-Type': 'application/json'
            }

            return make_requests(request, method, url, payload, headers)

    context = {
        'title': title,
    }
    return render(request, 'index.html', context)