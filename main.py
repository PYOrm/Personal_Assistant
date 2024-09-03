from multiprocessing import Process
import os 

def runserver():
    os.system('python manage.py runserver')

def process_tasks():
    os.system('python manage.py process_tasks')

if __name__ == '__main__':
    processes=[
        Process(target=runserver),
        Process(target=process_tasks),        
    ]
    for p in processes:
        p.start()

    for p in processes:
        p.join()