import pytest
from hamcrest import *
import os
import sys
sys.path.append(os.path.join
                (os.path.basename(__file__),
                 '../khighlights_viewer'))

from khighlights import KindleHighlights


class TestKindleHighlights():

    @pytest.fixture
    def setup(self):
        return KindleHighlights('B00H992JJA')

    def test_get_num_of_popular(self, setup):
        assert setup.get_num_popular(), "should get num of popular highlights"
