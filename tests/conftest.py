import pytest
from freezegun import freeze_time
from click.testing import CliRunner
import mhl.commands
import os
import time
import platform

# this file is automatically loaded by pytest we setup various shared fixtures here


@pytest.fixture(scope="session", autouse=True)
def set_timezone():
    """Fakes the host timezone to UTC so we don't get different mhl files if the tests run on different time zones
    seems like freezegun can't handle timezones like we want"""
    os.environ['TZ'] = 'UTZ'
    time.tzset()


@pytest.fixture(autouse=True)
def set_hostname(monkeypatch):
    def fake_hostname():
        return 'myHost.local'
    monkeypatch.setattr(platform, 'node', fake_hostname)


@pytest.fixture
@freeze_time("2020-01-15 13:00:00")
def nested_mhl_histories(fs):

    # create mhl histories on different directly levels
    fs.create_file('/root/Stuff.txt', contents='stuff\n')
    runner = CliRunner()
    result = runner.invoke(mhl.commands.seal, ['/root'])
    assert result.exit_code == 0

    fs.create_file('/root/A/AA/AA1.txt', contents='AA1\n')
    fs.create_file('/root/A/AB/AB1.txt', contents='AB1\n')
    result = runner.invoke(mhl.commands.seal, ['/root/A/AA'])
    assert result.exit_code == 0

    fs.create_file('/root/B/B1.txt', contents='B1\n')
    result = runner.invoke(mhl.commands.seal, ['/root/B'])
    assert result.exit_code == 0

    fs.create_file('/root/B/BA/BA1.txt', contents='BA1\n')
    fs.create_file('/root/B/BB/BB1.txt', contents='BB1\n')
    result = runner.invoke(mhl.commands.seal, ['/root/B/BB'])
    assert result.exit_code == 0


@pytest.fixture
@freeze_time("2020-01-15 13:00:00")
def simple_mhl_history(fs):

    # create a simple mhl history with two files in one generation
    fs.create_file('/root/Stuff.txt', contents='stuff\n')
    fs.create_file('/root/A/A1.txt', contents='A1\n')

    runner = CliRunner()
    result = runner.invoke(mhl.commands.seal, ['/root'])
    assert result.exit_code == 0


