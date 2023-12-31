import sys
from src.logger import logging

def error_message_details(error,error_details:sys):
    exc_type, exc_obj, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno

    error_message = f"Error occured in python script namew {file_name},in line no. {line_no}, error message{error}."

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
    
    def __str__(self):
        return self.error_message


'''
if __name__=="__main__":
    logging.info("Logging has started")
    try:
        a=1/0
    except Exception as e:
        logging.info('Division by zero') 
        raise CustomException(e,sys)
     '''
