from yake import KeywordExtractor

# Extract only keywords without scores
def key_extractor(text):
    # Create a KeywordExtractor instance
    kw_extractor = KeywordExtractor(top=5, windowsSize=0)
    # Extract keywords from the text
    keywords = kw_extractor.extract_keywords(text)
    # Extract just the keyword part from each (keyword, score) tuple
    keywords_only = [keyword for keyword, score in keywords]
    return keywords_only

# Text from which keywords will be extracted
text = "YAKE (Yet Another Keyword Extractor) is a Python library for extracting keywords from text."
l = key_extractor(text)
print(l)

