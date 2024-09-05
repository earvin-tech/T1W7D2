import time

def fetch_data_from_server(url, cb):
    # simulate fetching data from server
    print(f"Fetching data from {url}")
    time.sleep(3)
    print("Data fetching complete")
    # data fetched from the server
    data = "this is the data"
    # calling the callback function with that data
    cb(data)

def on_fetch(data):
    # do something with the data fetched from the server
    print(data)

fetch_data_from_server("http://www.ourwebsite.com/products", on_fetch)