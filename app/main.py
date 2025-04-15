def copy_file(command: str) -> None:
    command = command.strip()
    if not command:
        return

    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_filename = parts[1]
    destination_filename = parts[2]

    if source_filename == destination_filename:
        return

    try:
        with open(source_filename, "r") as source_file, open(destination_filename, "w") as destination_file:
            destination_file.write(source_file.read())
    except FileNotFoundError:
        return
