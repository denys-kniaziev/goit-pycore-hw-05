import sys
import re
from typing import Dict, List, Optional
from collections import defaultdict


def parse_log_line(line: str) -> Optional[Dict[str, str]]:
    """
    Parse a single log line and extract components.
    
    Args:
        line (str): A single line from the log file
        
    Returns:
        Optional[Dict[str, str]]: Dictionary with parsed components (date, time, level, message)
        Returns None if line format is invalid
    """
    # Regular expression pattern to match log format: YYYY-MM-DD HH:MM:SS LEVEL Message
    pattern = r'^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)$'
    
    match = re.match(pattern, line.strip())
    if match:
        date, time, level, message = match.groups()
        return {
            'date': date,
            'time': time,
            'level': level,
            'message': message
        }
    return None


def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Load and parse logs from a file.
    
    Args:
        file_path (str): Path to the log file
        
    Returns:
        List[Dict[str, str]]: List of parsed log entries
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    logs = []
    
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if line.strip():  # Skip empty lines
                    parsed_line = parse_log_line(line)
                    if parsed_line:
                        logs.append(parsed_line)
                    else:
                        print(f"Warning: Could not parse line {line_number}: {line.strip()}")
        
        return logs
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Log file not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading log file: {e}")


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Filter logs by specified level.
    
    Args:
        logs (List[Dict[str, str]]): List of parsed log entries
        level (str): Log level to filter by (case insensitive)
        
    Returns:
        List[Dict[str, str]]: Filtered list of log entries
    """
    # Using functional programming - filter with lambda
    return list(filter(lambda log: log['level'].upper() == level.upper(), logs))


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Count the number of log entries for each level.
    
    Args:
        logs (List[Dict[str, str]]): List of parsed log entries
        
    Returns:
        Dict[str, int]: Dictionary with log levels as keys and counts as values
    """
    # Using functional programming - defaultdict and list comprehension
    counts = defaultdict(int)
    
    # Count occurrences using list comprehension and functional approach
    levels = [log['level'] for log in logs]
    for level in levels:
        counts[level] += 1
    
    return dict(counts)


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Display log counts in a formatted table.
    
    Args:
        counts (Dict[str, int]): Dictionary with log levels and their counts
    """
    if not counts:
        print("No log entries found.")
        return
    
    print("Log Level        | Count")
    print("-----------------|-------")
    
    # Sort by log level for consistent output
    for level in sorted(counts.keys()):
        print(f"{level:<15} | {counts[level]}")


def display_log_details(logs: List[Dict[str, str]], level: str) -> None:
    """
    Display detailed log entries for a specific level.
    
    Args:
        logs (List[Dict[str, str]]): List of log entries for the specified level
        level (str): The log level being displayed
    """
    if not logs:
        print(f"No log entries found for level '{level.upper()}'.")
        return
    
    print(f"\nLog details for level '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    """
    Main function to handle command line arguments and execute log analysis.
    """
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_logfile> [log_level]")
        print("Example: python main.py sample.log")
        print("Example: python main.py sample.log error")
        sys.exit(1)
    
    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        # Load and parse logs
        print(f"Loading logs from: {file_path}")
        logs = load_logs(file_path)
        
        if not logs:
            print("No valid log entries found in the file.")
            return
        
        # Count logs by level
        counts = count_logs_by_level(logs)
        
        # Display general statistics
        display_log_counts(counts)
        
        # If specific level is requested, show detailed entries
        if filter_level:
            filtered_logs = filter_logs_by_level(logs, filter_level)
            display_log_details(filtered_logs, filter_level)
            
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
