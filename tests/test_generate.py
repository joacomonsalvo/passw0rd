import pytest
from passw0rd import generate


@pytest.mark.parametrize(
	"input_a, expected",
	[
		(generate(), str)
	]
)
def test_generate(input_a, expected):
	assert type(input_a) is expected

"""
def test_tmp_dir(tmpdir):
	data_in = "Something"
	fpath = f"{tmpdir}/test.txt"
	escribir(fpath, data_in)

	with open(fpath) as file_out:
		data_out = file_out.read()

	assert data_in == data_out
"""
