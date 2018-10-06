def myreadlines(f,newline):
    buf=""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos+len(newline):]
        chunk=f.read(36)
        if not chunk:
            yield buf
            break
        buf += chunk

with open("test1.txt") as f:
    for line in myreadlines(f,"{|}"):
        print(line)