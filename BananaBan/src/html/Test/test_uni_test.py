import pytest
import discord
from discordtest import ban

@pytest.fixture
def ctx():
    return discord.ext.commands.Context(
        prefix="!",
        guild=discord.Guild(id=123),
        channel=discord.TextChannel(id=456),
        author=discord.Member(id=789, name="TestUser")
    )

@pytest.fixture
def member():
    return discord.Member(id=987, name="TestMember")

@pytest.fixture
def steamid_valid():
    return "STEAM_1:0:123456"

@pytest.fixture
def steamid_invalid():
    return "INVALID_STEAMID"

@pytest.fixture
def reason():
    return "Violation of rules"

@pytest.fixture
def server():
    return "Server1"

@pytest.mark.asyncio
async def test_valid_steamid(ctx, member, steamid_valid, reason, server):
    result = await ban(ctx, member, steamid_valid, reason, server)
    assert result == "[ + ] DONE"

@pytest.mark.asyncio
async def test_invalid_steamid(ctx, member, steamid_invalid, reason, server):
    result = await ban(ctx, member, steamid_invalid, reason, server)
    assert result == "steamid er ikke korrekt"
