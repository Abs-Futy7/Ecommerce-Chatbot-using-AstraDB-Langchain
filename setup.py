from setuptools import find_packages, setup

setup(
    name="Ecommerce-Chatbot",
    version="0.0.0",
    author="Abs",
    author_email="bojackabs@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask']
)