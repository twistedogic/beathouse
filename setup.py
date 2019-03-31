from setuptools import setup, find_packages

setup(
    name="beathouse",
    version="0.0.1",
    author="Jordan Li",
    author_email="twistedogic@gmail.com",
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
)
