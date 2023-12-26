import pyrogram , pyromod
from config import Config 
from pyromod import listen

from pyrogram import Client, filters, enums
from kvsqlite.sync import Client as dt
p = dict(root='plugins')
tok = '6787244681:AAG4OuJhLXuxN4S-aAvIggIn0SiCaZLv6kM' ## توكنك 
id = 5997250376 ## ايديك
db = dt("data.sqlite", 'fuck')
if not db.get("checker"):
  db.set('checker', None)
if not db.get("admin_list"):
  db.set('admin_list', [id, 5997250376, 6581896306])
if not db.get('ban_list'):
  db.set('ban_list', [])
if not db.get('sessions'):
  db.set('sessions', [])
if not db.get('force'):
  db.set('force', ['sx4xx'])
x = Client(name='loclhosst', api_id=25721707, api_hash='c6a2826bd6bce80a2ea20a444fe2a934', bot_token=tok, workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)

x.run()