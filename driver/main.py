# 2020 Adelta
# https://github.com/A-delta

from old_driver.driver import Driver

def main():
    driver = Driver()
    driver.load_config()
    driver.establish_connection()
    driver.run()

if __name__ == "__main__":
    main()