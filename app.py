from prefect import flow, task
import time


@task(log_prints=True)
def task_A():
    print("Running Task A")
    time.sleep(3)
    return "Task A"


@task(log_prints=True)
def task_B():
    print("Running Task B")
    time.sleep(10)
    return "Task B"


@task(log_prints=True)
def task_C():
    print("Running Task C")
    time.sleep(10)
    return "Task C"


@task(log_prints=True)
def task_D():
    print("Running Task D")
    time.sleep(10)
    return "Task D"


@task(log_prints=True)
def task_E(result_B, result_C, result_D):
    print("Running Task E")
    time.sleep(2)
    return f"{result_B} + {result_C} + {result_D} + Task E"


@flow(log_prints=True)
def my_subflow():
    print("Running My Subflow")
    runB = task_B.submit()
    runC = task_C.submit()
    runD = task_D.submit()

    return [x.result() for x in [runB, runC, runD]]


@flow(log_prints=True)
def my_flow():
    print("Running My Flow")
    result_A = task_A()
    result_B, result_C, result_D = my_subflow()
    result_E = task_E(result_B, result_C, result_D)
    print(f"{result_A} + {result_E}")


if __name__ == "__main__":
    my_flow()
