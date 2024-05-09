from selenium import webdriver
import time

def test_index_page():
    """Test the index page"""
    driver = webdriver.Chrome()
    driver.get('http://localhost:5000')

    # Assert page title
    assert "Birthday Tracker Application" in driver.title

    # Assert page content
    assert "Welcome to the Birthday Tracker Application" in driver.page_source

    driver.quit()

def test_add_and_delete_birthday():
    """Test adding and deleting a birthday entry"""
    driver = webdriver.Chrome()
    driver.get('http://localhost:5000')

    # Add a birthday entry
    name_input = driver.find_element_by_id('name')
    name_input.send_keys('John')
    year_input = driver.find_element_by_id('year')
    year_input.send_keys('1990')
    month_input = driver.find_element_by_id('month')
    month_input.send_keys('5')
    day_input = driver.find_element_by_id('day')
    day_input.send_keys('10')
    add_button = driver.find_element_by_class_name('add-btn')
    add_button.click()

    # Wait for redirect
    time.sleep(1)

    # Assert user is added
    assert 'John' in driver.page_source

    # Delete the added user
    delete_button = driver.find_element_by_xpath('//button[contains(text(), "Delete")]')
    delete_button.click()

    # Wait for redirect
    time.sleep(1)

    # Assert user is deleted
    assert 'John' not in driver.page_source

    driver.quit()

if __name__ == '__main__':
    test_index_page()
    test_add_and_delete_birthday()
