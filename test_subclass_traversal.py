from jaraco.classes.ancestry import iter_subclasses


def test_deep_subclass_chain():
    root = type('Root', (), {})
    classes = [root]
    for number in range(1100):
        classes.append(type(f'Level{number}', (classes[-1],), {}))
    assert list(iter_subclasses(root)) == classes[1:]


def test_shared_descendants_are_expanded_once():
    calls = []

    class Meta(type):
        def __subclasses__(cls):
            calls.append(cls)
            return super().__subclasses__()

    root = Meta('Root', (), {})
    left = Meta('Left', (root,), {})
    right = Meta('Right', (root,), {})
    shared = Meta('Shared', (left, right), {})
    leaf = Meta('Leaf', (shared,), {})
    assert list(iter_subclasses(root)) == [left, shared, leaf, right]
    assert calls.count(shared) == 1
    assert calls.count(leaf) == 1


def test_unhashable_classes():
    class Meta(type):
        __hash__ = None

    root = Meta('Root', (), {})
    child = Meta('Child', (root,), {})
    assert list(iter_subclasses(root)) == [child]
