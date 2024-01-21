from time import sleep
from tetris_controller import TetrisController
from tetris_algorithm import generate_move

def main():
    print("Starting...")
    tc = TetrisController()
    for _ in range(10):
        tc.get_game_state()
        tc.get_next_tile()
        sleep(10)
    tc.driver.quit()
    
    

if __name__ == "__main__":
    main()