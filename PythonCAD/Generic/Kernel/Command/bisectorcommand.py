#!/usr/bin/env python
#
# Copyright (c) 2010 Matteo Boscolo
#
# This file is part of PythonCAD.
#
# PythonCAD is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# PythonCAD is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public Licensesegmentcmd.py
# along with PythonCAD; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#This module provide a class for the bisector command
#
from Kernel.exception                      import *
from Kernel.composedentity                 import ComposedEntity
from Kernel.Command.basecommand            import *
from Kernel.GeoComposedEntity.bisector     import Bisector
from Kernel.GeoEntity.segment              import Segment


class BisectorCommand(BaseCommand):
    """
        this class rappresent the champfer command
    """
    def __init__(self, document):
        BaseCommand.__init__(self, document)
        self.exception=[ExcEntity,
                        ExcEntity, 
                        ExcPoint, 
                        ExcPoint,
                        ExcLenght,  
                        ]
        self.message=[  "Give me the first  Entity ID", 
                        "Give me the second Entity ID", 
                        "Give me the first point near the first entity",
                        "Give me the second point near the second entity", 
                        "Give me the bisector lengh"]
    def getEntsToSave(self):
        """
            get the chamfer segments
        """
        objEnt=[]
        ent1=self.document.getEntity(self.value[0])
        ent2=self.document.getEntity(self.value[1])
        
        cel1=ent1.getConstructionElements()
        seg1=Segment(cel1)
        
        cel2=ent2.getConstructionElements()
        seg2=Segment(cel2)
        arg={
             "OBJECTJOINT_0":seg1,
             "OBJECTJOINT_1":seg2,  
             "OBJECTJOINT_2":self.value[2], 
             "OBJECTJOINT_3":self.value[3], 
             "OBJECTJOINT_5":self.value[4], 
             }

        cmf=Bisector(arg)
        bisectorSegment = cmf.getReletedComponent()
        objEnt.append(bisectorSegment)
        return objEnt
        
    def applyCommand(self):
        """
            apply the champfer command
        """
        if len(self.value)!=5:
            raise PyCadWrongImputData("Wrong number of imput parameter")
        for _ent in self.getEntsToSave():
            self.document.saveEntity(_ent)
       
