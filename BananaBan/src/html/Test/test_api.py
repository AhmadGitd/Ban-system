# test_bot_functions.py
import unittest
from unittest.mock import AsyncMock, MagicMock, patch
from discordtest import ban  # Assuming discordtest is the name of your script

class TestBanFunction(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.ctx = MagicMock()
        self.member = MagicMock()
        self.steamid_valid = "STEAM_1:0:123456"
        self.steamid_invalid = "INVALID_STEAMID"
        self.reason = "Violation of rules"
        self.server = "Server1"

    @patch('discordtest.finduser_request', new_callable=AsyncMock)
    @patch('discordtest.banuser_request', new_callable=AsyncMock)
    async def test_valid_steamid(self, mock_banuser_request, mock_finduser_request):
        mock_finduser_request.return_value = "null"
        mock_banuser_request.return_value = ("[ + ] DONE", 200)
        
        result = await ban(self.ctx, self.member, self.steamid_valid, self.reason, self.server)
        
        self.assertEqual(result, "[ + ] DONE")
        self.ctx.guild.ban.assert_called_with(self.member)

    @patch('discordtest.finduser_request', new_callable=AsyncMock)
    async def test_invalid_steamid(self, mock_finduser_request):
        mock_finduser_request.return_value = "null"
        
        result = await ban(self.ctx, self.member, self.steamid_invalid, self.reason, self.server)
        
        self.assertEqual(result, "steamid er ikke korrekt")

if __name__ == '__main__':
    unittest.main()
