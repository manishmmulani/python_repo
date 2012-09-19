# triangular.py compute first 100 triangular numbers. Do
# 'octo.py server triangular.py' on server with address IP
# and 'octo.py client IP' on each client. Server uses source
# & final, sends tasks to clients, integrates results. Clients
# get tasks from server, use mapfn & reducefn, return results.

source = dict(zip(range(100), range(100)))

def final(key, value):
    print key, value

def mapfn(key, value):
    for i in range(value + 1):
        yield key, i

def reducefn(key, value):
    return sum(value)

