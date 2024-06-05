import pathlib

import pytest
from typer.testing import CliRunner

from inspectds.cli import app


runner = CliRunner()


@pytest.mark.parametrize(
    "path", [pytest.param(path, id=path.name) for path in pathlib.Path("tests/data/").glob("*")]
)
def test_grib(path: pathlib.Path) -> None:
    if path.suffix == ".grib":
        pytest.importorskip("cfgrib")
    if path.suffix == ".slf":
        pytest.importorskip("xarray_selafin")
    result = runner.invoke(app, [path.as_posix()])
    assert result.exit_code == 0
    assert "Dimensions" in result.stdout
    assert "attributes" not in result.stdout
