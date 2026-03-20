from setuptools import setup

setup(
    name="omniswap",
    version="1.0.0",
    description="The simplest Solana swap SDK. Built for bots & AI agents. Best prices via Jupiter.",
    long_description=open("README.md").read() if __import__("os").path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    author="OmniSwap",
    url="https://penguin500.github.io/omniseedai/docs/",
    py_modules=["omniswap"],
    install_requires=["requests>=2.28.0"],
    extras_require={"sign": ["solders>=0.18.0"]},
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Office/Business :: Financial",
    ],
    keywords="solana swap jupiter defi bot agent trading",
)
