import json

def remove_hash_from_pal(pal):
    dump = json.dumps(pal)    
    result = json.loads(dump.replace("#", ""))
    return result
