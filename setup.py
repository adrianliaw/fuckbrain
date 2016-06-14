from setuptools import setup

setup(
    name="fuckbrain",
    version="0.1",
    license="MIT",
    packages=["fuckbrain"],
    install_requires=[
        "jupyter_client",
        "ipykernel",
        "clime",
    ],
    package_data={
        "fuckbrain": ["*.pkl"]
    },
)
