import os 
import telegram
import json

bot = telegram.Bot(token=os.environ["TOKEN"])
data_mon = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
with open("./pan_data.json") as json_file:
    source_data = json.load(json_file)

def thithi(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(request),bot)
        chat_id = update.message.chat.id
        complete_message = update.message.text.split(' ')
        print('Received msg: ', complete_message)
        if complete_message[0] == '/tithi':
            res_text = getTithi(complete_message[1])
        elif complete_message[0] == '/start':
            res_text = 'Hello! I am bot, please use /help to know what I can do'
        elif complete_message[0] == '/help':
            res_text = 'I give the Tithi,  Nakshatra and other details for the given date of the current year(2019).\n To request send a command as /tithi <mm-dd-yyyy>'
        else:
            res_text = 'Invalid command entered, please use /help'
            
        bot.sendMessage(chat_id=chat_id,text=res_text)
    return f'ok'


def getTithi(date_value):
    #function to get the tithi
    req_date = date_value.split('-')
    if(req_date[2] != '2019'):
    	res_text = 'I can only give you 2019 details'
    else:
        list_name = 'panchangam_'+ data_mon[int(data[0])-1]
        print(json.dumps(source_data[list_name][int(data[1])-1],indent=4))
        tih_value = 'Thithi: ' + source_data[list_name][int(data[1])-1].Thithi + '\n'
        nak_value = 'Nakshatram: ' + source_data[list_name][int(data[1])-1].Nakshatram + '\n'
        dur_value = 'Durmuhurtam: ' + source_data[list_name][int(data[1])-1].Durmuhurtam + '\n'
        rah_value = 'Rahukalam: ' + source_data[list_name][int(data[1])-1].Rahukalam + '\n'
        var_value = 'Varjam: ' + source_data[list_name][int(data[1])-1].Varjam + '\n'
    	res_text = tih_value + nak_value + dur_value + rah_value + var_value
    return(res_text)
