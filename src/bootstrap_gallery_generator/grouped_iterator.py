from typing import Generator, Tuple


def grouped_iterator(input_iter: Generator,
                     groupsize: int) -> Generator[Tuple, None, None]:
    if groupsize < 1:
        raise ValueError
    counter = groupsize
    returnlist = []
    for value in input_iter:
        returnlist.append(value)
        counter -= 1
        if not counter:
            yield tuple(returnlist)
            counter = groupsize
            returnlist = []
    if returnlist:
        yield tuple(returnlist)
