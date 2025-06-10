
default_length = 42
default_pattern = "-"

def line(pattern=default_pattern,length=default_length):
    line = (pattern * length)[:length]
    print(line)

def header(title,pattern=default_pattern,length=default_length):
    print()
    line(pattern,length)
    print(f"{title:^{length}}")
    line(pattern,length)
    print()

def footer(pattern=default_pattern,length=default_length):
    print()
    line(pattern,length)
    
def print_text_multiline(split_text,width=default_length):
    while len(split_text) > width:
        break_position = split_text.rfind(' ', 0, width)
        if break_position == -1:
            break_position = width 
        print(split_text[:break_position])
        split_text = split_text[break_position:].lstrip()
    if split_text:
        print(split_text)