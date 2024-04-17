from prefect import flow, task


@task(log_prints=True)
def task_A():
    print("Running Task A")
    return "Task A"


@task(log_prints=True)
def task_B():
    print("Running Task B")
    return "Task B"


@task(log_prints=True)
def task_C():
    print("Running Task C")
    return "Task C"


@task(log_prints=True)
def task_D():
    print("Running Task D")
    return "Task D"


@task(log_prints=True)
def task_E(result_B, result_C, result_D):
    print("Running Task E")
    return f"{result_B} + {result_C} + {result_D} + Task E"


@flow(log_prints=True)
def my_flow():
    print("Running My Flow")
    result_A = task_A()
    result_B = task_B()
    result_C = task_C()
    result_D = task_D()
    result_E = task_E(result_B, result_C, result_D)
    print(result_E)


if __name__ == "__main__":
    my_flow()
