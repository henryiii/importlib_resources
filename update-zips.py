"""
Generate the zip test data files.

Run to build the tests/zipdataNN/ziptestdata.zip files from
files in tests/dataNN.

Replaces the file with the working copy, but does commit anything
to the source repo.
"""

import contextlib
import os
import pathlib
import zipfile


def main():
    suffixes = '01', '02'
    tuple(map(generate, suffixes))


def generate(suffix):
    root = pathlib.Path('importlib_resources/tests')
    zfpath = root / f'zipdata{suffix}/ziptestdata.zip'
    with zipfile.ZipFile(zfpath, 'w') as zf:
        for src, rel in walk(root / f'data{suffix}'):
            dst = 'ziptestdata' / rel
            print(src, '->', dst)
            zf.write(src, dst)


def walk(datapath):
    for dirpath, dirnames, filenames in os.walk(datapath):
        with contextlib.suppress(KeyError):
            dirnames.remove('__pycache__')
        for filename in filenames:
            res = pathlib.Path(dirpath) / filename
            rel = res.relative_to(datapath)
            yield res, rel


__name__ == '__main__' and main()
