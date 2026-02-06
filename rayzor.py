import argparse
import sys

from colorama import Fore, Style, init

import collect_configs


def main():
    parser = argparse.ArgumentParser(prog="raysor", description="Raysor CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    subparsers.required = True

    # --- 'collect' command ---
    collect_parser = subparsers.add_parser("collect", help="Run the collection process")

    # 1. --channels (Flag, required)
    collect_parser.add_argument(
        "--channels",
        required=True,  # Makes this mandatory
        type=str,
        help="Path of the channels file",
    )

    # 2. --hours-back (Flag, required)
    collect_parser.add_argument(
        "--hours-back", required=True, type=int, help="Number of hours to go back"
    )

    # 3. --output (Flag, required)
    collect_parser.add_argument(
        "--output", required=True, type=str, help="Path for the output file"
    )

    args = parser.parse_args()

    if args.command == "collect":
        collect_configs.run(args.channels, args.hours_back, args.output)


init(autoreset=True)


def print_banner():
    # Using Option 1 (The Blade)
    banner = r"""
      ____  ___ __  __ ____  ____  ____ 
     / __ \/   |\ \/ /__  / / __ \/ __ \
    / /_/ / /| | \  /  / / / / / / /_/ /
   / _, _/ ___ | / /  / /_/ /_/ / _, _/ 
  /_/ |_/_/  |_|/_/  /____\____/_/ |_|  
        """
    print(Fore.RED + Style.BRIGHT + banner)
    # print(Fore.WHITE + "        [ DEV: " + Fore.RED + "DRACO-TLW" + Fore.WHITE + " ]")
    print(
        Fore.RED
        + Style.BRIGHT
        + " > "
        + Fore.LIGHTWHITE_EX
        + Style.NORMAL
        + "CUTTING THROUGH NOISE."
        + Fore.RED
        + Style.BRIGHT
        + " FINDING SIGNAL."
    )
    print("-" * 42)
    print(Style.RESET_ALL, end="")


def setup_fixed_screen():
    """
    Clears screen, prints banner, and sets the scroll region
    so the banner never moves.
    """
    # Clear screen and go to top home
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Print your banner
    print_banner()

    # --- THE IMPORTANT PART ---
    # We need to tell the terminal to only scroll starting from line 11.
    # (Your banner takes up about 10 lines visual space).
    TOP_MARGIN = 11

    # Set Scroll Region: line 11 to bottom
    sys.stdout.write(f"\033[{TOP_MARGIN};r")

    # Move cursor to the start of the scroll region
    sys.stdout.write(f"\033[{TOP_MARGIN};1H")
    sys.stdout.flush()


def restore_terminal():
    """Resets terminal to normal behavior on exit."""
    sys.stdout.write("\033[r")  # Reset scroll region
    sys.stdout.write("\033[999;1H")  # Move cursor to bottom
    sys.stdout.write(Style.RESET_ALL)  # Reset colors
    sys.stdout.flush()


if __name__ == "__main__":
    try:
        setup_fixed_screen()
        main()

    except KeyboardInterrupt:
        pass
    finally:
        restore_terminal()
