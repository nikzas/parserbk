from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import datetime, timedelta


class ParserAviator():
    def __init__(self):
        self.page = None

    def run(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            self.page = browser.new_page()
            self.page.goto("https://lucky-jet.gamedev-atech.cc/"
                           "?exitUrl=https%253A%252F%252F1wowei.xyz%252Fcasino&language=ru&b=demo")
            self.page.locator(".sc-jIILKH > .sc-gYbzsP > .sc-hhOBVt").click()
            self.page.screenshot(path="example.png")
            self.locators = ".sc-dwnOUR"        #Для замены возможного div class
            return self.page.locator(self.locators).text_content()

    def corr_text_df(self):
        massive = [float(i.replace('\xa0', '')) for i in self.run().split(sep='x') if i != '']  # Здесь  уже float
        df = pd.DataFrame(massive)
        return df

    def corr_text_series(self):
        massive = [float(i.replace('\xa0', '')) for i in self.run().split(sep='x') if i != '']
        ser = pd.Series(massive)
        return ser

    def last_edit_text(self, global_massive, next_mass):
        first_cnt = global_massive[0:3].stack()
        index_find = next_mass[next_mass.isin(first_cnt)].index
        global_massive = pd.concat([next_mass[:index_find.values[0]], global_massive]).reset_index(drop=True)
        print(global_massive)
        return global_massive

    start_date = datetime(2024, 2, 17, 23, 59)

    def start_time(self):
        global start_date
        current_date = start_date
        start_date += timedelta(days=1)
        return current_date


