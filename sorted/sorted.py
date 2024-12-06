from os import getcwd, path

def sort_files():
    """
    Opens several files, sorts them by a number of lines and writes
    their contents into a new file.

    """
    cwd = getcwd()
    files = {}
    # Read all files into a dictionary keyed by a tuple of file line
    # count and a filename.
    for i in range(1, 4):
        filename = f'{i}.txt'
        with open(path.join(cwd, 'files', filename), encoding='UTF-8') as file:
            lines = file.readlines()
            key = (len(lines), filename)
            files[key] = lines
    # Sort files by the count of lines.
    files = dict(sorted(files.items()))

    # Open a new file to write files there.
    with open(path.join(cwd, 'files', 'sorted.txt'), 'w', encoding='UTF-8') as file:
        for (count, filename), lines in files.items():
            file.write(f'{filename}\n')
            file.write(f'{count}\n')
            file.writelines(lines)
            file.write('\n')
