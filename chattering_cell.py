# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:21:20 2021

@author: anooprac
"""

import izhikevich_cells as izh


class chCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        self.celltype='Chattering' # Regular spiking
        self.C=50
        self.k=1.5
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=25
        
        
myCell = chCell(4000)

myCell.simulate()
izh.plotMyData(myCell, 4000)