import time

def new_run_id() -> int:
    return int(time.time() * 1000)

def log_landing_run(run_id, ):
    row = ()
    spark.createDataFrame([row], schema = SCHEMA).write.mode('append').saveAsTable(table_name)