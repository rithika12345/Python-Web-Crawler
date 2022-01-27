def crawler(lines):
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import gspread
    import datetime
    import json
    from time import sleep
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    gc=gspread.service_account(filename='webcrawler/corded-academy-305706-9d7a3bc33748.JSON')
    sh=gc.open('scraper').sheet1
    n1=len(lines)
    links = []
    n_pages = 20
    for j in range(n1):
        for page in range(1, n_pages):
            url = "http://www.google.com/search?q=" + lines[j] + "&start=" +str((page - 1) * 10)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            Date=datetime.datetime.now()
            search = soup.find_all('div', class_="yuRUbf")
            for h in search:
                links.append(h.a.get('href'))
            n=len(links)
            for i in range(n):
                product={'Date':Date,'Link':links[i]}
                sh.append_row([str(product['Date']),str(product['Link'])])
                sleep(0.5)
                
                
