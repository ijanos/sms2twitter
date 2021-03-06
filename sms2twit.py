#!/usr/bin/env python
import Queue
from twthread import TwitterUpdate
from smsthread import MessageReader


if __name__ == "__main__":
    queue = Queue.Queue()

    smsreader = MessageReader(queue)
    twthread = TwitterUpdate(queue)

    # Threads wont keep alive the application after main thread exited
    twthread.daemon = True
    smsreader.daemon = True

    smsreader.start()
    twthread.start()

    raw_input("Press Enter to exit...")
