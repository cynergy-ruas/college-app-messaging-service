class APIErrors(Exception):
    """
    This Class handles all the API errors 
    Args:
        Exception :  This takes execption as the arugment 
    """
    
    def __init__(self,code,message):
        super().__init__(message)
        self.code = code 
        self.message = message