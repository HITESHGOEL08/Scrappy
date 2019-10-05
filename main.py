from selenium import webdriver
from time import sleep
import pandas as pd


pickup = 'Honolulu, Hawaii, United States of America'
drop = 'Pearl City, Yoakum, Texas, United States of America'

# email = "singhaisid0@gmail.com"
# password = "teuko@123"

browser = webdriver.Firefox(executable_path='./geckodriver')
browser.set_window_size(900,900)
browser.set_window_position(0,0)
sleep(1)
def expedia(city,today,next_date):
    t_m,t_d,t_y = today.split('/')
    n_m,n_d,n_y = next_date.split('/')
    browser.get('https://car-rental.expedia.co.in/en-in/book?pickupIATACode=HNL&dpln=5000776&pickupCountryCode=US&returnIATACode='+city+'&drid1=6004012&returnCountryCode=US&age=30&pickupDate='+str(t_d)+'&pickupMonth='+str(t_m)+'&pickupYear='+str(t_y)+'&returnDate='+str(n_d)+'&returnMonth='+str(n_m)+'&returnYear='+str(n_y)+'&pickupHour=10&pickupMinute=30&returnHour=10&returnMinute=30&residencyId=IN&currencyID=USD&clientId=388196&tpid=27&EAPID=0&TUID=-1&GUID=0420ac4e-53fd-44a2-af27-11ab1e7f85be#/vehicles')
    sleep(10)
    for q in range(0,30):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)


    l1 = []
    l2 = []
    all_lunch = browser.find_elements_by_xpath('//*[@class ="ct-no-margin-bottom"]')
    print("all",all_lunch)
    for k in all_lunch:
        p = []
        print("________________________________________________________________________")
        m = k.get_attribute("innerText")
        print('t2',m)

        p.append(m)
        l1.append(p)
    all_lunch = browser.find_elements_by_xpath('//*[@class ="ct-total-price ct-font-weight-bold notranslate ct-floatr"]')
    print('a2',all_lunch)
    for n in range(0,len(all_lunch)):
        m = all_lunch[n].get_attribute("innerText")
        m = str(m)
        m = m.replace(',','')
        m = m.split('.')[0]
        l1[n].append(str(m))

    print(l1)


    df = pd.DataFrame(l1,columns=['type','price'])
    # df.to_csv('s_1.csv',sep=';')


    l2 =[]
    lst = df['type'].unique()
    for k in lst:
        prc2 = min(df.loc[df['type']== k]['price'].tolist())
        print(prc2)
        l2.append(prc2)
    lst = list(lst)


    final = []
    for i in range(0,len(lst)):
        final.append([lst[i],l2[i]])
    print(final)
    dfin = {}
    for _ in final:
        dfin[_[0]] = _[1]
    return [dfin]
