def transform(legacy_data):
    data = {}
    for point,letters in legacy_data.items():
        temp = data.fromkeys(map(str.lower,letters), point)
        data.update(temp)
    return data