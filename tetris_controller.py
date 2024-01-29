import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import dotenv_values
from tetris_move import Move

secrets = dotenv_values(".env")

class TetrisController:
    def __init__(self):
        self.board_state = []
        self.next_tile = None

        os.environ["GH_TOKEN"] = secrets["GH_TOKEN"]
        self.driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
        self.driver.get('https://chvin.github.io/react-tetris/?lan=en')
        sleep(5)

    def get_game_state(self) -> list[list[str]]:
        board_state = []
        board = self.driver.find_element(By.CLASS_NAME, "_6pVK")
        rows = board.find_elements(By.TAG_NAME, "p")
        for row in rows:
            squares = row.find_elements(By.TAG_NAME, "b")
            board_state.append(list(square.get_attribute("class") for square in squares))
        self.board_state = board_state

    def get_next_tile(self) -> list[list[str]]:
        next_tile = []
        next_tile_element = self.driver.find_element(By.CLASS_NAME, "_3Wmt")
        rows = next_tile_element.find_elements(By.TAG_NAME, "div")
        for row in rows:
            squares = row.find_elements(By.TAG_NAME, "b")
            curr_row = []
            for square in squares:
                curr_row.append(square.get_attribute("class"))
            next_tile.append(curr_row)
        self.next_tile = next_tile

    def is_game_over(self) -> bool:
        try:
            if self.driver.find_element(By.CLASS_NAME, "_20Jp"):
                return True
            return False
        except NoSuchElementException:
            return False

    def send_keys(self, keys: str) -> None:
        actions = ActionChains(self.driver)
        actions.send_keys(keys)
        actions.perform()

    def make_move(self, move: Move):
        self.send_keys(Keys.UP * move.rotation)
        self.send_keys(Keys.LEFT * abs(move.horizontal_movement) 
                       if move.horizontal_movement < 0 
                       else Keys.RIGHT * move.horizontal_movement)
        self.send_keys(Keys.SPACE)
