# fout = open('output.txt', 'w')
# line1 = "This here's the wattle,\n"
# fout.write(line1)

# line2 = "the emblem of our land.\n"
# fout.write(line2)
# fout.close()

import os
def walk(dirname):
  for name in os.listdir(dirname):
    path = os.path.join(dirname, name)
    print(path)
  if os.path.isfile(path):
    print(path)
  else:
    walk(path)
    
walk('unit-8')