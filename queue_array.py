# CPE 202 Lab3 
# Name: Ashley Sutter
# Student ID: 011278952
# Date (last modified): 1/25/2019
#
# Lab 3
# Section 5
# Purpose of Lab: Understand queue, write queue w arrays
# additional comments


class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0
        self.last = 0
        self.first = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return self.num_items == 0

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return self.num_items == self.capacity 

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.is_full() == False:
           self.items[self.last] = item
           self.last = (self.last+1) % self.capacity
           self.num_items += 1
        else:
           raise IndexError

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.is_empty() == False:
           temp = self.first
           self.first = (self.first+1) % self.capacity
           self.num_items -= 1
           return self.items[temp]
        else:
           raise IndexError()

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items

    def peek(self):
        '''Returns the next item that will be dequeued
        return'''
        if self.is_empty() == True:
            raise IndexError()
        else:
            return self.items[self.first]
