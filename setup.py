from setuptools import setup

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name="scratchconnectplus",
    version="5.0",
    description="Continuation of the ScratchConnect project that interacts with Scratch's various services.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jdev082/scratchconnectplus/",
    author="jdev082",
    author_email="jdev0894@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords=['connect scratch', 'scratch api', 'api', 'scratch', 'bot', 'scratch bot',
              'scratch cloud', 'scratch cloud variables', 'scratch data', 'scratch stats', 'cloud requests',
              'fast cloud requests'],
    packages=["scratchconnect"],
    install_requires=['requests', 'websocket-client', 'Pillow'],
    extras_require={
        'terminal': ['scScratchTerminal']
    }
)
