from setuptools import setup, find_packages

setup(
    name="vector_ai_plugin",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "openai",
        "psycopg2-binary",
        "pgvector",
        "numpy",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "vectorai=vector_ai_plugin.main:main"
        ]
    },
    author="Rodrigo Dias de Oliveira",
    description="A semantic search plugin for PostgreSQL using AI and vector embeddings.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
