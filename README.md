# 🔐 File Integrity Checker

A simple Python command-line tool for detecting changes to files using **SHA-256 hashes**.

The program creates a baseline of files in a directory and can later check that directory for files that have been **modified, deleted, or added**.

This project was created as a way to learn more about Python, file handling, hashing, and basic cybersecurity concepts.

## ✨ Features

- 📁 Recursively scans directories
- 🔐 Generates SHA-256 hashes for files
- 💾 Stores hashes in a JSON baseline
- ✅ Detects unchanged files
- ⚠️ Detects modified files
- 🗑️ Detects deleted files
- 🆕 Detects newly added files
- 🖥️ Simple interactive CLI

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/DenzelVW-xyz/File-Integrity-Checker.git
cd File-Integrity-Checker
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 📖 Usage

Start the program:

```bash
python checker.py
```

Choose either:

```text
Scan
Check
```

### Scan

`Scan` recursively scans the selected directory and calculates the SHA-256 hash of each file.

```text
You selected: Scan
Directory to scan: /home/user/test
```

The hashes are stored in `baseline.json`.

### Check

Select `Check` and provide the directory you previously scanned:

```text
You selected: Check
Directory to check: /home/user/test
```

Example output:

```text
/home/user/test/1.txt : OK
/home/user/test/2.txt : Changed
/home/user/test/3.txt : Deleted!
/home/user/test/5.txt : NEW!
```

## 🔎 How It Works

During a scan:

```text
Directory
   │
   ▼
Find Files
   │
   ▼
Read File Contents
   │
   ▼
SHA-256 Hash
   │
   ▼
baseline.json
```

During a check, the current SHA-256 hashes are compared with the hashes stored in the baseline.

- `OK` — File exists and its contents have not changed.
- `Changed` — File exists, but its contents have changed.
- `Deleted` — File existed in the baseline but no longer exists.
- `NEW` — File exists now but was not present in the baseline.

## 📂 Project Structure

```text
File-Integrity-Checker/
├── checker.py
├── requirements.txt
├── README.md
├── .gitignore
└── baseline.json
```

## 🛠️ Built With

- Python
- `hashlib`
- `os`
- `json`
- `select-options`

## ⚠️ Disclaimer

This project is primarily intended for learning and experimentation. It should not be treated as a replacement for professional file-integrity monitoring or security software.
