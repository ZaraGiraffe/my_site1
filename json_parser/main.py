import json


pth = "j.json"


def navigate(path):
    """
    navigated through json file
    """
    file = open(path, 'r')
    data = json.load(file)
    while isinstance(data, list) or isinstance(data, dict):
        if isinstance(data, list):
            print(f"choose index in range: 0 - {len(data)-1}")
            ind = "-1"
            while not ind.isnumeric() or int(ind) < 0 or int(ind) >= len(data):
                ind = input()
            data = data[int(ind)]
        elif isinstance(data, dict):
            print(f"choose key: {list(data.keys())}")
            ind = "fuf"
            while ind not in data.keys():
                ind = input()
            data = data[ind]
    print(data)


#navigate(pth)
