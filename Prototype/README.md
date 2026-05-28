# Prototype

⚠️ **Project Status: ONGOING** 🚧

This is the prototype phase of the Society_MCE project. The project is actively under development and subject to changes.

## Overview

This prototype contains experimental implementations and proof-of-concept code for document processing and analysis, including:

- **OCR Engine** - Optical Character Recognition implementation
- **LLM Parser** - Large Language Model-based text parsing
- **Table Structure Detector** - Detection and analysis of table structures in documents
- **OCR Structure Analyzer** - Analysis of document structure using OCR
- **Pipeline** - Integration pipeline combining all modules

## Core Approach

🎯 **Text-Based Processing**

The system is designed to work for **most document types** by focusing on **text content extraction and processing**. The code operates primarily on:

- **Text extraction** from documents
- **Text analysis and parsing** using LLM models
- **Content structure understanding** based on text patterns

### Table Handling

📊 **Format-Agnostic Table Processing**

The code handles tables **regardless of their visual structure**:

- ✅ Tables **with lines/borders** are processed
- ✅ Tables **without lines** (space-separated, tab-separated) are processed
- ✅ **Visual formatting does NOT affect** the text extraction and parsing logic

The system focuses on **extracting and understanding the text content** within tables rather than relying on visual table structure detection. This makes it robust to different table formatting styles and layouts.

## Components

- `OCREngine.py` / `OCREngine.ipynb` - OCR processing module
- `LLMParser.py` / `LLMParser.ipynb` - LLM-based parsing module
- `TableStructureDetector.py` / `TableStructureDetector.ipynb` - Table detection module
- `OCRStructureAnalyzer.py` / `OCRStructureAnalyzer.ipynb` - Document structure analysis
- `Pipline.ipynb` / `Pipline_temp.ipynb` - Pipeline notebooks for testing
- `paddle_ocr.ipynb` - PaddleOCR implementation experiments
- `TempPiplineMain.ipynb` - Main pipeline notebook (work in progress)

## Status

✋ This prototype is **actively being developed**. Code, structure, and implementations may change frequently.

## Note

For the latest updates and project structure, refer to the main repository documentation.
