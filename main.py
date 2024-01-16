import threading

import asyncio as asyncio

from main_bot import main_main
from sub_bot import main_sub


def loop1():
    asyncio.run(main_main())


def loop2():
    asyncio.run(main_sub())


# Create threads for each loop
thread1 = threading.Thread(target=loop1)
thread2 = threading.Thread(target=loop2)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

