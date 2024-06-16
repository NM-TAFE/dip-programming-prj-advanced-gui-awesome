[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/SCA-edx6)

<div align="center">

# OcrRoo

## v1 - Drafted by Rafael Avigad/James Makela

---

[Badges here]

**AI Powered OCR Code Recognition from Video Tutorials**

[![Build](https://github.com/NM-TAFE/project-advanced-ui-development-team-mental-capacity/actions/workflows/build.yml/badge.svg)](https://github.com/NM-TAFE/project-advanced-ui-development-team-mental-capacity/actions/workflows/build.yml)
[![Tests](https://github.com/NM-TAFE/project-advanced-ui-development-team-mental-capacity/actions/workflows/tests.yml/badge.svg)](https://github.com/NM-TAFE/project-advanced-ui-development-team-mental-capacity/actions/workflows/tests.yml)
[![Accessibility](https://github.com/NM-TAFE/project-advanced-ui-development-team-mental-capacity/actions/workflows/accesibility.yml/badge.svg)](https://github.com/NM-TAFE/project-advanced-ui-development-team-mental-capacity/actions/workflows/accesibility.yml)

</div>

## About

A video player designed to assist visually impaired developers who want to learn to code.
The program reads code from videos to assist visually impaired developers in using these resources.

## Features - (need more info)

---

[Demo Video here]

- Ability to upload, or enter a video link.
- OcrRoo picks out any code text from the provided video, and reads that text to the user.

## Installation

To install and run this project, please follow the [Installation Guide](https://github.com/NM-TAFE/dip-programming-prj-advanced-gui-awesome/wiki/Installation-Guide)
in the [Wiki](https://github.com/NM-TAFE/dip-programming-prj-advanced-gui-awesome/wiki).

#### Basic Installation

1. Navigate to the projects root folder

2. Create a virtual environment

```bash
python -m venv ./venv
```

3. Activate the virtual environment
   Windows:

```bash
./venv/Scripts/activate
```

Mac/Linux

```bash
source venv/bin/activate
```

4. Install dependencies with pip

```bash
pip install -r requirements.txt
```

5. Navigate to App Directory

Change into app directory.

```bash
cd app/

```

6. Run the Application

To run the application with silenced debug/logging output, execute the following command. Debug and logging outputs will be saved to an `app.log` file

```bash
python app.py

```

7. Install Tesseract OCR
- https://github.com/UB-Mannheim/tesseract/wiki
- Once the .exe is downloaded open it and go through the installation steps.
- When you run the program, there is an automated Tesseract executable search in the Settings.
Feel free to do the search to save a lot of trouble.

To run the application with debug/logging output in the console, use the following command.This is recommended for development as it automatically reloads the app when changes are detected.

```bash
flask run --debug

```

#### Configuration Variables

To use the project, add the following configuration variables to your `config.ini` file:

- `openai_api_key`: API key for OpenAI
- `tesseract_executable`: Path to Tesseract OCR executable
- `ide_executable`: Path to preferred IDE executable

In the current version of the project, this manual configuration is necessary.However, future builds will allow you to perform this configuration from the user interface (UI). 


## Contributing

To contribute to this project, please follow the [Contribution Guide](https://github.com/NM-TAFE/dip-programming-prj-advanced-gui-awesome/wiki/Contribution-Guide)
in the [Wiki](https://github.com/NM-TAFE/dip-programming-prj-advanced-gui-awesome/wiki).

## Code of Conduct

---

- To view the code of conduct, please visit the [Code of Conduct] page in the [Wiki](https://github.com/NM-TAFE/dip-programming-prj-advanced-gui-awesome/wiki).

## License

This project is licensed under the [Creative Commons Zero v1.0 Universal](LICENSE) license.

## Credits

This code was first created by the 2023, S2 Advanced Programming Diploma Group at North Metro TAFE. If you would like your contribution acknowledged, please contact Rafael.
