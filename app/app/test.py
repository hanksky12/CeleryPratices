from app.app.tasks.tasks import add, tsum, sub
from celery import chord
# for i in range(1000):
#     result = sub.s(100, 10).apply_async()
#     print(f"結果 {result.get()}")




task_list = []
for i in range(1000):
    task = add.signature((i, 10), countdown=1)
    task_list.append(task)

result = chord(task_list)(tsum.s())
print(result.get())