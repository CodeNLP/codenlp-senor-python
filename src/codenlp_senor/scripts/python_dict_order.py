from collections import defaultdict

from codenlp_senor.core import timeit


@timeit
def first_distinct_item(items: list[str]) -> list[str]:
    groups = defaultdict(list)
    for item in items:
        groups[item].append(1)
    for k, v in groups.items():
        if len(v) == 1:
            return k
    return None


@timeit
def first_distinct_item_2pass(items: list[str]) -> list[str]:
    groups = defaultdict(list)
    for item in items:
        groups[item].append(1)
    for item in items:
        if len(groups.get(item, [])) == 1:
            return item
    return None


if __name__ == '__main__':
    names = ["Jo", "John", "Chris", "Mark", "Ivona"] * 10_000_000 + ["Distinct"]

    first_distinct_item(names)
    first_distinct_item_2pass(names)

    # func:first_distinct_item       took: 2.0438 sec
    # func:first_distinct_item_2pass took: 7.0440 sec
