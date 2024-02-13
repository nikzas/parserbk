from playwright.sync_api import Playwright, sync_playwright
import pandas as pd

class ParserAviator():
    def __init__(self):
        self.page = None

    def run(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            self.page = browser.new_page()
            self.page.goto("https://lucky-jet.gamedev-atech.cc/?exitUrl=https%253A%252F%252F1wowei.xyz%252Fcasino&language=ru&b=demo")
            self.page.locator(".sc-jIILKH > .sc-gYbzsP > .sc-hhOBVt").click()
            self.page.screenshot(path="example.png")
            self.locators = ".sc-dwnOUR"        #Для замены возможного div class
            return self.page.locator(self.locators).text_content()

    def corr_text(self):
        massive = [float(i.replace('\xa0', '')) for i in self.run().split(sep='x') if i != '']  # Здесь  уже float
        df = pd.DataFrame(massive).T
        return df

if __name__ == "__main__":
    CNT = 0
    start = ParserAviator()
    global_massive = start.corr_text()
    while True:
        next_mass = start.corr_text()
        #index_global_massive = global_massive.loc[CNT, :3]  # Первые три числа в массиве
        res_g_m = global_massive.loc[CNT, :3]
        res_n_m = next_mass.loc[CNT+1, :3]
        res_g_m = res_g_m[0]

        result = res_g_m.compare(res_n_m)


        global_massive = pd.concat([global_massive, next_mass], ignore_index=True)
        print(global_massive)

