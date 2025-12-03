import os
import inspect

def read_input(use_test_file=False, separator=None, cast_to=None):
    """
    Liest input.txt oder test.txt ein.
    
    Args:
        use_test_file (bool): Wenn True, wird test.txt gelesen, sonst input.txt.
        separator (str, optional): Das Trennzeichen für Einträge in einer Zeile.
        cast_to (type, optional): Ein Typ (z.B. int), in den alle Einträge umgewandelt werden sollen.
        
    Returns:
        list: Ein 1D oder 2D Array, abhängig vom Dateiinhalt und Separator.
    """
    
    # --- FIX: Robuste Pfad-Ermittlung ---
    # Wir schauen direkt in den Call-Stack, wer diese Funktion aufgerufen hat.
    # stack()[1] ist der Aufrufer (solution.py).
    # .filename gibt uns den absoluten Pfad zur Datei, auch bei dynamischem Import.
    caller_frame = inspect.stack()[1]
    caller_filename = caller_frame.filename
    base_path = os.path.dirname(os.path.abspath(caller_filename))
    # ------------------------------------
    
    filename = "test.txt" if use_test_file else "input.txt"
    file_path = os.path.join(base_path, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
    except FileNotFoundError:
        print(f"[ERROR] Datei nicht gefunden: {file_path}")
        return []

    lines = content.splitlines()

    # Logik für die Rückgabeformate
    data = []

    # Fall 1: Eine lange Zeile mit Separator -> 1D Array
    if len(lines) == 1 and separator:
        data = lines[0].split(separator)
    
    # Fall 2: Mehrere Zeilen mit Separator -> 2D Array
    elif len(lines) > 1 and separator:
        data = [line.split(separator) for line in lines]
        
    # Fall 3: Mehrere Zeilen, EIN Entry pro Zeile (kein Separator angegeben) -> 1D Array
    else:
        data = lines

    # Optional: Typumwandlung (z.B. alles zu Integer)
    if cast_to:
        if data and isinstance(data[0], list): # 2D Fall
            data = [[cast_to(item) for item in row] for row in data]
        elif data: # 1D Fall
            data = [cast_to(item) for item in data]

    return data