from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from databaseproperty import *

create_table()

options = Options()
options.add_experimental_option('detach', True, )
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
for n in range(1, 4000):

    url = f"https://www.propertyfinder.ae/en/search?page={n}"

    # Navigate to the specified URL
    driver.get(url)

    # Execute JavaScript code on the web page
    script = """
    // JavaScript code to execute
    // Replace this with your desired JavaScript code
    //console.log("Hello, JavaScript!");

    // Example: Get the title of the web page
    var pageTitle = window?.propertyfinder?.settings?.search?.payload?.included;

    return pageTitle;
    """
    result = driver.execute_script(script)

    for entry in result[:25]:
        print(entry)
        print("------")
        insert_property(entry)




# Close the browser window
driver.quit()