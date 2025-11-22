import redis

pool = redis.ConnectionPool(host="127.0.0.1", port=6379)
r = redis.Redis(connection_pool=pool)
pipe = r.pipeline(transaction=True)
a = pipe.set("name", "alex")
b = pipe.set("role", "sb")
c = pipe.execute()
print(a)
print(b)
print(c)
