from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class VehiclePage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.CSS_SELECTOR, "#model1 .js-name")
        self.model_select = (By.CSS_SELECTOR, "#model1 .js-model")
        self.year_input = (By.CSS_SELECTOR, "#model1 .js-year")
        self.color_select = (By.ID, "vehColor")
        self.clone_button = (By.ID, "cloneVehicle")

    def fill_vehicle_data(self, name, model, year):
        self.driver.find_element(*self.name_input).send_keys(name)
        Select(self.driver.find_element(*self.model_select)).select_by_visible_text(model)
        self.driver.find_element(*self.year_input).send_keys(year)

    def select_color(self, color):
        Select(self.driver.find_element(*self.color_select)).select_by_visible_text(color)

    def clone_vehicle(self):
        self.driver.find_element(*self.clone_button).click()

    def get_cloned_data(self):
        name = self.driver.find_element(By.CSS_SELECTOR, "#model2 .js-name").get_attribute("value")
        model = Select(self.driver.find_element(By.CSS_SELECTOR, "#model2 .js-model")).first_selected_option.text
        year = self.driver.find_element(By.CSS_SELECTOR, "#model2 .js-year").get_attribute("value")
        color = self.driver.find_element(By.CSS_SELECTOR, "#model2 .js-color").get_attribute("value")
        return {"name": name, "model": model, "year": year, "color": color}
