pfad1 : str = "./porn.txt"
pfad2 : str = "./other.txt"

def compare_files_and_write_diff(file1_path, file2_path):
    try:
        file1_lines : set[str] = set()
        with open(file1_path, 'r') as file1:
            file1_lines.update(file1)

        with open(file2_path, 'r') as file2:
            for line in file2:
                if line.startswith("||") and line not in file1_lines:
                    file1_lines.add(line)  

        sorted_lines : set[str] = sorted(file1_lines)

        with open(file1_path, 'w') as output_file:
            output_file.writelines(sorted_lines)

        print(f"Unterschiedliche Zeilen wurden in '{file1_path}' geschrieben.")

    except FileNotFoundError as e:
        print(f"Fehler: Datei nicht gefunden - {e.filename}")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def main():
    compare_files_and_write_diff(pfad1, pfad2)

if __name__ == '__main__':
    main()