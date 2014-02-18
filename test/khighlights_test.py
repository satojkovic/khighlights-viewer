import pytest
from hamcrest import *
import os
import sys
sys.path.append(os.path.join
                (os.path.basename(__file__),
                 '../khighlights_viewer'))

from khighlights import KindleHighlights


class KindleHighlightsTest():

    @pytest.fixture
    def setup(self):
        return KindleHighlights('B00H992JJA')

    def get_num_of_popular_test(self):
        expected = 5
        actual = setup.get_num_popular()

        assert_that(actual, equal_to(expected))
