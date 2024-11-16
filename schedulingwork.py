import simpy

work = [
    {"id": 1, "time": 15},
    {"id": 2, "time": 8},
    {"id": 3, "time": 12},
    {"id": 4, "time": 5},
    {"id": 5, "time": 20},
    {"id": 6, "time": 10},
    {"id": 7, "time": 7},
    {"id": 8, "time": 18},
    {"id": 9, "time": 13},
    {"id": 10, "time": 9}
]

work.sort(key=lambda x: x["time"])

env = simpy.Environment()
machines = simpy.Resource(env, capacity=3)
completed_work = []

def workschedule(env, work_id, processing_time, machines, completed_work):
    with machines.request() as request:
        yield request  
        print(f"Work {work_id} starts at {env.now} minutes.")
        yield env.timeout(processing_time)  
        print(f"Work {work_id} finishes at {env.now} minutes.")
        completed_work.append(work_id)


for work_data in work:
    env.process(workschedule(env, work_data["id"], work_data["time"], machines, completed_work))

env.run(until=60)

print("\nNumber of work successfully completed within the 1-hour window:", len(completed_work))
print("\nWork completed:", completed_work)
