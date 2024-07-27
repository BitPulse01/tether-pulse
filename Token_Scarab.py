from selenium.webdriver.common.by import By
import selenium.webdriver as WS
from colorama import Fore, init


init(convert= True)
def Scrab_tokenbaz():
    URL = "https://tokenbaz.com/"

    DRIVER = WS.Chrome()
    DRIVER.get(URL)

    PROFIT = DRIVER.find_element(By.XPATH, '//*[@id="profit"]') 
    TABLE = DRIVER.find_element(By.XPATH, '//*[@id="tbMainPricesTable"]')
    ROWS = TABLE.find_elements(By.CLASS_NAME, 'price-table-row')


    PROFIT_TEXT = PROFIT.text.replace("\n", " | ", -1)
    # print(f"Name and type {Fore.CYAN + '||' + Fore.RESET} Buy price {Fore.CYAN + '||' + Fore.RESET} Buy amount {Fore.CYAN + '||' + Fore.RESET} Sell price {Fore.CYAN + '||' + Fore.RESET} Sell amount {Fore.CYAN + '||' + Fore.RESET} Wage")
    INFOR = []
    for row in ROWS:
        Name_and_type = row.find_element(By.CLASS_NAME, 'price-table-exchange-cell')
        Buy_price = row.find_element(By.CLASS_NAME, 'currency-details-item')
        Buy_amount = row.find_element(By.CLASS_NAME, 'price-table-cell')
        Sell_price = row.find_element(By.CLASS_NAME, 'sell-price-cell')
        Sell_amount = row.find_element(By.CLASS_NAME, 'price-table-cell')
        Wage = row.find_element(By.CLASS_NAME, 'static-fee')

        Name_and_type_text = Name_and_type.text.replace("\n", " | ", -1)
        Buy_price_text = Buy_price.text.replace("\n", " | ", -1)
        Buy_amount_text = Buy_amount.text.replace("\n", " | ", -1)
        Sell_price_text = Sell_price.text.replace("\n", " | ", -1)
        Sell_amount_text = Sell_amount.text.replace("\n", " | ", -1)
        Wage_text = Wage.text.replace("\n", " | ", -1)

        if Buy_price.value_of_css_property("color") == "rgba(0, 166, 84, 1)":
            Buy_price_text = " 📉 " + Buy_price_text + " 📉 "

        if Sell_price.value_of_css_property("color") == "rgba(0, 166, 84, 1)":
            Sell_price_text = " 📈 " + Sell_price_text + " 📈 "
        
        INFO: dict[str, str] = {
            "Name_and_type" : Name_and_type_text,
            "Buy_price" : Buy_price_text,
            "Buy_amount" : Buy_amount_text,
            "Sell_price" : Sell_price_text,
            "Sell_amount" : Sell_amount_text,
            "Wage" : Wage_text
        }

        INFOR.append(INFO)
        # print(f"{Name_and_type_text} {Fore.CYAN + '||' + Fore.RESET} {Buy_price_text} {Fore.CYAN + '||' + Fore.RESET} {Buy_amount_text} {Fore.CYAN + '||' + Fore.RESET} {Sell_price_text} {Fore.CYAN + '||' + Fore.RESET} {Sell_amount_text} {Fore.CYAN + '||' + Fore.RESET} {Wage_text}")
        # print(INFO)
        # print(INFOR)

    print(PROFIT_TEXT)

    return INFOR
