
import logging
import os
from datetime import datetime

Logfile = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",Logfile)
os.makedirs(logs_path,exist_ok=True)


logfile_path = os.path.join(logs_path,Logfile)

logging.basicConfig(
    filename=logfile_path,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
