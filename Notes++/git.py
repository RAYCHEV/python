from subprocess import call
import os

ret = os.system('git pull')


print(ret)
