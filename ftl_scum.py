#!/usr/bin/env python3
"""
FTL Scum - A command-line save-scumming utility for FTL: Faster Than Light.
"""

import os
import re
import shutil
import struct
import subprocess
import sys
from datetime import datetime
from typing import Any

SRC: str = os.path.expanduser("~/.local/share/FasterThanLight/continue.sav")
DEFAULT_dest_dir: str = os.path.expanduser("~/Documents/ftl_scum_saves")
CONFIG_FILE: str = os.path.expanduser("~/.config/ftl_save_scum.conf")
dest_dir: str = ""


def input_with_prefill(prompt: str, text: str) -> str:
    """Prompts the user for input with a prefilled value."""
    try:
        import readline
        def hook() -> None:
            readline.insert_text(text)
            readline.redisplay()

        readline.set_startup_hook(hook)
        try:
            return input(prompt)
        finally:
            readline.set_startup_hook(None)
    except ImportError:
        print(f"(Default: {text})")
        val = input(prompt)
        return val if val else text


def check_deps() -> None:
    """Checks for required external dependencies."""
    if not shutil.which("fzf"):
        print("Error: missing required dependency: fzf", file=sys.stderr)
        print("Install with: sudo apt-get install fzf", file=sys.stderr)
        sys.exit(1)


