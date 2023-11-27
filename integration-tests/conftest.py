import pytest
import logging
import sh
import json
import toml
import os
from dynaconf import Dynaconf

@pytest.fixture
def settings():
    yield Dynaconf(
        envvar_prefix="CSI_CLIENT_TOOLS",
        settings_files=["settings.toml", ".secrets.yaml"],
        environments=True,
    )

