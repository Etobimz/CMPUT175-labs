#----------------------------------------------------
# Lab 6, Exercise 2 - Queue efficiencies
# 
# Author of supporting code: CMPUT 175 Team
# Author of dequeue_experiment(): 
#----------------------------------------------------

import random
import time
from queues import BoundedQueue
from queues import CircularQueue
from decimal import Decimal
from terminalplot import plot2

def enqueue_experiment(queue_class , queue_size ):
    '''
    This function will enqueue elements into Bounded and Circular queues and return them
    :param queue_class: The queue_class description that we want to declare the  object for like BoundedQueue, CircularQueue
    :param queue_size: The size of the queue and the number of elements that we want to enter in queue
    :return: Bounded Queue Object, Circular  Queue Object
    '''
    # init the relevant objects
    queue = queue_class(queue_size)

    # enqueue elements to max capacity of queue
    while not queue.isFull():
        value = random.random()
        queue.enqueue(value)

    return queue


def dequeue_experiment(queue):
    '''
    This function will be responsible for dequeues the elements in the queue
    :param queue: (queue object) The queue object that we want to test on
    :return: (float) Returns the time of execution of the dequeue operation
    '''
    # the time to dequeue all the elements

    ##### START CODE HERE #####

    # start the time
    start = time.time()

    # keeps dequeing untill the queue is empty
    while not queue.isEmpty():
        queue.dequeue() # works for both bonded and circular queues since they both have the 'isEmpty' and 'dequeue' methods in thier classes

    # End the timer
    end = time.time()

    # Calculate the elapsed time
    time_interval = float(end - start)

    return time_interval



def avg_dequeue_experiment(queue_class, size, sample_size = 5):
    '''
    This function is used to average over many runs for the dequeue experiment
    :param queue_class: (function-type) The typeof queue that we are using
    :param size: (int) Size of the queue to do experiment
    :param sample_size : (int) The number of samples to be used for averaging
    :return: (float) return the average time
    '''
    q_run_avg = 0
    for i in range(sample_size):
        queue = enqueue_experiment(queue_class, size)
        q_run_avg += dequeue_experiment(queue)

    return float(q_run_avg)/sample_size
   

def main():
    # queue sizes that we will use for different experiments
    # queues_sizes = [10000, 20000 , 30000, 40000, 50000, 60000, 70000,80000,  90000, 100000]
    queues_sizes = [10000, 30000, 50000, 70000, 90000, 100000]

    # the setup of the experiment
    bqueues = []
    cqueues = []
    for q in queues_sizes:
        # print("Done for Queue Size : {}".format(q))
        bq = enqueue_experiment(BoundedQueue, q)
        cq = enqueue_experiment(CircularQueue,q)
        bqueues.append(bq)
        cqueues.append(cq)

    # perform the dequeue experiment
    bounded_queue_times = [dequeue_experiment(q) for q in bqueues]
    circular_queue_times = [dequeue_experiment(q) for q in cqueues]

    # print table of results for one run each (not averaged)
    print("Times for Bounded and Circular Queue without using Average")
    line = '-'*(13 + 14*len(queues_sizes))
    line2 = str('-'*13 + '+')*(1 + len(queues_sizes))
    print(line)
    print(str(" Queue Size  | " + ' '.join(" {:<10} |".format(q) for q in queues_sizes)))
    print(line2)
    print(str(" B que Time  | " + ' '.join(" {:<10} |".format(('%.2E' % Decimal(str(q)))[:10]) for q in bounded_queue_times)))
    print(line2)
    print(str(" C que Time  | " + ' '.join(" {:<10} |".format(('%.2E' % Decimal(str(q)))[:10]) for q in circular_queue_times)))
    print(line)


    # plot the terminal graph
    try:
        print('''
        Legend : 
        '*' : Points of the Bounded Queue
        '#' : Points of Circular Queue
        '+' : Points where both coincide''')

        plot2(queues_sizes, bounded_queue_times , circular_queue_times)
    except:
        print("Not able to print graph. Continuing .....")

    # run experiment using averages
    avg_b_queue_times = [avg_dequeue_experiment(BoundedQueue, size) for size in queues_sizes]
    avg_c_queue_times = [avg_dequeue_experiment(CircularQueue, size) for size in queues_sizes]

    # display table of averaged results (multiple runs for each data point)
    print("Times for Bounded and Circular Queue with Averaging")
    print(line)
    print(str(" Queue Size  | " + ' '.join(" {:<10} |".format(q) for q in queues_sizes)))
    print(line2)
    print(str(
        " B que Time  | " + ' '.join(" {:<10} |".format(('%.2E' % Decimal(str(q)))[:10]) for q in avg_b_queue_times)))
    print(line2)
    print(str(
        " C que Time  | " + ' '.join(" {:<10} |".format(('%.2E' % Decimal(str(q)))[:10]) for q in avg_c_queue_times)))
    print(line)

    try:
        # plot the graph
        print('''
        Legend : 
        '*' : Points of the Bounded Queue
        '#' : Points of Circular Queue
        '+' : Points where both coincide''')

        plot2(queues_sizes, avg_b_queue_times, avg_c_queue_times)
    except:
        print("Not able to print graph. Continuing .....")


if __name__ == '__main__':
    # calculate total program run time
    start = time.time()
    main()
    end = time.time()
    print("The program took {} seconds to run".format(end - start))

#the circular queue time remains constant even at increasing queues sizes, unlike the bonded queue which had significant increase in time  as the queue size increased




