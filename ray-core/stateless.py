import ray

ray.init()


@ray.remote
def append_one(container):
    container.append(1)
    return container


def local_append_one(container):
    container.append(1)
    return container


container = []

future = append_one.remote(container)
result = ray.get(future)
print(result)  # Output: [1]
print(container)  # Output: []

local_append_one(container)
print(container)  # Output: [1]
