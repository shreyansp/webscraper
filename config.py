import os

dirname, filename = os.path.split(os.path.abspath(__file__))

OUTPUT_ROOT = os.path.join(dirname,'output')
CHROME_DRIVER = os.path.join(dirname,'drivers/chromedriver.exe')
if not os.path.exists(OUTPUT_ROOT):
    os.mkdir(OUTPUT_ROOT)