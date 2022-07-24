import os
import sys


class HousingException(Exception):

    def __init__(self, error_message: Exception, error_details: sys):
        super().__init__(error_message)

        self.error_message=error_message



    @staticmethod


    def get_detailed_error_message(error_message: Exception, error_details: sys)->str:

        """ 
        error_message : Exception object
        error_detail: sys module object
        """

        _,_ ,exec_tb = error_details.exc_info()

        # _,_ are the atributes in error_details, which we dont need. we need the trace back only from error_detail

        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f" ERROR occured in script : [{file_name}] at line number : [{line_number}] error message : [{error_message}]"
        return error_message

    def __str__(self):
        return self.error_message
        
        

        



    

