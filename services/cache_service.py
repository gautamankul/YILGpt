import redis

cache = redis.Redis(host='localhost', port=6379, db=0)

def get_cached(query: str):
    return cache.get(query)

def set_cache(query: str, response: str):
    cache.set(query, response)