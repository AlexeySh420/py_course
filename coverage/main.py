def howmanyletters(input: str) -> str:
    if len(input) < 1:
        return 'no data'
    elif len(input) < 3:
        return 'less than three letters?!'
