
t_print = r"print"
t_open_paren = r"\("
t_close_paren = r"\)"
t_str = r"\".*?\""


all_token = [t_print, t_open_paren, t_close_paren, t_str]

import re


def tokenize(code_text):
    return [token.group() for token in generate_tokens(code_text)]

def generate_tokens(code_text):
    tokens = token_dict(code_text)
    while True:
        next_gen, next_token = min(tokens.items(), key=lambda x: x[1].start())
        yield next_token
        try:
            tokens[next_gen] = next(next_gen)
        except StopIteration:
            del tokens[next_gen]
        if not tokens.keys():
            break

def token_dict(code_text):
    return dict(token_gen_and_val(code_text))

def token_gen_and_val(code_text):
    for token in all_token:
        pattern = re.compile(token)
        pattern_gen = pattern.finditer(code_text)
        yield pattern_gen, next(pattern_gen)
