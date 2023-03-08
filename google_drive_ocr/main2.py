from .application import GoogleOCRApplication
import asyncio
import os



DIR = os.path.dirname(__file__)
os.chmod(DIR, 0o777)

def orc(img_path, credentials_path, output_path):
    app = GoogleOCRApplication(credentials_path)
    
    print(app.perform_ocr(img_path, output_path))

async def async_orc(img_path, credentials_path, output_path):
    # asyncio.get_event_loop().run_in_executor(None, orc)
    # asyncio.get_event_loop().run_in_executor(None, orc)
    # asyncio.gather(asyncio.get_event_loop().run_in_executor(None, orc),asyncio.get_event_loop().run_in_executor(None, orc))
    asyncio.get_event_loop().run_in_executor(None, lambda:orc(img_path, credentials_path, output_path))
    
# asyncio.run(async_orc())

