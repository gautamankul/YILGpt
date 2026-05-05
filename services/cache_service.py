import redis

try:
    cache = redis.Redis(host="localhost", port=6379, db=0)
    cache.ping()
    REDIS_AVAILABLE = True
except:
    REDIS_AVAILABLE = False


def get_cached(query: str):
    if REDIS_AVAILABLE:
        return cache.get(query)
    return None


def set_cache(query: str, response: str):
    if REDIS_AVAILABLE:
        cache.set(query, response)
