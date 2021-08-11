def separate_names(names):
    for full_name in names:
        for name in full_name.split(' '):
            yield name


def get_longest(namelist_filename):  # The pipeline function
    full_names = (name.strip() for name in open(namelist_filename))
    names = separate_names(full_names)
    lengths = ((name, len(name)) for name in names)
    return max(lengths, key=lambda x: x[1])


print(get_longest(namelist_filename='names.txt'))
