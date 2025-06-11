import re

def remove_number_segments(text):
    # Pattern: any segment of 10 or more characters made only of digits, /, -, or .
    pattern = r'\b[0-9/\-\.]{10,}\b'
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text


def remove_short_newline_blocks(text, max_chars=50):
    # Pattern: newline, then up to max_chars non-newline characters, then another newline
    pattern = re.compile(r'\n([^\n]{0,' + str(max_chars) + r'})\n')
    
    # Repeatedly remove matches to handle nested or sequential cases
    while True:
        new_text, count = pattern.subn('\n', text)
        if count == 0:
            break
        text = new_text
    return text.strip()


def add_space_after_period(text):
    new_text = text[0]
    for i in range(1, len(text)):
        if(text[i-1] == "." and text[i] != " "):
            new_text += " "
            new_text += text[i]
        else:
            new_text += text[i]
    return new_text


def remove_brbr(text):
    i = 0
    new_text = ""
    while(i<len(text)):
        if(i<len(text)-11 and text[i:i+10] == "</br></br>"):
            i += 10
        else:
            new_text += text[i]
            i += 1
    return new_text