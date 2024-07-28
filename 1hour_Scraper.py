from colorama import Fore
import mysql.connector
import Token_Scarab
import configure 
import time


class database_controller:
    def __init__(self) -> None:
        self.DATABASE = mysql.connector.connect(**configure.config)
        self.CURSOR = self.DATABASE.cursor()
        
        self.CURSOR.execute("CREATE DATABASE IF NOT EXISTS tokenbaz_cache")
        
        self.DATABASE.database = "tokenbaz_cache"

        self.CURSOR.execute("""CREATE TABLE IF NOT EXISTS info (
                       id INT AUTO_INCREMENT PRIMARY KEY, datetime MEDIUMTEXT, Name_And_Type VARCHAR(255), Buy_Price VARCHAR(255), Buy_Amount VARCHAR(255), Sell_Price VARCHAR(255), Sell_Amount VARCHAR(255), Wage VARCHAR(255), Profit VARCHAR(255))""")
        
        print(Fore.GREEN + "DATABASE AND TABLES CREATED SUCCESSFULLY ✅")


    def insert_into_table(self, data: list[dict[str, str]]) -> None:
        for index, DataDict in enumerate(data):
            print(DataDict)
            Name_and_type = DataDict.get("Name_and_type", None)
            Buy_Price = DataDict.get("Buy_price", None).replace("📉", "*", -1)
            Buy_Amount = DataDict.get("Buy_amount", None)
            Sell_Price = DataDict.get("Sell_price", None).replace("📈", "*", -1)
            Sell_Amount = DataDict.get("Sell_amount", None)
            Wage = DataDict.get("Wage", None)
            Profit = DataDict.get("Profit", None)

            SQL_CODE = "INSERT INTO info (datetime, Name_And_Type, Buy_Price, Buy_Amount, Sell_Price, Sell_Amount, Wage, Profit) VALUES (NOW(), %s, %s, %s, %s, %s, %s, %s)"
            VALUES = (Name_and_type, Buy_Price, Buy_Amount, Sell_Price, Sell_Amount, Wage, Profit)

            self.CURSOR.execute(SQL_CODE, VALUES)

            self.DATABASE.commit()

            
class get_info:
    def __init__(self) -> None:
        for _ in range(60):
            INFORMATION = Token_Scarab.Scrab_tokenbaz()

            print(Fore.GREEN + f"{time.time()}" + " : " + Fore.CYAN + f"{INFORMATION}")

            DATABASE_CONTROLLER = database_controller()
            DATABASE_CONTROLLER.insert_into_table(INFORMATION)

            time.sleep(60)
        

start_time = time.perf_counter()

while True:
    info_getter = get_info()
    print(info_getter)
    end_time = time.perf_counter()

    if (end_time - start_time) >= 60 * 2:
        print(Fore.RED + "ended")
        print(Fore.RED + end_time - start_time)
        
        break
