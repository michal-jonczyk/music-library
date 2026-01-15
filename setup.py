from setuptools import setup, find_packages

setup(
    name='music_library',
    version='0.1.0',
    description='Music Library - Desktop app and REST API',
    author='Michał Jończyk',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.10',
    install_requires=[
        'fastapi==0.109.0',
        'uvicorn==0.27.0',
        'sqlalchemy==2.0.25',
        'pydantic==2.5.3',
    ],
    extras_require={
        'dev': [
            'pytest==7.4.4',
            'pytest-cov==4.1.0',
            'httpx==0.26.0',
        ]
    },
)