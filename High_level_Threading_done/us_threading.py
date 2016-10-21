'''
We can use 2 source code at a same time with threading.

'''

import threading


def do_this():
    print "do_this is working now. and thread 1"

def do_that():
    print "Nothing to do."

def main():
    print "this is main _ threading."
    threadd= threading.Thread(target=do_this)
    threadd.start()
    print threading.active_count()
    print threading.enumerate()
    print threading.current_thread()

if (__name__ == "__main__"):
    main()
