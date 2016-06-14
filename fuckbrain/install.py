import sys
import json
import tempfile
from jupyter_client.kernelspec import install_kernel_spec
from pathlib import Path


kernel_spec = {
    "argv": [sys.executable, "-m", "fuckbrain.kernel", "-f", "{connection_file}"],
    "name": "fuckbrain",
    "display_name": "Fuckbrain",
}

def install(kernel_name="fuckbrain", user=False, replace=False):
    """
    options:
        -k=<str>, --kernel-name=<str>
        -u, --user
        -r, --replace
    """
    path = Path(tempfile.mkdtemp(suffix="_kernels")) / kernel_name
    path.mkdir()
    with (path / "kernel.json").open("w") as f:
        json.dump(kernel_spec, f)

    return install_kernel_spec(str(path), kernel_name, user, replace)
