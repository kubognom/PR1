import threading
import time
import random

Pause = False
stop = False
break_ = False


class C1(threading.Thread):
    def __init__(self):
        super(C1, self).__init__()
        self.iterations = 0
        self.daemon = True  # Allow main to exit even if still running.
        self.paused = True  # Start out paused.
        self.state = threading.Condition()

    def run(self):
        global Pause
        global stop
        global break_
        self.resume()
        while True:
            with self.state:
                if self.paused:
                    self.state.wait()  # Block execution until notified.
            print("C1 осталось 4с")
            AA = int(input("1,2>>"))

            time.sleep(4)
            if AA == 1:
                stop = True
                break
            if AA == 2:
                break_ = True

            print("C1 2c")
            time.sleep(2)
            Pause = True
            time.sleep(.1)
            self.iterations += 1

    def pause(self):
        with self.state:
            self.paused = True  # Block self.

    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()  # Unblock self if waiting.


class C2(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(C2, self).__init__(*args, **kwargs)
        self._event = threading.Event()

    def run(self):
        while True:
            print("C2")


    def off_C(self):
        self._event.set()
class C3(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(C3, self).__init__(*args, **kwargs)
        self._event = threading.Event()

    def run(self):
        while True:
            print("C2")


    def off_C(self):
        self._event.set()

def win_init():
    thread_list = []
    pausedthread = []
    pause_list = []
    global Pause
    global stop
    global  break_
    M=1
    while M!=0:

        thread_viboor = int(input("1>> 2>> 3>> 4>>> 6 >>  5-start "))



        if thread_viboor == 1:
            thread_list.append(C1())
        if thread_viboor == 2:
            thread_list.append(C2())
        if thread_viboor == 3:
            thread_list.append(C3())
        if thread_viboor ==4:
            A = thread_list.pop(int(input(">>"))-1)
            thread_list.append(A)
        if thread_viboor == 6:
            P = pause_list.pop(0)
            thread_list.append(P)
        if thread_viboor == 5:

            B = thread_list.pop(0)
            for i in range(len(pausedthread)):
                if B == pausedthread[i]:
                    Pause = True
                else:
                    Pause = False
            print(B, " running")
            if Pause == False:
                B.start()
            B.resume()
            Pause = False


            while True:
                if break_ == True:
                    pause_list.append(B)
                    B.pause()
                    print("..")
                    break_ = False
                    break

                if Pause == True:

                    B.pause()
                    thread_list.append(B)
                    pausedthread.append(B)
                    print("..")
                    Pause = False

                    break
                if stop == True:
                    B.join()
                    print("..")
                    stop = False
                    break


        print('potoki',thread_list)
        print('pause ',pause_list)



    while True:

        event = str(input("input"))

        if event == 'start' and producer_count != 0 and consumer_count != 0:
            for i in range(len(thread_list)):
                thread_list[i].start()

            producer_count = 0
            consumer_count = 0


        if event == 'q':
            print("Осталось:",q)
            for i in range(len(producer_list)):
                producer_list[i].off_P()
                producer_list[i].join()
            producer_list = []
            for i in range(len(consumer_list)):
                consumer_list[i].off_C()
                consumer_list[i].join()
            consumer_list = []
            event = ''
        if event == 'stop':
            break




if __name__ == '__main__':
    win_init()