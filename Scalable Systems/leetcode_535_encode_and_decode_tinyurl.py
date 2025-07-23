# Leetcode Problem: 535. Encode and Decode TinyURL
# https://leetcode.com/problems/encode-and-decode-tinyurl/
# 
# 🧠 Concept: Hashing, Dictionary-based mapping, URL shortening
# 🛠️ Approach: 
# - Salt the original long URL with a counter to prevent collisions.
# - Generate a short MD5 hash (first 6 chars).
# - Store mapping of short_url -> long_url in a dictionary.
# 
# ⏱️ Time Complexity:
# - encode: O(1)
# - decode: O(1)
# 
# 💾 Space Complexity:
# - O(N) for storing N URL mappings.

import hashlib

class Codec:
    def __init__(self):
        self.counter = 0
        self.url_map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        self.counter += 1
        salted_url = longUrl + str(self.counter)
        hash_code = hashlib.md5(salted_url.encode()).hexdigest()[:6]
        short_url = f"http://tinyurl.com/{hash_code}"
        self.url_map[short_url] = longUrl
        return short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.url_map[shortUrl]
