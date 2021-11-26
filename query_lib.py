import requests


def query_lib(lib):
    print("lib arg", lib, type(lib))
    link = "https://smulibraries.southeastasia.cloudapp.azure.com/public/count.json"
    r = requests.get(link)
    data = r.json()
    
    if lib == "0":
        return({
            "current": data["lks"]["inside"],
            "max": 1000
            })
    if lib == "1":
        return({
            "current": data["kgc"]["inside"],
            "max": 300
            })


if __name__ == "__main__":
    print(query_lib(0))