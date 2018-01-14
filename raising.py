class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s=raw_input('Enter somthing --->')
    if len(s)<3:
        raise ShortInputException(len(s),3)
except EOFError:
    print'Why did you do an EOF on me?'
except ShortInputException,self:
    print'ShortInputException:The input was of length %d, was excepting at least %d' %(self.length,self.atleast)

else:
    print'No exception was raised.'
