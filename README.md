# Defectly - Bug Tracking System

![image](https://github.com/Osigelialex/Defectly/assets/97721950/2de3fb5d-b308-4cd0-b3de-af405cfbf5f2)

## Overview

Defectly is a web-based application designed to help teams efficiently manage and track software bugs and issues. It provides a centralized platform for bug reporting, assignment, tracking, and resolution.

### Features

- User authentication and authorization.
- Bug/issue creation with detailed information.
- Categorization of bugs by severity, status.
- Assignment of bugs to specific team members.
- Commenting and discussion on bug reports.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Getting Started

Provide instructions on how to get a copy of the project up and running on a local development environment.

### Prerequisites

Python.

### Installation

Step-by-step instructions for installing and setting up the project.

```bash
git clone https://github.com/Osigelialex/Defectly.git
cd Defectly
pip install -r requirements.txt
```

### Usage
```bash
python manage.py migrate
python manage.py runserver
```
Access the application in your web browser at http://localhost:8000

### Admin priviledges
```bash
python manage.py createsuperuser
```
login in with created admin account to get admin features
