from twttr import shorten
def test():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("t3113r") == "t3113r"
    assert shorten("T@!!*r") == "T@!!*r"


