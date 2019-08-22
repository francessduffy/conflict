from redis import Redis
from rq import get_current_job
from app.model.results import fetchoutput
from app.run_simulator import simulator
import rq
import matplotlib.pyplot as plt
import os

def simulator_instance():
    rq.Queue('simulator', connection=Redis.from_url('redis://'))
    modelresults = fetchoutput()
    return modelresults

def full_simulator():
    data = simulator()
    data.to_csv('test.csv', index=False)

def launch_simulator():
    # global finished
    queue = rq.Queue('full_simulator', connection=Redis.from_url('redis://'))
    job = queue.enqueue('app.tasks.full_simulator')
    # finished = True

def get_progress():
    fulljob = get_current_job(connection=Redis.from_url('redis://'), job_class=full_simulator())
    return fulljob.meta.get('progress', 0) if fulljob is not None else 100

def graphing(df):
    if os.path.exists("app/static/graph1.png"):
        os.remove("app/static/graph1.png")
    if os.path.exists("app/static/graph2.png"):
        os.remove("app/static/graph2.png")
    if os.path.exists("app/static/graph3.png"):
        os.remove("app/static/graph3.png")
    df.plot(kind='line', x='rounds', y=['strength1', 'strength2', 'strength3'])
    plt.savefig('app/static/graph1.png')
    df.plot(kind='line', x='rounds', y=['oneandtwo', 'oneandthree', 'twoandthree'])
    plt.savefig('app/static/graph2.png')
    df.plot(kind='line', x='rounds', y=['community1defend', 'community2defend', 'community3defend'])
    plt.savefig('app/static/graph3.png')
