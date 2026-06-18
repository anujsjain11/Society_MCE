# Society_MCE

![Project Status](https://img.shields.io/badge/status-In%20Development-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)

A comprehensive document processing and analysis platform using Optical Character Recognition (OCR) and Large Language Models (LLM) for intelligent text extraction and structure understanding.

## 📋 Table of Contents

- [Overview](#overview)
- [Prototype Documentation](#prototype-documentation)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Overview

Society_MCE is designed to process various document types and extract meaningful information through a pipeline that combines OCR technology with LLM-based parsing. The system is built to handle multiple document formats with a focus on robustness and accuracy.

## Prototype Documentation

### 🎯 Project Goal

The prototype phase aims to establish a **text-based processing pipeline** that can effectively handle various document types by extracting and analyzing text content intelligently.

### Core Philosophy

- **Format-Agnostic Processing**: The system is designed to work with most document types
- **Text-Centric Approach**: Focus on content extraction rather than visual structure
- **Flexible Table Handling**: Process tables regardless of visual formatting (with or without borders)
- **LLM-Powered Analysis**: Use advanced language models for intelligent parsing and understanding

### Key Capabilities

#### 1. **OCR Engine**
- Extracts text from image-based documents
- Supports multiple document formats
- High-accuracy text recognition
- **File**: `OCREngine.py` / `OCREngine.ipynb`

#### 2. **LLM Parser**
- Analyzes extracted text using language models
- Extracts structured information from unstructured text
- Intelligent content classification and extraction
- **File**: `LLMParser.py` / `LLMParser.ipynb`

#### 3. **Table Structure Detector**
- Identifies and analyzes tables in documents
- Extracts table content and structure
- Works with formatted and unformatted tables
- **File**: `TableStructureDetector.py` / `TableStructureDetector.ipynb`

#### 4. **OCR Structure Analyzer**
- Analyzes overall document structure
- Identifies sections, headings, and content blocks
- Maps document layout and organization
- **File**: `OCRStructureAnalyzer.py` / `OCRStructureAnalyzer.ipynb`

#### 5. **Processing Pipeline**
- Integrates all components into a unified workflow
- Manages data flow between modules
- Handles error management and logging
- **File**: `Pipline.ipynb` / `TempPiplineMain.ipynb`

### Table Processing Strategy

The prototype handles tables through a **content-focused approach**:

| Feature | Status | Details |
|---------|--------|---------|
| Bordered Tables | ✅ Supported | Tables with visual borders/lines |
| Borderless Tables | ✅ Supported | Space/tab-separated content |
| Format Independence | ✅ Supported | Visual formatting doesn't affect parsing |
| Text Extraction | ✅ Optimized | Focus on content understanding |
| Structure Recovery | ✅ Implemented | Reconstructs table relationships from text |

### Technical Stack

- **OCR Technology**: PaddleOCR
- **Language Models**: OpenAI / Hugging Face models
- **Processing**: Python 3.8+
- **Notebooks**: Jupyter for experimentation and testing
- **Data Processing**: Pandas, NumPy

## Features

- ✅ Multi-format document support
- ✅ Text extraction with OCR
- ✅ Intelligent content parsing with LLM
- ✅ Table detection and extraction
- ✅ Document structure analysis
- ✅ Flexible, modular architecture
- ✅ Notebook-based development and testing

## Architecture

```
Documents (PDF, Images, Scans)
    ↓
[OCR Engine]
    ↓
Raw Text Extraction
    ↓
[Structure Analyzer]
    ↓
Document Structure Identification
    ↓
[Table Detector]
    ↓
Table Content Extraction
    ↓
[LLM Parser]
    ↓
Structured Data Output
```

## Installation

### Prerequisites
- Python 3.8 or higher
- Pip or conda package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/anujsjain11/Society_MCE.git
cd Society_MCE

# Install dependencies
pip install -r requirements.txt

# Optional: For development with Jupyter notebooks
pip install jupyter notebook
```

## Usage

### Running the Full Pipeline

```python
# Using the pipeline notebook
jupyter notebook Prototype/TempPiplineMain.ipynb
```

### Individual Components

```python
# OCR Engine
from Prototype.OCREngine import OCREngine
ocr = OCREngine()
text = ocr.extract_text('document.pdf')

# LLM Parser
from Prototype.LLMParser import LLMParser
parser = LLMParser()
parsed_data = parser.parse(text)

# Table Structure Detector
from Prototype.TableStructureDetector import TableStructureDetector
detector = TableStructureDetector()
tables = detector.detect_tables(text)
```

## Project Structure

```
Society_MCE/
├── README.md                           # Main documentation
├── requirements.txt                    # Python dependencies
├── Prototype/
│   ├── README.md                      # Prototype-specific documentation
│   ├── OCREngine.py                   # OCR implementation
│   ├── OCREngine.ipynb               # OCR notebook
│   ├── LLMParser.py                  # LLM parser implementation
│   ├── LLMParser.ipynb               # LLM parser notebook
│   ├── TableStructureDetector.py     # Table detection implementation
│   ├── TableStructureDetector.ipynb  # Table detection notebook
│   ├── OCRStructureAnalyzer.py       # Structure analyzer implementation
│   ├── OCRStructureAnalyzer.ipynb    # Structure analyzer notebook
│   ├── Pipline.ipynb                 # Main pipeline notebook
│   ├── Pipline_temp.ipynb            # Temporary pipeline experiments
│   ├── TempPiplineMain.ipynb         # Current main pipeline
│   ├── paddle_ocr.ipynb              # PaddleOCR experiments
│   └── data/                         # Sample data and test files
├── docs/                             # Additional documentation
└── tests/                            # Test files
```

## Current Status

⚠️ **Project Status**: ONGOING 🚧

This is an **active development** project. The following are in progress:

- Core pipeline optimization
- Performance benchmarking
- Extended document format support
- Enhanced LLM model integration
- Comprehensive testing suite

## Development Workflow

### Adding New Features

1. Create a feature branch
2. Develop in the appropriate component file or notebook
3. Test thoroughly using provided test data
4. Submit for review

### Running Experiments

Use Jupyter notebooks in the `Prototype/` directory for experimentation:
- Isolated testing of components
- Rapid prototyping
- Result visualization
- Documentation of findings

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages
6. Push to your branch
7. Create a Pull Request

## Future Roadmap

- [ ] Production deployment pipeline
- [ ] API service development
- [ ] Extended model support
- [ ] Performance optimization
- [ ] Comprehensive test coverage
- [ ] Documentation improvements
- [ ] Community feedback integration

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Contact & Support

For questions, issues, or suggestions, please open an issue on the [GitHub repository](https://github.com/anujsjain11/Society_MCE).

---

**Last Updated**: May 28, 2026
**Maintainer**: Anuj Jain (@anujsjain11)
