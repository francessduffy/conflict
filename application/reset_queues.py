from redis import Redis
import rq

def reset_queues():
    queue = rq.Queue('simulator', connection=Redis.from_url('redis://ec2-54-146-142-160.compute-1.amazonaws.com:6379'))
    print('simulator queue contents prior:', queue.count)
    queue.empty()
    print('simulator queue contents after:', queue.count)
    queue = rq.Queue('full_simulator', connection=Redis.from_url('redis://ec2-54-146-142-160.compute-1.amazonaws.com:6379'))
    print('full_simulator queue contents prior:', queue.count)
    queue.empty()
    print('full_simulator queue contents after:', queue.count)