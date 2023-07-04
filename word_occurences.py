import re

def find_word_occurrences():
    pattern = r'\b(heritable|inherit|inheritance)\b'
    with open('origin.txt', 'r') as file:
        lines = file.readlines()

    occurrences = []
    for line_num, line in enumerate(lines, start=1):
        matches = re.findall(pattern, line, flags=re.IGNORECASE)
        for match in matches:
            occurrences.append(f"{line_num}\t{match}")

    with open('occurrences.txt', 'w') as file:
        file.write('\n'.join(occurrences))

if __name__ == '__main__':
    find_word_occurrences()
