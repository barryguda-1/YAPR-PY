##Yet another /proc parser
import os

def parse_proc_directory():
    process_info = []
    
    # Get the list of all entries in the /proc directory
    entries = os.listdir('/proc')
    
    for entry in entries:
        if entry.isdigit():
            try:
                # Read the process status file
                with open(f'/proc/{entry}/status', 'r') as file:
                    lines = file.readlines()
                    
                    # Extract the process ID and process name
                    pid = int(lines[5].split()[1])
                    process_name = lines[0].split(':')[1].strip()
                    
                    # Add the process information to the list
                    process_info.append({'pid': pid, 'name': process_name})
            except (FileNotFoundError, IndexError, ValueError):
                pass
    
    return process_info

# Example usage
processes = parse_proc_directory()

# Print the process information
for process in processes:
    print(f"PID: {process['pid']}, Name: {process['name']}")
