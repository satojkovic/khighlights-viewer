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
        self.highlight = KindleHighlights('B00H992JJA')

    def test_scrape_popular_highlight(self, setup):
        assert self.highlight, "should be not Null"
