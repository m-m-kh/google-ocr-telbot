from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from telegram import Update
from google_drive_ocr.main2 import async_orc
import os
from pdfpng.main import extract_png
DIR = os.path.dirname(__file__)

from time import time

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    text = """Welcome to OCR bot
  send me a pdf/png/jpg file to extract text;
  attention:max file's size 2MB;"""
    await update.message.reply_text(text)
    try:
        os.makedirs(str(update.message.from_user.id))
    except:
        pass
async def recive_file(update:Update, context:ContextTypes.DEFAULT_TYPE):
    # print(
    s = time()
    # 
    try:
        file_size = int(update.message.document.file_size)/1000000
        file_id = update.message.document.file_id
    except:
        file_size = int(update.message.to_dict()['photo'][-1]['file_size'])/1000000
        file_id = update.message.to_dict()['photo'][-1]['file_id']
        
    file = await context.bot.get_file(file_id)
    file_format = file.to_dict()['file_path'][-3:]
    file = await file.download_as_bytearray()
    
    
    
    file_name = f'{update.message.from_user.id}{update.message.id}'
    file_path = f'\{update.message.from_user.id}'+f'\{file_name}.'+'{}'
    credentials_path = "\credentials.json"
    print(file_format)

        
    if file_format == 'pdf':
        file_path_pdf = f'\{update.message.from_user.id}'+f'\{file_name}'+'{}.{}'
        print('ok')
        with open(file_path.format('pdf'),'wb') as f:
            f.write(file)
        count = extract_png(file_path.format('pdf'), f'\{update.message.from_user.id}'+f'\{file_name}')
        for i in range(count):
            await async_orc(file_path_pdf.format(i,'png'), credentials_path, file_path_pdf.format(i, 'txt'))
        
        count-=1
        while count >= 0:
            try:
                await update.message.reply_document(file_path_pdf.format(count, 'txt'))
                os.remove(file_path_pdf.format(count, 'png'))
                os.remove(file_path_pdf.format(count, 'txt'))
                count-=1
            except:
                pass
        os.remove(file_path.format('pdf'))
                
            
    else:
        with open(file_path.format('png'),'wb') as f :
            f.write(file)
        await async_orc(file_path.format('png'), credentials_path, file_path.format('txt'))
        
        status = False
        while status == False:
            try:
                await update.message.reply_document(file_path.format('txt'))
                status = True
                os.remove(file_path.format('png'))
                os.remove(file_path.format('txt'))
            except:
                pass
    
    e = time()
    print(e-s)  



app = ApplicationBuilder().token('5935895439:AAH38AovHN8v_GWxZA3uIKic4AMgLteDWGk').build()

app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.PHOTO | filters.Document.IMAGE | filters.Document.PDF, recive_file))

app.run_polling()
