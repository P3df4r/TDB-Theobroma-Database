#!/usr/bin/env python3
#coding: utf-8
import os
import BlastClass
from threading import Thread

class BlastThread(Thread):
    blastInstance = None
    bValor = None
    query = None
    def __init__(self, databName, downDName, xmlName):
        outputPath = os.path.join(downDName, xmlName)
        self.blastInstance = BlastClass.Blast(databName, outputPath)
        Thread.__init__(self)
    def prepare(self, bValor, query):
        self.bValor = bValor
        self.query = query
    def run(self):
        self.blastInstance.run(self.bValor, self.query)

