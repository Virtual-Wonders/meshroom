#!/usr/bin/env python
from celery import Celery
import subprocess

app = Celery('meshroomTasks', backend='rpc://', broker='pyamqp://vwuser:password1234@192.168.0.121:5672/myvhost')

@app.task
def runTask(nodeName, meshroomFile, parallelArgs):
    #print('meshroom_compute --node {nodeName} "{meshroomFile}" {parallelArgs} --extern'.format(nodeName=nodeName, meshroomFile=meshroomFile, parallelArgs=parallelArgs))
    #subprocess.call(['./meshroom/meshroom_compute', '"/home/vwadmin/meshroom_testing/test.mg"', '--node ' + nodeName, parallelArgs])
    subprocess.call('./meshroom/meshroom_compute --node {nodeName} "{meshroomFile}" {parallelArgs} --extern'.format(nodeName=nodeName, meshroomFile="/home/vwadmin/meshroom_testing/test.mg", parallelArgs=parallelArgs), shell=True)