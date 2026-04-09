import re
from typing import List

URL_REGEX = re.compile(
    r'\b(?:https?://|www\.)'           
    r'[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*' 
    r'(?:\:\d+)?'                        
    r'(?:/[a-zA-Z0-9\-./]*)?',           
    re.IGNORECASE
)

TRAILING_PUNCT = ',.!?;:'

def find_urls(text: str) -> List[str]:
    urls = []
    for match in URL_REGEX.findall(text):
        url = match.rstrip(TRAILING_PUNCT)
        domain_part = url.split('/')[0]  
        if '..' in domain_part:
            continue
        urls.append(url)
    return urls