import redis


def test_redis():
    r = redis.Redis(host="192.168.190.2", port=6379, password="")
    r.set("name", "jason")
    assert str(r.get("name")) == "jason"
