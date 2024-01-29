from time import sleep
from selenium.webdriver.common.keys import Keys
from tetris_controller import TetrisController
from tetris_algorithm import generate_move

def main():
    print("Opening game...")
    tc = TetrisController()
    sleep(3)
    game_over = False
    print("Starting game...")
    tc.get_next_tile()
    tc.send_keys(Keys.SPACE)
    while not game_over:
        tc.get_game_state()
        move = generate_move(tc.board_state[-16:], tc.next_tile)
        tc.get_next_tile()
        tc.make_move(move)
        sleep(0.5)
        game_over = tc.is_game_over()
    tc.driver.quit()
    
    

if __name__ == "__main__":
    main()