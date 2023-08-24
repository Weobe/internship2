def wrap_text(text, width=100):
    result = ""
    l = 0
    r = len(text)
    while l < r:
        l = text.find("\n", l, r)
        if l == -1:
            break
        if l < r:
            text = text[:l] + " \n " + text[(l + 1):]
        l += 3
        
    parsed = text.split(' ')
    sz = 0
    for i in parsed:
        if sz + len(i) > width:
            result += "\n"
            sz = 0
        else:
            result += " " 
        result += i
        sz += len(i)
        if (i == "\n"):
            sz = 0
            result += "\n\n"
    return result

        
