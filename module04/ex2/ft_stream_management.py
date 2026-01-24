import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
ar_ID = input("Input Stream active. Enter archivist ID: ")
print("Input Stream active. Enter status report:", end = "")
status_rep = sys.stdin.readline()

sys.stdout.write(f'{{]}}STANDARD {{]}} Archive status from: {ar_ID}: {status_rep}\n')
sys.stderr.write(f'{{[}}ALERT{{]}} System diagnostic: Communication channels verified\n')