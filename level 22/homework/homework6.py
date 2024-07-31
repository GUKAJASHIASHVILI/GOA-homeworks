def manual_replace(text,str_to_replace,replacement):
    result = ""
    i = 0

    while i < len(text):
        if text[i:i+len(str_to_replace)] == str_to_replace:
            text += replacement
            i += len(str_to_replace)
        else:
            result += text[i]
            i += 1

    return result


print(manual_replace("Hello world!", "world!", "there!"))