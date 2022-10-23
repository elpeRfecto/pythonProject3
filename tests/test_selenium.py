from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_open_web_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://petfriends.skillfactory.ru/')
    btn_new_user = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/button')
    btn_new_user.click()
    btn_exist_acc = driver.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()
    field_email = driver.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("mmjkeee@mail.ru")

    field_pass = driver.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("123456")

    btn_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    if driver.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

        assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    statistic = driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                              ".table.table-hover tbody tr")))

    pets = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    number_of_pets = len(pets)

    assert number == number_of_pets

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                              ".\\.col-sm-4.left")))

    statistic = driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    images = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    half = number / 2

    number_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_photos += 1

    assert number_photos >= half

#
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                              ".table.table-hover tbody tr")))
    pets = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    string = driver.find_elements(By.XPATH, '//table[@class ="table table-hover"]/tbody/tr')
    name = driver.find_elements(By.XPATH, "//tr/td[1]")
    animal_type = driver.find_elements(By.XPATH, '//tr/td[2]')
    age = driver.find_elements(By.XPATH, '//tr/td[3]')
    for i in range(len(string)):
        assert name[i].text and animal_type[i].text and age[i].text != ''
        count_name = len(name)
        count_type = len(animal_type)
        count_age = len(age)
        assert count_type == count_name
        assert count_name == count_age

#
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                              ".table.table-hover tbody tr")))

    pets = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    pets_name = []
    for i in range(len(pets)):
        data_pet = pets[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    assert r == 0
    print(r)
    print(pets_name)

#
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     ".table.table-hover tbody tr")))

    pets = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    list_data = []
    for i in range(len(pets)):
        data_pet = pets[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)

    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '

    list_line = line.split(' ')

    set_list_line = set(list_line)

    a = len(list_line)
    b = len(set_list_line)

    result = a - b

    assert result == 0

    driver.quit()
