# -*- coding:utf-8 -*-
# @FileName  :celery_test.py
# @Time      :2024/9/12
# @Author    :Jack


if __name__ == "__main__":
    from tasks import sum_test

    # ************************** 同步调用 *****************************
    # result1 = sum_test(2, 5)


    # ************************** 异步调用 *****************************
    # delay： 是 Celery 任务的一个方法，用于将任务提交到任务队列中，以便在后台异步执行。
    result = sum_test.delay(x=2, y=5)

    # result.ready: 用于检查异步任务是否已经完成 True OR False
    while not result.ready():
        # 使用 result.state 来检查任务的状态，例如 SUCCESS、FAILURE PENDING 等。
        print(result.state)
    print(result.get())
