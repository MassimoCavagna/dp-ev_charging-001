import time

def new_run_id() -> int:
    return int(time.time() * 1000)

def 