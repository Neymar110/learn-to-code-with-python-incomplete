class Job():
    pass

class Waiter(Job):
    pass

print(issubclass(Waiter, Job))

Jane = Waiter()

Gardener = Job()

print(isinstance(Gardener, Job))

print(isinstance(Jane, Waiter))

# The first argument in isinstance is the instance and the seccond is the class

# The first argument in issubclass is the sub class then the super class

print(isinstance(1, int))

print(isinstance(len, object))

#It can be as vague as object