from telethon import TelegramClient, events
import json
import requests

APP_ID= your app id #my.telegram.org
APP_HASH='your api hash' #my.telegram.org
BOTT='your bot token '#@botfather

bot = TelegramClient('bot', APP_ID, APP_HASH).start(bot_token=BOTT)



def staat(qq):
  url = "https://api.telegram.org/bot"+BOTT+"/sendphoto"
  data = {
    "chat_id": str(qq),
    "photo":"https://telegra.ph/file/cb8084323dcd0b7b65a6f.jpg",
    "caption": " Get instant access to Corona in Sri Lanka 🇱🇰. 📊 Automatically retrieve the latest corona information after adding it to the SLCovid19slbzonebot 😷 to your  Group. Use   /help   for more information.",
    "parse_mode": "HTML",
    "reply_markup":{
        "inline_keyboard": [ 
            [
                {
                    "text": "➕ Add me to your Group 🦠 ",
                    "url": "https://t.me/SLCovid19slbzonebot?startgroup=new"
                }, 
                {
                    "text": "📦 Ho to create your one  ",
                    "url": "https://www.youtube.com/channel/UCvYfJcTr8RY72dIapzMqFQA"
                }
            ]
        ]
    }
}
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)

def staa():
    r = requests.get('https://hpb.health.gov.lk/api/get-current-statistical')
    jsondata = json.loads(r.text)
    update_date_time    = str(jsondata['data']['update_date_time'])
    local_new_cases     = str(jsondata['data']['local_new_cases'])
    local_active_cases  = str(jsondata['data']['local_active_cases'])
    local_total_cases   = str(jsondata['data']['local_total_cases'])
    local_deaths        = str(jsondata['data']['local_deaths'])
    local_recovered     = str(jsondata['data']['local_recovered'])
    local_total_number_of_individuals_in_hospitals = str(jsondata['data']['local_total_number_of_individuals_in_hospitals'])
    global_new_cases    = str(jsondata['data']['global_new_cases'])
    global_total_cases  = str(jsondata['data']['global_total_cases'])
    global_deaths       = str(jsondata['data']['global_deaths'])
    global_new_deaths   = str(jsondata['data']['global_deaths'])
    global_recovered    = str(jsondata['data']['global_recovered'])

    textt = str(
                    '<b>CURRENT SITUATION</b>' + '\n' + '\n' + '<b>' +
                    update_date_time + ' now </b>' + '\n' + '\n' +
                    '<b>🇱🇰 Situation in Sri Lanka</b>' + '\n' + '\n'  +
                    '🤒 Number of confirmed patients (cumulative) = ' + '<code>' +
                    local_total_cases + '</code>' + '\n' +
                    '🤕 Number of patients receiving treatment = ' + '<code>' + local_active_cases + '</code>' +
                    '\n' + '😷 Number of new patients = ' + '<code>' + local_new_cases + '</code>' +
                    '\n' +
                    '🏥 Persons currently under investigation in hospitals = ' + '<code>' +
                    local_total_number_of_individuals_in_hospitals +  '</code>' + '\n' +
                    '🙂 The number who recovered and left = ' + '<code>' + local_recovered + '</code>' + 
                    '\n' + '⚰ Number of deaths= ' + '<code>'  + local_deaths + '</code>' + '\n' +
                    '\n' + '<b>🌎 Worldwide status</b>' + '\n' +
                    '\n' + '🤒 Number of confirmed patients (cumulative) = ' '<code>'  +
                    global_total_cases + '</code>' + '\n' + '😷 Number of new patients= ' '<code>'  +
                    global_new_cases + '</code>' + '\n' + '⚰ Number of deaths = ' '<code>'  +
                    global_deaths + '</code>' + '\n' + '🙂 Healed number = ' '<code>'  +
                    global_recovered + '</code>' + '\n' + '\n' + '\n' +
                    '✅ All information is provided by the government and reputable sources' + '\n' +
                    '~ @sl_bot_zone 🇱🇰 ~'),
    return textt
def sta():
         r = requests.get(f"https://corona.lmao.ninja/v2/countries/{variabla}").json()
         reply_text = f"**රට {r['country']} 🦠**\n🤒 Number of confirmed patients (cumulative)= {r['cases']:,}\n😷 Number of new patients = {r['todayCases']:,}\n⚰ Number of deaths = {r['deaths']:,}\n⚰ New death  = {r['todayDeaths']:,}\n🙂 Healthed number =  {r['recovered']}"
         message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)



@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    staat(event.original_update.message.peer_id.user_id)
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/corona'))
async def corona(event):
    await event.respond(staa(),parse_mode='html')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/corona {variabla}'))
async def corona(event):
    await event.respond(sta(),parse_mode='MARKDOWN')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/help'))
async def help(event):
    await event.respond('Use the /corona command to view the latest corona news')
    raise events.StopPropagation

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
