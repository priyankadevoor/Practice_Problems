import logging
import threading

global_counter = 0

lock = threading.Lock()
logging.basicConfig(
    filename='app.txt',
    level=logging.INFO,
    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
)
def increment_counter():
    global global_counter
    with lock:
        global_counter += 1
        print(global_counter)
        logging.info(f"Counter incremented to {global_counter}")
t = []
for _ in range(50):
    t.append(threading.Thread(target=increment_counter))

for thread in t:
    thread.start()
    thread.join()
