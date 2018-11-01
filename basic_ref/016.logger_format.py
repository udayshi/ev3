import logging
fmtstr="%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
fmtdt="%m/%d/%Y %I:%M:%S %p"

logging.basicConfig(level=logging.DEBUG,filename='output.log',filemode='w',format=fmtstr,datefmt=fmtdt)

logging.debug('Debug Logging')
logging.info('Info Logging')
logging.warning('Warning Logging')
logging.error('Error Logging')
logging.critical('Critical Logging')

logging.critical('Critical Error on my log')

