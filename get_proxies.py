import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import pandas as pd
import requests
from time import sleep

chrome_driver_path = "C:\Tools\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)


class GetProxies0:
    def __init__(self):
        self.url = "https://free-proxy-list.net/"
        try:
            driver.get(self.url)
            proxy_list_click = driver.find_element(By.CLASS_NAME, "fa-clipboard")
            proxy_list_click.click()
            proxy_text = driver.find_element(By.XPATH, "//*[@id='raw']/div/div/div[2]/textarea").get_attribute("value")
            useless_0 = proxy_text.split("\n")[0]
            useless_1 = proxy_text.split("\n")[1]
            proxy_text = proxy_text.replace(useless_0, "")
            proxy_text = proxy_text.replace(useless_1, "")
            with open("proxylist.csv", "w") as f:
                f.write(proxy_text)
            df = pd.read_csv("proxylist.csv")
            df.to_csv('proxylist.csv', index=False)

        except selenium.common.exceptions.NoSuchElementException:
            print("Something has changed on the website")
            driver.close()
            exit()


class GetProxies1:
    def __init__(self):
        self.geonode_proxies_url = "https://proxylist.geonode.com/api/" \
                      "proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&protocols=https"
        response = requests.get(self.geonode_proxies_url).json()
        for data in response["data"]:
            ip = data["ip"]
            port = data["port"]
            proxy = f"\n{ip}:{port}"
            with open("proxylist.csv", "a+") as f:
                f.write(proxy)
            df = pd.read_csv("proxylist.csv")
            df.to_csv('proxylist.csv', index=False)


class GetProxies2:
    def __init__(self):
        self.var = 1
        for _ in range(3):
            self.url = f"http://free-proxy.cz/en/proxylist/country/all/https/ping/all/{self.var}"
            driver.get(self.url)
            click = driver.find_element(By.ID, "clickexport")
            click.click()
            proxies = driver.find_element(By.ID, "zkzk").text
            sleep(1)
            self.var += 1
            with open("proxylist.csv", "a+") as f:
                f.write(proxies)
            df = pd.read_csv("proxylist.csv")
            df.to_csv('proxylist.csv', index=False)
        driver.close()
