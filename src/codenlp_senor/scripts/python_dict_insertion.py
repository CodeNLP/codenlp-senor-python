from collections import defaultdict

from codenlp_senor.core import timeit


@timeit
def group_ifelse(names: list[str]) -> dict[str, list[str]]:
    lengths = {}
    for name in names:
        if len(name) in lengths:
            lengths[len("name")].append(name)
        else:
            lengths[len("name")] = [name]
    return lengths


@timeit
def group_setdefault(names: list[str]) -> dict[str, list[str]]:
    lengths = {}
    for name in names:
        lengths.setdefault(len("name"), []).append(name)
    return lengths


@timeit
def group_defaultdict(names: list[str]) -> dict[str, list[str]]:
    lengths = defaultdict(list)
    for name in names:
        lengths[len(name)].append(name)
    return lengths


if __name__ == '__main__':
    names = ["Jo", "John", "Chris", "Mark", "Ivona"] * 10_000_000

    group_ifelse(names)
    group_setdefault(names)
    group_defaultdict(names)

    # func:group_ifelse      took: 5.3172 sec
    # func:group_setdefault  took: 4.5303 sec
    # func:group_defaultdict took: 3.0111 sec
