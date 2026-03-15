import sys

class NetworkSecurityException(Exception):
    def __init__(self, message, error_details:sys):
        super().__init__(message)
        self.message = message
        _, _, self.traceback = error_details.exc_info()

        self.line_number = self.traceback.tb_lineno
        self.file_name = self.traceback.tb_frame.f_code.co_filename

    def __str__(self):
        return f"{self.message} (File: {self.file_name}, Line: {self.line_number})"
    
if __name__ == "__main__":
    try:
        raise NetworkSecurityException("An error occurred in the network security module.", sys)
    except NetworkSecurityException as e:
        print(e)