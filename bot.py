
from pyrogram import Client, filters
from truecallerpy import search_phonenumber
import re
id = "a2i0H--bsDYqhFMFcXSk-tVykJleH_U2Qfz8RwhTujiofGGodRbk2DKOP6_eRg71"
API_ID = "7280833"
API_HASH = "faa0e3b6d30779426d833dec02ab70d9"
TOKEN = "1969982366:AAHoE4d2bnRem_Ng8pL694z_jHQAXMJB6LA"
print("bot Started succes fully ❣❣❣♥")
app = Client("tagremover", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH)



@app.on_message(filters.private & filters.text & filters.create(
    lambda _, __, message: bool(re.match(r'^(\+91|91|\+91\s)?(\d{4}|\d{3})\s?\d{3}\s?\d{3}$', message.text.strip()))
))
async def tag(client, message):
    a = search_phonenumber(str(message.text),"IN", id)
    b =['Truecaller result\n\n']
    if a is not None and 'data' in a and len(a['data']) > 0 and 'name' in a['data'][0]:
        b.append("Name: " +  a['data'][0]['name'])
    if 'gender' in a['data'][0]:
        b.append("Gender:"+ a['data'][0]['gender'])
    if 'image' in a['data'][0]:
        b.append("Image URL:"+ a['data'][0]['image'])
    if 'phones' in a['data'][0] and len(a['data'][0]['phones']) > 0 and 'carrier' in a['data'][0]['phones'][0]:
        b.append("Carrier:"+ a['data'][0]['phones'][0]['carrier'])
    if 'internetAddresses' in a['data'][0] and len(a['data'][0]['internetAddresses']) > 0 and 'id' in a['data'][0]['internetAddresses'][0]:
        b.append("Email ID:"+ a['data'][0]['internetAddresses'][0]['id'])
    await client.send_message(
        chat_id=message.chat.id,
        text='\n'.join(b),
        reply_to_message_id=message.id
    )
app.run()
