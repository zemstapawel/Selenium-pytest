import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.vehicle_page import VehiclePage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/html/index.html")
    yield driver
    driver.quit()

@pytest.mark.parametrize("model", ["BMW", "Mazda"])
def test_clone_vehicle(driver, model):
    page = VehiclePage(driver)
    page.fill_vehicle_data(name="Vehicle 1", model=model, year="2020")
    page.select_color("Red")
    page.clone_vehicle()
    data = page.get_cloned_data()

    assert data == {
        "name": "Vehicle 1",
        "model": model,
        "year": "2020",
        "color": "Red"
    }
