
import logging


extraData={'user':'uday@uday.com.np'}


fmtstr="User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"


logging.basicConfig(level=logging.DEBUG,filename='output.log',filemode='w',format=fmtstr)


logging.critical('Critical Error on my log',extra=extraData)
logging.info('Just Info',extra=extraData)