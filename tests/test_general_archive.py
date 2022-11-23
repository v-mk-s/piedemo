import pytest
import zipfile
import bz2
from piedemo.checkpoint.archive import GeneralArchiveMember


def test_zipfile():
    MSG = "Hello world"
    with zipfile.ZipFile("test.zip", 'w') as zf:
        zf.writestr("1.txt", MSG)

    GA = GeneralArchiveMember('test.zip', '1.txt')
    assert GA.listarchive() == ['1.txt']
    with GA.temporary_extract() as ga:
        assert str(ga).endswith('1.txt'), ga
        assert ga.read_text() == MSG


def test_bz2():
    MSG = b"Hello world"
    with bz2.open("1.txt.bz2", 'wb') as f:
        f.write(MSG)

    GA = GeneralArchiveMember('1.txt.bz2', '1.txt')
    assert GA.listarchive() == ['1.txt']
    with GA.temporary_extract() as ga:
        assert str(ga).endswith('1.txt'), ga
        assert ga.read_bytes() == MSG
