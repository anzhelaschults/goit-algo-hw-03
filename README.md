
# goit-algo-hw-03

Homework 3 - Algorithms and Recursion

## Description

This repository contains solutions for assignment 3.

## Files

- `task1.py` - Script that copies files and organizes them by extension
- `task2.py` - Koch Snowflake fractal visualization

## Task 1: File Sorting

This script copies files from one folder to another and sorts them by file type.

**How to run:**
```bash
python task1.py test_folder dist
```

The first argument is the source folder, the second is the destination folder (default is `dist`).

## Task 2: Koch Snowflake

This program draws a Koch Snowflake fractal. 

**How to run:**
```bash
python task2.py
```

Enter the recursion level when asked (try 0-4).

## Testing

## Testing

To test Task 1, create a test folder with different file types:  

```bash
mkdir -p test_folder/subfolder1/subfolder2
echo "Hello World" > test_folder/file1.txt
echo "Another text file" > test_folder/file2.txt
echo "print('Hello')" > test_folder/script.py
echo "body { margin:  0; }" > test_folder/style.css
echo '{"name": "test"}' > test_folder/subfolder1/data.json
echo "# README" > test_folder/subfolder1/subfolder2/readme. md
```

Then run:
```bash
python task1.py test_folder
```

## Author

Anzhela Schults