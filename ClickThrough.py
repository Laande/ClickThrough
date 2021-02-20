import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction, HMessage

extension_info = {
    "title": "Click Through",
    "description": ":ct | Only Habbix.ws / Leet.ws",
    "version": "2.0",
    "author": "Lande"
}

ext = Extension(extension_info, sys.argv)
ext.start()

def speech(message):
    (text, color, index) = message.packet.read('sii')
    if (text == ':ct'):
        message.is_blocked = True
        ext.send_to_client("{l}{h:1446}{i:0}{s:\"' :ct on ' or ' :ct off '\"}{i:0}{i:1}{i:0}{i:0}")
    if (text == ':ct on'):
        message.is_blocked = True
        ext.send_to_client("{l}{u:448}{b:true}")
        ext.send_to_client("{l}{h:1446}{i:0}{s:\"Click Through Enabled !\"}{i:0}{i:1}{i:0}{i:0}")
    if (text == ':ct off'):
        message.is_blocked = True
        ext.send_to_client("{l}{u:448}{b:false}")
        ext.send_to_client("{l}{h:1446}{i:0}{s:\"Click Through Disabled !\"}{i:0}{i:1}{i:0}{i:0}")

ext.intercept(Direction.TO_SERVER, speech, 1314)
