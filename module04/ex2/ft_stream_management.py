import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
ar_ID = input("Input Stream active. Enter archivist ID: ")
print("Input Stream active. Enter status report: ", end="")
status_rep = sys.stdin.readline()

sys.stdout.write(f'\n{{]}}STANDARD{{]}} Archive status from: '
                 f'{ar_ID}: {status_rep}\n')
word = "{[}ALERT{]}"
sys.stderr.write(f'{word} System diagnostic: '
                 f'Communication channels verified\n')

print("{{]}}STANDARD {{]}} Data transmission complete\n")
print("Three-channel communication test successful.")
