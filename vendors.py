import subprocess
import shutil
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        install_vendors(
            self.metadata.core.dependencies, self.config["ignore-dependencies"]
        )


def install_vendors(dependencies, ignore):
    vendor = [p for p in dependencies if all([ig not in p for ig in ignore])]
    print(" ".join(vendor))
    if not shutil.which("uv"):
        print("uv is not found in PATH.")
    uv_args = ["uv", "pip", "install", "-t", "src/subtitleterms/vendor", *vendor]
    subprocess.run(uv_args)
