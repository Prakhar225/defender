import time
import random
from pynput.keyboard import Key, Controller

# Configuration parameters
minimum_wait_time = 60  # seconds
maximum_wait_time = 300  # seconds
keys = [Key.up, Key.down, Key.left, Key.right]

# Create a keyboard controller
keyboard = Controller()

def press_random_keys(num_keys=5):
   """Presses a random number of keys from the specified set."""
   for _ in range(num_keys):
       key = random.choice(keys)
       keyboard.press(key)
       keyboard.release(key)

while True:
   # Press random keys several times
   press_random_keys(random.randint(2, 10))  # Vary the number of key presses

   # Wait for a random amount of time before the next iteration
   wait_time = random.randint(minimum_wait_time, maximum_wait_time)
   time.sleep(wait_time)
