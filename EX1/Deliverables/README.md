# Document Generator - Python & Docker Automation

## Overview

This project implements an automated document generation system that creates personalized Word documents from YAML configuration files and Word templates using Python and Docker. The solution processes band information from a YAML file and generates individual documents for each band using a predefined template.

## Features

- **YAML Configuration Processing**: Reads structured data from YAML files
- **Word Document Generation**: Creates personalized .docx files using mail merge functionality
- **Docker Containerization**: Runs in isolated container environment with non-root user
- **Command-line Interface**: Flexible CLI with multiple options
- **Debug Mode**: Verbose logging for troubleshooting
- **Batch Processing**: Handles multiple entries automatically

## Technical Stack

- **Language**: Python 3
- **Container**: Docker (Alpine Linux base)
- **Dependencies**: 
  - `pyyaml` - YAML file processing
  - `mailmerge` - Word document generation
  - `argparse` - Command-line argument parsing

## Project Structure

```
├── main.py              # Main Python script
├── Dockerfile           # Container configuration
├── requirements.txt     # Python dependencies
├── inputs/
│   ├── config.yaml      # YAML configuration file
│   └── template.docx    # Word template file
└── output/              # Generated documents directory
```

## How It Works

### Configuration Processing
The script reads a YAML file containing band information with the following structure:

bands:
  - name: "Band Name"
    initials: "BN"
    genre: "Rock"
    members: "Member list"
    about: "Band description"
    musics:
      - name: "Song 1"
        album: "Album 1"
      - name: "Song 2" 
        album: "Album 2"


### Document Generation
For each band entry, the script:
1. Extracts band information and up to 3 songs
2. Maps data to template placeholders
3. Generates a personalized Word document
4. Saves the file with the band name

## Usage

### Building the Docker Image

```
docker build -t ex1 .
```


### Running the Container

```
docker run --rm -v ${PWD}/:/app/ ex1 -c <path of config file> -t <path of template file> -o output
```

### Command-line Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `-c, --config` | YAML configuration file | ✅ |
| `-t, --template` | Word template file | ✅ |
| `-o, --output` | Output directory | ❌ (default: current directory) |
| `-d, --debug` | Enable debug mode | ❌ |

## Error Handling

The application includes comprehensive error handling for:

- Missing configuration files
- Invalid YAML syntax
- Template processing errors
- File I/O operations
- Missing required data fields

## Output

The script provides:
- Progress logging (with debug mode)
- Success/failure status for each document
- Final summary with generation statistics