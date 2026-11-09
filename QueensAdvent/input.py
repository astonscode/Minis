def choose(choices, e, text):
    # acceptable answers (-1 for any, list for else)
    # e for error message
    # text for input
    badResponse = True
    while badResponse:
        try:
            choices = list(choices)
            c = input(text)
            if c in choices or choices == [-1] or c.lower() in choices:
                badResponse = False
                return c
            else:
                raise ValueError 
        except ValueError:
            print(e)
            badResponse = True