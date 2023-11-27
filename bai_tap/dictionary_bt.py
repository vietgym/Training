def dis(data):
    for key, value in data.items():
        print(f'Key: {key}, Value: {value}')


def find(data):
    tmp = data["result"]
    value_result = data.get("index_result")
    for key, value in tmp.items():
        if key <= value_result:
            continue
        if value:
            a = key
            break
    data["index_result"] = a
    return data


data1 = {
    "result": {
        "1":  876,
        "2": None,
        "3": None,
        "4": 234,
        "5": 345,
        "6": 456,
        "7": 789,
        "8": None,
        "9": 234,
        "10": None
    },
    "index_result": "7"
}
dis(find(data1))
