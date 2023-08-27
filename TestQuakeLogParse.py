import unittest
from unittest.mock import patch
import io
import sys
import quakeLogParse

class TestQuakeLogParse(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_process_log(self, mock_urlopen):
        # Mock response for urllib.request.urlopen
        mock_response = io.BytesIO(b'InitGame:\nKill: 1 2 3: player1 killed player2 by MOD_RAILGUN\nShutdownGame:')
        mock_urlopen.return_value = mock_response

        # Call the processing function
        game_stats = quakeLogParse.process_log("fake_url")

        # Add your assertions here based on the expected game_stats

if __name__ == '__main__':
    unittest.main()
