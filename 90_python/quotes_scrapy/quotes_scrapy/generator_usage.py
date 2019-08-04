"""
1. 一般来说，for x in []/()/string 中，in后面跟的对象是一个可以迭代的对象。
这样有个缺点，如果后面的对象特别大的时候，会全部加载到内存中。

2. 为了解决这种问题，可以使用生成器。
生成器是可以迭代的，但只可以读取它一次。因为用的时候才生成。
只可以读取一次是什么一次呢？比如有一列表 a = [1, 2, 3, 4]， 我们可以通过index反复读取，但是生成器不可以。
例如 generator = (x + 1 for x in range(3))，请注意，这里使用的是()。不是列表，列表是[]

3. 带有 yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代，工作原理同上。
yield 是一个类似 return 的关键字，但是不会退出for循环。

4. 我们可以使用python中内置的next()方法读取生成器的内容
"""


def generator_function():
    for i in range(3):
        yield i
'''
gen = generator_function()
print(next(gen))
print(next(gen))
print(next(gen))
# 如果yield的内容都取完了，会报StopIteration异常
print(next(gen))
'''

"""
    生成器使用方式2，在for循环中使用，为什么for循环中不会提示StopIteration异常呢？
    for循环会自动捕捉到这个异常并停止调用next()

for gen in generator_function():
	print(gen)
"""