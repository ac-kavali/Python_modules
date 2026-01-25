import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

# Read Entry Using "input()"
ar_ID = input("Input Stream active. Enter archivist ID: ")
print("Input Stream active. Enter status report: ", end="")

# Read Entry Using "sys.stdin"
status_rep = sys.stdin.readline()

# Print Out using sys.stdout Entry
sys.stdout.write(f'\n[STANDARD] Archive status from: '
                 f'{ar_ID}: {status_rep}\n')

# Print and test Diagnostic (Error) channel
sys.stderr.write('[ALERT System diagnostic: '
                 'Communication channels verified\n')

print("{{]}}STANDARD {{]}} Data transmission complete\n")
print("Three-channel communication test successful.")
