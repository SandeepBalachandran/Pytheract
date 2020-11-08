![](./images/preview.png)
<h1 align='center'>Pytheract</h1>
<p align="center"> 
  <a href="https://github.com/SandeepBalachandran/Pytract/releases/" target="_blank">
    <img alt="GitHub release" src="https://img.shields.io/github/v/release/SandeepBalachandran/Pytract?include_prereleases&style=flat-square">
  </a> 

  <a href="https://github.com/SandeepBalachandran/Pytract/commits/master" target="_blank">
    <img src="https://img.shields.io/github/last-commit/SandeepBalachandran/Pytract?style=flat-square" alt="GitHub last commit">
  </a>

  <a href="https://github.com/SandeepBalachandran/Pytract/issues" target="_blank">
    <img src="https://img.shields.io/github/issues/SandeepBalachandran/Pytract?style=flat-square&color=red" alt="GitHub issues">
  </a>

  <a href="https://github.com/SandeepBalachandran/Pytract/pulls" target="_blank">
    <img src="https://img.shields.io/github/issues-pr/SandeepBalachandran/Pytract?style=flat-square&color=blue" alt="GitHub pull requests">
  </a>

  </br>

  <a href="https://standardjs.com" target="_blank">
    <img alt="ESLint" src="https://img.shields.io/badge/code_style-standard-brightgreen.svg?style=flat-square">
  </a>
  
  <a href="" target="_blank">
    <img alt="ESLint" src="https://img.shields.io/github/stars/SandeepBalachandran/Pytract">
  </a>
  
  <a href="" target="_blank">
    <img alt="ESLint" src="https://img.shields.io/github/forks/SandeepBalachandran/Pytract">
  </a>
   <a href="" target="_blank">
    <img alt="Codesize" src="https://img.shields.io/github/languages/code-size/SandeepBalachandran/Pytract.svg">
  </a>
  <a href="" target="_blank">
    <img alt="Top Language" src="https://img.shields.io/github/languages/top/SandeepBalachandran/Pytract.svg">
  </a>
  
</p>
<hr>

<h2 align="center">Optical character recognition using tesseract </h2> 

# Table of contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Installation](#installation)
- [Contribute](#contribute)

# Introduction

An application that extract meaningful data from any type of documents. [Currently support image formats .Other file supports in progress.].

# Usage
*For **end users**.*

Currently in progress to set up an environment

### Flow
 * Upload a file using the frontend.
 * Tesseract will extract the texts available in the file uploaded.




# Installation
*For **developers**.*
### Prerequisites

The application has a number of dependencies. Kindly ensure you have the following installed on your machine:

- [ ] Python
- [ ] Python (Complete details provided below)
- [ ] Mongo
- [ ] Mongodb compass(optional , alternatives available)
- [ ] Tesseract
- [ ] Git


- Python
  - [Official download.](https://www.python.org/downloads/)
  
- Tesseract 
  - [Offcial documentation.](https://github.com/tesseract-ocr/tessdoc/blob/master/Documentation.md)
  - [Offcial download section.](https://github.com/tesseract-ocr/tessdoc/blob/master/Downloads.md)
  - [V5 alpha using in dev machine.](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe)

- Mongo
   - [Official download.](https://www.mongodb.com/try/download/community)
   
- Git
  - [Official download.](https://git-scm.com/downloads)
  
  
  ### Running the Application
  
  1. Install Python if it is not installed already. Add the environment variables and check version. 
    ```cmd
      C:\Users\username> python
      Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
      Type "help", "copyright", "credits" or "license" for more information.
    ```
  2. Install Mongodb if it is not installed already.
  3. Install Mongodb compass. ( Client )
  4. Go to Mongo db bin folder and run the server
   ```cmd
   C:\Program Files\MongoDB\Server\4.4\bin> mongod
   ```
  It will be available in port 27017
  
  5. Go to compass get in to the db
  
  ```cmd
    mongodb://localhost:27017
  ```
  6. Install Tesseract

  7. Clone the repository
  
  ```cmd
  git clone https://github.com/SandeepBalachandran/Pytheract.git
  ```
  8. Check into the cloned repository
  
  ```cmd
  cd Pytheract
  ```
  9. If you are using Pipenv, setup the virtual environment and start it as follows:
  
  ```cmd
  pipenv install 
  ```

  10 . Run Flask

  ```cmd
  set FLASK_APP=app.py
  set FLASK_ENV=development
  flask run 
  ```

  It will be available in port 5000
 
# Contribute
Please check the [**Contributing Guidelines**](https://github.com/SandeepBalachandran/Pytract/blob/master/CONTRIBUTING.md) before contributing.

