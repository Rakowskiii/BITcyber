import base64
def verify(tkn, key):
    token = []
    temp = tkn.split('.')
    for i in temp:
        i = i.replace(r'\.','')
        while len(i)%4:
            i+='='
        token.append(base64.b64decode(i))
    token[0] = eval(token[0].decode("UTF-8"))
    token[1] = eval(token[1].decode("UTF-8"))
    if token[0]['alg'] == 'None':
        print(token[2])
        if token[2] == b'':
            return token[1]

print(verify("eyJhbGciOiJOb25lIiwidHlwIjoiSldUIn0K.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.asd", "key"))
#print(token[0]['alg'])