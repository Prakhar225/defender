import pyautogui
import random
import time

def press_random_keys(keys=["up", "down", "left", "right", "ctrl", "shift"], min_wait_time=60, max_wait_time=300, min_key_presses=1, max_key_presses=10):
    try:
        while True:
            # Generate random wait time
            wait_time = random.randint(min_wait_time, max_wait_time)
            print(f"Waiting for {wait_time} seconds...")
            time.sleep(wait_time)

            # Generate random number of key presses
            num_key_presses = random.randint(min_key_presses, max_key_presses)

            # Press random keys
            for _ in range(num_key_presses):
                key = random.choice(keys)
                pyautogui.press(key)
                print(f"Pressed key: {key}")

    except KeyboardInterrupt:
        print("Bot stopped.")

if __name__ == "__main__":
    keys = ["up", "down", "left", "right", "ctrl", "shift"]  # Default keys
    min_wait_time = 60  # Default minimum wait time in seconds
    max_wait_time = 300  # Default maximum wait time in seconds
    min_key_presses = 1  # Default minimum number of key presses
    max_key_presses = 10  # Default maximum number of key presses

    press_random_keys(keys, min_wait_time, max_wait_time, min_key_presses, max_key_presses)
