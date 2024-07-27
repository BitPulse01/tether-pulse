from colorama import Fore
import mysql.connector
import Token_Scarab
import configure 
import time


class get_info:
    def __init__(self) -> None:
        for _ in range(60):
            INFORMATION = Token_Scarab.Scrab_tokenbaz()

            print(Fore.GREEN + f"{time.time()}" + " : " + Fore.CYAN + INFORMATION)

            time.sleep(60)
        

class database_controller:
    def __init__(self) -> None:
        DATABASE = mysql.connector.connect(**configure.config)
        CURSOR = DATABASE.cursor()
        
        CURSOR.execute("CREATE DATABASE IF NOT EXISTS tokenbaz_cache")
        
        DATABASE.database = "tokenbaz_cache"

        CURSOR.execute("""CREATE TABLE IF NOT EXISTS info (
                       id INT AUTO_INCREMENT PRIMARY KEY, 
                       datetime VARCHAR(255), 
                       Name_And_Type VARCHAR(255), 
                       Buy_Price VARCHAR(255), 
                       Buy_Amount VARCHAR(255), 
                       Sell_Price VARCHAR(255), 
                       Sell_Amount VARCHAR(255), 
                       Wage VARCHAR(255))""")
        
        print(Fore.GREEN + "DATABASE AND TABLES CREATED SUCCESSFULLY ✅")


    def insert_into_table(self, data) -> None:
        pass


start_time = time.perf_counter()

DATABASE_CONTROLLER = database_controller()

while True:
    # info_getter = get_info()
    end_time = time.perf_counter()

    if (end_time - start_time) >= 60 * 2:
        print(Fore.RED + "ended")
        print(Fore.RED + end_time - start_time)
        
        break
