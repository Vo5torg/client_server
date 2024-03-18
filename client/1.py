import asyncio
import time


def measure_time(func):
    async def wrapper(*args, **kwargs):
        a = 10
        if a == 10:
            result = await func(*args, **kwargs)
        else:
            result = 1
        return result

    return wrapper


@measure_time
async def my_func():
    await asyncio.sleep(1)
    return 2


async def my_func_1():
    print(await my_func())


print(asyncio.run(my_func()))


# def decorator(func):
#     def wrapper():
#         print('before main')
#         res = func()
#         print('after main')
#         return res
#     return wrapper
#
#
# @decorator
# def a():
#     return 1
#
# print(a())
