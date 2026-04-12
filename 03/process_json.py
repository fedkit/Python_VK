from typing import Callable, Any
import json


def process_json(
    json_str: str,
    required_keys: list[str] | None = None,
    tokens: list[str] | None = None,
    callback: Callable[[str, str], Any] | None = None,
) -> None:
    
    if (not required_keys) or (not tokens) or (not callback):
        return None
    
    jstr = json.loads(json_str)

    for i in jstr:
        jstr[i] = [word.lower() for word in jstr[i].split()]

    lower_tokens = [word.lower() for word in tokens]

    for key in required_keys:
        if key in jstr:
            for token in jstr[key]:
                if token in lower_tokens:
                    callback(key, token)