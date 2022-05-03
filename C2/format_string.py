def format_string(string, formatter=None):
    '''Format a string using the formatter object, which is 
    expected to have a format() method that accepts
    a string.'''

    class DefaultFormatter:
        '''Format a string in title class.'''
        def format(self, string):
            # Return string with title format
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()
    
    return formatter.format(string)

hello_string = "hello world, how are you today?"

class FormatUpperString:
    def format(self, string):
        return str(string).upper()

print("input: " + hello_string)
print("output: " + format_string(hello_string))
print("="*40)
# Pass other formatter
print("input: " + hello_string)
print("output: " + format_string(hello_string, FormatUpperString()))