import pytest
import subprocess

@pytest.fixture
def genpat(tmp_path):
	"""
	generate test video
	"""
	vidfn = tmp_path / 'bars.avi'
	subprocess.check_call(['/Users/aznable/Desktop/exercise-2-ffmpeg-ZeyuKeithFu/ffmpeg', '-v', 'warning','-f', 'lavfi',
						   '-i', 'smptebars','-t', 5., str(vidfn)])
	return vidfn