def resolve_dest_dir() -> None:
    """Resolves and creates the destination directory for backups."""
    global dest_dir
    configured: str = ""
    if os.path.isfile(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        configured = os.path.expanduser(line)
                        break
        except OSError:
            pass

    if configured:
        try:
            os.makedirs(configured, exist_ok=True)
            dest_dir = configured
            return
        except OSError:
            pass

    entered: str = input_with_prefill("Save snapshots to directory: ", DEFAULT_dest_dir)
    entered = os.path.expanduser(entered.strip() or DEFAULT_dest_dir)

    try:
        os.makedirs(entered, exist_ok=True)
    except OSError as e:
        print(
            f"Error: cannot create or access directory: {entered}\n{e}", file=sys.stderr
        )
        sys.exit(1)

    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write(entered + "\n")
    dest_dir = entered


def show_meta(base: str) -> None:
    """Prints the metadata for a given save file base name."""
    print(f"File: {base}\n")
    meta_path: str = os.path.join(dest_dir, base) + ".meta"
    if os.path.isfile(meta_path):
        with open(meta_path, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("(no description)")


def last_description() -> str:
    """Gets the user description from the most recent save file."""
    if not os.path.isdir(dest_dir):
        return ""

    saves: list[tuple[float, str]] = []
    for fname in os.listdir(dest_dir):
        if fname.endswith(".sav"):
            full_path = os.path.join(dest_dir, fname)
            saves.append((os.path.getmtime(full_path), fname))

    if not saves:
        return ""

    saves.sort(reverse=True, key=lambda x: x[0])
    latest: str = saves[0][1]
    meta_path: str = os.path.join(dest_dir, latest + ".meta")

    if not os.path.isfile(meta_path):
        return ""

    desc: str = ""
    with open(meta_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("Description: "):
                desc = line[len("Description: ") :].strip()
                break
    return desc


def get_int(f: Any) -> int:
    """Reads a 4-byte little-endian integer from a file stream."""
    b: bytes = f.read(4)
    if not b or len(b) < 4:
        return 0
    return struct.unpack("<i", b)[0]


def get_bool(f: Any) -> bool:
    """Reads a boolean (as a 4-byte int) from a file stream."""
    return get_int(f) != 0


def get_string(f: Any) -> str:
    """Reads a length-prefixed string from a file stream."""
    length: int = get_int(f)
    if length <= 0 or length > 10000:
        return ""
    return f.read(length).decode("utf-8", errors="ignore")


def prettify(name: str) -> str:
    """Translates internal game IDs to human-readable strings."""
    known = {
        "MISSILES_2_PLAYER": "Artemis Missile",
        "MISSILES_HULL": "Hull Missile",
        "LASER_CHAINGUN": "Chain Laser",
        "LASER_BURST_2": "Burst Laser II",
        "LASER_BURST_3": "Burst Laser III",
        "LASER_BURST_1": "Burst Laser I",
        "LASER_HULL_2": "Hull Laser II",
        "LASER_HULL_1": "Hull Laser I",
        "BOMB_BREACH_2": "Breach Bomb II",
        "BOMB_HEAL_SYSTEM": "Healing Burst",
        "SHOTGUN": "Flak I",
        "SHOTGUN_2": "Flak II",
        "BEAM_FIRE": "Fire Beam",
        "ION_CHARGEGUN": "Charge Ion",
        "DEFENSE_2": "Defense Drone II",
        "DEFENSE_1": "Defense Drone I",
        "SHIP_REPAIR": "Hull Repair Drone",
        "COMBAT_BEAM": "Combat Beam Drone",
        "ANTI_DRONE": "Anti-Combat Drone",
        "DRONE_RECOVERY": "Drone Recovery Arm",
        "ROCK_ARMOR": "Rock Plating",
        "ZOLTAN_BYPASS": "Zoltan Shield Bypass",
        "WEAPON_PREIGNITER": "Weapon Pre-Igniter",
        "LONG_RANGE_SCANNER": "Long-Ranged Scanners",
        "SCRAP_COLLECTOR": "Scrap Recovery Arm",
    }
    if name in known:
        return known[name]
    s: str = name.replace("_", " ").title()
    s = (
        s.replace(" 1", " I")
        .replace(" 2", " II")
        .replace(" 3", " III")
        .replace(" 4", " IV")
    )
    return s


def parse_save(sav_path: str) -> str:
    """Parses an FTL continue.sav file for ship information."""
    blueprint: str = "Unknown"
    sector: int = 1

    try:
        with open(sav_path, "rb") as f:
            file_format: int = get_int(f)
            if file_format == 11:
                get_bool(f)
            if file_format in [7, 8, 9, 11]:
                get_bool(f)
            for _ in range(5):
                get_int(f)
            get_string(f)  # playerShipName
            blueprint = get_string(f)
            sector = get_int(f)
            data: bytes = f.read()
    except (OSError, struct.error, ValueError):
        return ""

    weapons: list[str] = []
    drones: list[str] = []
    augments: list[str] = []
    first_offset: int = -1

    for match in re.finditer(b"[A-Za-z0-9_]{4,}", data):
        s: str = match.group(0).decode("ascii", errors="ignore")
        start: int = match.start()
        end: int = match.end()

        if first_offset != -1 and start - first_offset > 2000:
            continue

        is_weapon: bool = False
        if "DLC" in s or "BOMBER" in s:
            pass
        elif any(
            x in s
            for x in [
                "LASER",
                "BEAM",
                "BOMB",
                "MISSILES",
                "ION",
                "SHOTGUN",
                "HALBERD",
                "GLAIVE",
                "FLAK",
                "CHARGE",
            ]
        ) and s not in ["COMBAT_BEAM", "weapon_upgrade"]:
            is_weapon = True

        is_drone: bool = False
        if (
            "DEFENSE_" in s
            or "COMBAT_" in s
            or "DRONE_" in s
            or "SHIP_REPAIR" in s
            or "ANTI_DRONE" in s
        ) and "RECOVERY" not in s and s not in ["used_drone", "DRONE_RECOVERY"]:
            is_drone = True

        is_augment: bool = False
        if s in [
            "DRONE_RECOVERY",
            "ROCK_ARMOR",
            "ZOLTAN_BYPASS",
            "WEAPON_PREIGNITER",
            "SCRAP_COLLECTOR",
            "REPAIR_ARM",
            "LONG_RANGE_SCANNER",
        ]:
            is_augment = True

        if is_weapon or is_drone or is_augment:
            if first_offset == -1:
                first_offset = start

            if is_weapon or is_drone:
                if end + 4 <= len(data):
                    armed_val: int = struct.unpack("<i", data[end : end + 4])[0]
                    if armed_val in (0, 1):
                        if is_weapon and s not in weapons:
                            weapons.append(s)
                        if is_drone and s not in drones:
                            drones.append(s)
            elif is_augment and s not in augments:
                augments.append(s)

    ship_class: str = blueprint.replace("PLAYER_SHIP_", "")
    layout: str = "A"
    if ship_class.endswith("_2"):
        layout = "B"
        ship_class = ship_class[:-2]
    elif ship_class.endswith("_3"):
        layout = "C"
        ship_class = ship_class[:-2]

    if ship_class == "HARD":
        ship_class = "Kestrel"

    parts: list[str] = []
    parts.append(f"Ship: {ship_class.title()} {layout}")
    parts.append(f"Sector: {sector}")
    if weapons:
        parts.append(f"Weapons: {', '.join(prettify(w) for w in weapons)}")
    if drones:
        parts.append(f"Drones: {', '.join(prettify(d) for d in drones)}")
    if augments:
        parts.append(f"Augments: {', '.join(prettify(a) for a in augments)}")

    return "\n".join(parts)


def do_save() -> None:
    """Handles the saving of a snapshot."""
    if not os.path.isfile(SRC):
        print(f"Error: FTL save not found at {SRC}", file=sys.stderr)
        sys.exit(1)

    suggestion: str = f"continue_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sav"
    filename: str = input_with_prefill("Save snapshot as: ", suggestion).strip()

    if not filename:
        print("Error: filename cannot be empty", file=sys.stderr)
        sys.exit(1)

    if not filename.endswith(".sav"):
        filename += ".sav"

    dest_path: str = os.path.join(dest_dir, filename)
    meta_path: str = dest_path + ".meta"

    if os.path.exists(dest_path):
        confirm: str = input(f"{dest_path} already exists. Overwrite? [y/N] ")
        if not confirm.lower().startswith("y"):
            print("Aborted.")
            sys.exit(1)

    parsed_info: str = parse_save(SRC)
    prev_description: str = last_description()

    if " - Sec" in prev_description or " - W:" in prev_description:
        prev_description = ""

    if parsed_info:
        print("\n--- Current Save Data ---")
        print(parsed_info)
        print("-------------------------\n")

    description: str = input_with_prefill(
        "Description (optional): ", prev_description
    ).strip()

    shutil.copy2(SRC, dest_path)

    with open(meta_path, "w", encoding="utf-8") as f:
        if parsed_info:
            f.write(parsed_info + "\n")
        f.write(f"Description: {description}\n\n")
        f.write(f"Saved: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"Saved snapshot to {dest_path}")


def do_restore() -> None:
    """Handles restoring a snapshot via fzf."""
    os.makedirs(dest_dir, exist_ok=True)
    saves: list[tuple[float, str]] = []
    for fname in os.listdir(dest_dir):
        if fname.endswith(".sav"):
            full_path = os.path.join(dest_dir, fname)
            saves.append((os.path.getmtime(full_path), fname))

    if not saves:
        print(f"No saved snapshots found in {dest_dir}", file=sys.stderr)
        sys.exit(1)

    saves.sort(reverse=True, key=lambda x: x[0])
    save_names: list[str] = [x[1] for x in saves]

    script_path = os.path.abspath(__file__)
    preview_cmd = f"python3 {script_path} --show-meta {{}}"

    fzf = subprocess.Popen(
        [
            "fzf",
            "--height=70%",
            "--layout=reverse",
            "--border",
            "--prompt=Restore > ",
            "--header=Select a snapshot to restore  (Enter: confirm, Esc: cancel)",
            "--preview=" + preview_cmd,
            "--preview-window=right:55%:wrap",
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )

    out, _ = fzf.communicate("\n".join(save_names))
    if not out:
        print("Aborted.")
        sys.exit(1)

    choice = out.strip()
    if not choice:
        print("Aborted.")
        sys.exit(1)

    print(f"\nSelected: {choice}")
    meta_path = os.path.join(dest_dir, choice + ".meta")
    if os.path.isfile(meta_path):
        with open(meta_path, "r", encoding="utf-8") as f:
            print(f.read())
    print()

    confirm = input(
        f"Restore this snapshot over the current FTL save? This will overwrite {SRC} [y/N] "
    )
    if not confirm.lower().startswith("y"):
        print("Aborted.")
        sys.exit(1)

    os.makedirs(os.path.dirname(SRC), exist_ok=True)
    shutil.copy2(os.path.join(dest_dir, choice), SRC)
    print(f"Restored '{choice}' to {SRC}")


def usage() -> None:
    """Prints usage information."""
    print(f"Usage: {os.path.basename(__file__)} [save|restore]")
    print("\n  save      Save a snapshot of the current FTL game state (default).")
    print("  restore   Browse and restore a previously saved snapshot.")


def main() -> None:
    """Main entry point."""
    if len(sys.argv) > 1 and sys.argv[1] == "--show-meta":
        resolve_dest_dir()
        if len(sys.argv) > 2:
            show_meta(sys.argv[2])
        sys.exit(0)

    check_deps()
    resolve_dest_dir()

    mode: str = "save"
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ("save", "-s", "--save"):
            mode = "save"
        elif arg in ("restore", "-r", "--restore"):
            mode = "restore"
        elif arg in ("-h", "--help"):
            usage()
            sys.exit(0)
        else:
            print(f"Unknown option: {arg}", file=sys.stderr)
            usage()
            sys.exit(1)

    if mode == "save":
        do_save()
    elif mode == "restore":
        do_restore()


if __name__ == "__main__":
    main()
