import os.path
import pytest
import flatdict
from src.config_set import config_settings


def test_toflatdict():
    assert config_settings.to_flatdict("D:\Aishwarya_Work\pythonProject3\configurat.cfg") == flatdict.FlatDict({})
    assert type(config_settings.to_flatdict("D:\Aishwarya_Work\pythonProject3\tests\configurations.cfg")) == flatdict.FlatDict
    assert type(config_settings.to_flatdict("D:\Aishwarya_Work\pythonProject3\tests\schedule.yml")) == flatdict.FlatDict
    assert config_settings.to_flatdict("D:\Aishwarya_Work\pythonProject3\reschedule.yml") == "File path or name is not correct, lease check again wirh correct filename."
