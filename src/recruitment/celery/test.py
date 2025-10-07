# coding=utf-8

from tasks import add

result = add.delay(5, 5)
print("Is task ready: %s" % result.ready())

run_result = result.get(timeout=1)
print("task result: %s" % run_result)
