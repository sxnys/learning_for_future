import asyncio
import threading

@asyncio.coroutine
def hello():
	print('Hello world, current thread: {}'.format(threading.current_thread()))    # OR threading.currentThread()
	r = yield from asyncio.sleep(1)
	print('Hello again, current threadL: {}'.format(threading.current_thread()))

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	tasks = [hello(), hello()]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()