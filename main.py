#!/usr/bin/env python3
import sys
from src.cron import CronExpression

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py \"<cron expression>\"")
        sys.exit(1)

    try:
        parts = sys.argv[1].split()
        expression = CronExpression(
            minute=parts[0],
            hour=parts[1],
            day_of_month=parts[2],
            month=parts[3],
            day_of_week=parts[4],
            command=' '.join(parts[5:])
        )
        print(expression.format_output())
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
