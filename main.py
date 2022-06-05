import requests
import csv
import concurrent.futures
from get_proxies import GetProxies0, GetProxies1, GetProxies2
free_proxy_list = GetProxies0()
#free_proxy_list_1 = GetProxies1()
free_proxy_list_2 = GetProxies2()
proxylist = []

with open('proxylist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])


def extract(proxy):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http': proxy, 'https': proxy}, timeout=2)
        print(r.json(), ' | Works')
    except:
        pass
    return proxy


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract, proxylist)
