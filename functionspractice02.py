#!/usr/bin/env python3

import datetime
import time
import os
#
def logarchive():
    nowtime = datetime.datetime.now().strftime("%d_%m_%y,%H:%M")
    logname = "log_" + nowtime + ".old"
    os.rename("/home/student/log.txt", "/tmp/log/" + logname)
