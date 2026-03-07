from setuptools import setup, find_packages

setup(
    name="semi-ai-toolkit",
    version="0.1.0",
    description="Open-source AI tools for semiconductor equipment",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="MST Semiconductor (集芯科技)",
    author_email="contact@ai-mst.com",
    url="https://github.com/shensi8312/semi-ai-toolkit",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.24",
        "pandas>=2.0",
        "scipy>=1.10",
        "scikit-learn>=1.3",
        "torch>=2.0",
    ],
    extras_require={
        "dev": ["pytest", "flake8", "black", "isort"],
    },
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
