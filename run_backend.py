import os
import subprocess
import time

os.chdir("yolo-9000/darknet")
p = subprocess.Popen(['./darknet', 'detector', 'test', 'cfg/combine9k.data', 'cfg/yolo9000.cfg', '../yolo9000-weights/yolo9000.weights'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
time.sleep(15)
stdout, stderr = p.communicate(input='data/dog.jpg')
p.stdin.write('data/dog.jpg\n')
#print(p.stdout)
#time.sleep(10)
p.stdin.write('data/person.jpg')
#stdout, stderr = p.communicate(input='data/person.jpg')
print(p.stdout)
