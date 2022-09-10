
class PythonPrint:
    def __init__(self, print_arg):
        self.print_arg = print_arg
    
def build_ast(token_list):
    token_index = 0
    current_token = token_list[token_index]

    if current_token == "print":
        token_index += 1
        current_token = token_list[token_index]
        assert current_token == "("

        token_index += 1
        current_token = token_list[token_index]
        print_arg = current_token
        
        token_index += 1
        current_token = token_list[token_index]
        assert current_token == ")"

        yield PythonPrint(print_arg)
    


