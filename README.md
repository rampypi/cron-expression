# Cron Expression Parser

A robust cron expression parser that breaks down cron strings into their time components and displays when they will run.

## Features

- Parses standard cron expressions with 5 time fields
- Handles various patterns:
  - Lists (1,2,3)
  - Ranges (1-5)
  - Steps (*/15)
  - Range with steps (1-15/3)
- Clean, formatted output
- Comprehensive test suite

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ramapypi/cron-parser.git
cd cron-parser
```

2. Create and activate virtual environment:

```bash
python -m venv .cron_parser_venv
source .cron_parser_venv/bin/activate  # Unix/macOS
# or
.cron_parser_venv\Scripts\activate  # Windows
```

3. Install requirements:

```bash
pip install pytest
```

## Usage

Run the parser with a cron expression:

```bash
python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```

Example output:

```bash
minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find
```

## Cron Expression Format

┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday)
│ │ │ │ │
│ │ │ │ │
* * * * * command


## Running Tests

```bash
pytest tests/test_cron_parser.py -v
```
