import check50

@check50.check()
def test():
    """Hello World"""
    check50.run("python test.py").stdout("Hello World!", regex=False).exit(0)