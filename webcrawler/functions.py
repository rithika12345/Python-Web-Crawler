def handle_uploaded_file(f):
    data=f.read().splitlines()
    n=len(data)
    for i in range(n):
        data[i]=data[i].decode("utf-8")
    print(data)
    return data

