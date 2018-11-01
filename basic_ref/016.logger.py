import logging

logging.basicConfig(level=logging.DEBUG,filename='output.log',filemode='w')
logging.debug('Debug Logging')
logging.info('Info Logging')
logging.warning('Warning Logging')
logging.error('Error Logging')
logging.critical('Critical Logging')
logging.critical('Critical Error on my log')
