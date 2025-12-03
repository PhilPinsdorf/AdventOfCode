import os
import sys
import argparse
import time
import importlib.util
import requests  # pip install requests

# --- KONFIGURATION ---
# Bitte hier deine E-Mail oder Repo-URL eintragen (wird von AoC gefordert)
USER_AGENT = "github.com/philpinsdorf/AdventOfCode by philemon.pinsdorf@live.de"

# --- HELPER: FORMATIERUNG ---
def print_result(part, result, duration):
    """Gibt das Ergebnis hübsch formatiert aus."""
    print(f"┌{'─'*45}┐")
    print(f"│ Part {part} {' '*(37 - len(str(part)))} │")
    print(f"├{'─'*45}┤")
    
    res_str = str(result)
    # Wenn das Ergebnis sehr lang ist (z.B. OCR Text), kürzen wir die Vorschau in der Box
    if len(res_str) > 41:
        print(f"│ Ergebnis: (siehe unten){' '*22}│")
    else:
        print(f"│ Ergebnis: {res_str}{' '*(33 - len(res_str))} │")
        
    time_str = f"{duration:.4f} ms"
    print(f"│ Zeit:     {time_str}{' '*(33 - len(time_str))} │")
    print(f"└{'─'*45}┘")
    
    # Bei langen Ergebnissen wird es hier nochmal komplett ausgegeben
    if len(res_str) > 41:
        print(f"\nLanges Ergebnis Part {part}:\n{res_str}\n")
    print() # Leerzeile für Abstand

# --- HELPER: DOWNLOAD ---
def download_input(year, day, file_path):
    """Lädt den Input von adventofcode.com herunter."""
    session_cookie = ""
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    
    # 1. Versuche Session aus .env zu lesen
    try:
        with open(env_path, "r") as f:
            for line in f:
                if line.strip().startswith("AOC_SESSION="):
                    session_cookie = line.strip().split("=", 1)[1]
                    break
    except FileNotFoundError:
        print("[WARN] Keine .env Datei gefunden. Download wird übersprungen.")
        return

    if not session_cookie:
        print("[WARN] AOC_SESSION in .env nicht gefunden. Download übersprungen.")
        return

    print(f"--- Lade Input für {year} Tag {day} herunter... ---")
    
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "Cookie": f"session={session_cookie}",
        "User-Agent": USER_AGENT
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(response.text.rstrip())
            print("[OK] Input erfolgreich heruntergeladen.")
        elif response.status_code == 404:
            print("[ERROR] Tag noch nicht verfügbar (404).")
        else:
            print(f"[ERROR] Download fehlgeschlagen: Status {response.status_code}")
            print("Prüfe, ob der Session-Cookie in der .env Datei aktuell ist.")
    except Exception as e:
        print(f"[ERROR] Verbindungsfehler: {e}")

# --- COMMAND: CREATE ---
def create_day(year, day):
    day_str = str(day).zfill(2)
    base_folder = str(year)
    day_folder = os.path.join(base_folder, f"day_{day_str}")
    
    os.makedirs(day_folder, exist_ok=True)
    
    template_content = f"""
from aoc_utils import read_input

data = read_input(use_test_file=True)

def solve_1():
    solution = 0
    return solution

def solve_2():
    solution = 0
    return solution

"""

    files = {
        "input.txt": None, # Spezialbehandlung
        "test.txt": "",
        "solution.py": template_content
    }
    
    for filename, content in files.items():
        path = os.path.join(day_folder, filename)
        
        if not os.path.exists(path):
            if filename == "input.txt":
                # Versuche Download
                download_input(year, day, path)
                # Falls Download fehlschlug und Datei fehlt -> leer anlegen
                if not os.path.exists(path):
                    with open(path, 'w', encoding='utf-8') as f: f.write("")
            else:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content.strip())
            print(f"[OK] Erstellt: {path}")
        else:
            print(f"[INFO] Existiert bereits: {path}")

# --- COMMAND: RUN ---
def run_day(year, day):
    day_str = str(day).zfill(2)
    script_path = os.path.join(str(year), f"day_{day_str}", "solution.py")
    
    if not os.path.exists(script_path):
        print(f"[ERROR] Datei nicht gefunden: {script_path}")
        return

    print(f"\n🎄 === Advent of Code {year} - Day {day} === 🎄\n")

    # --- NEU: Root-Verzeichnis zum Pfad hinzufügen ---
    # Damit 'import aoc_utils' in der solution.py funktioniert,
    # ohne dass dort sys.path Hacks stehen müssen.
    root_dir = os.getcwd() 
    if root_dir not in sys.path:
        sys.path.append(root_dir)
    # -------------------------------------------------

    # Modul dynamisch laden (Rest bleibt gleich)
    spec = importlib.util.spec_from_file_location("solution_module", script_path)
    module = importlib.util.module_from_spec(spec)
    sys.path.append(os.path.dirname(script_path)) # Für relative imports
    
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"[ERROR] Fehler beim Laden der Datei: {e}")
        return

    # Parts ausführen
    for part in [1, 2]:
        func_name = f"solve_{part}"
        if hasattr(module, func_name):
            func = getattr(module, func_name)
            
            start_time = time.perf_counter()
            try:
                result = func()
            except Exception as e:
                result = f"Error: {e}"
            end_time = time.perf_counter()
            
            duration_ms = (end_time - start_time) * 1000
            print_result(part, result, duration_ms)
        else:
            print(f"[INFO] Funktion {func_name} nicht gefunden.")

# --- MAIN ---
def main():
    parser = argparse.ArgumentParser(description="AoC Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Parser für 'create'
    parser_create = subparsers.add_parser("create", help="Erstellt Struktur & lädt Input")
    parser_create.add_argument("year", type=int)
    parser_create.add_argument("day", type=int)

    # Parser für 'run'
    parser_run = subparsers.add_parser("run", help="Führt Lösung aus & misst Zeit")
    parser_run.add_argument("year", type=int)
    parser_run.add_argument("day", type=int)

    args = parser.parse_args()

    if args.command == "create":
        create_day(args.year, args.day)
    elif args.command == "run":
        run_day(args.year, args.day)

if __name__ == "__main__":
    main()