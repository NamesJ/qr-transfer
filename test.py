import filecmp
import os

import qrutil



def cleanup(out_dir):
    # Cleanup after yourself
    for file in os.listdir(out_dir):
        fpath = os.path.join(out_dir, file)
        os.remove(fpath)


def test_qrutil():
    test_dir = os.path.join('test', 'qrutil')
    infile = os.path.join(test_dir, 'input', 'test.txt')
    out_dir = os.path.join(test_dir, 'output')
    expected_dir = os.path.join(test_dir, 'expected_output')
    images = qrutil.encodeFile(infile)
    qrutil.export(images, out_dir)

    # Check that directory listings match
    expected_files = os.listdir(expected_dir)
    out_files = os.listdir(out_dir)
    if expected_files != out_files:
        result = False
    # Check that individual files match
    result = filecmp.cmpfiles(expected_dir, out_dir, expected_files)
    match, mismatch, errors = result
    if len(mismatch) or len(errors):
        result = False
    cleanup(out_dir)
    if result:
        print('[PASS]\ttest_qrutil()')
    else:
        print('[FAIL]\ttest_qrutil()')


if __name__ == '__main__':
    # Run all tests
    test_qrutil()
