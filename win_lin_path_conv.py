#!/bin/env python

import subprocess
import tkinter
import argparse
import textwrap
from itertools import chain

class WinLinPathConverter:
    @staticmethod
    def _convert_win_to_lin_path(win_path: str) -> str:
        lin_path = win_path.replace("\\", "/")
        if lin_path.startswith("//"):
            lin_path = "smb:" + lin_path
        return lin_path

    @staticmethod
    def _get_clipboard_string() -> str:
        tk = tkinter.Tk()
        tk.withdraw()
        return tk.selection_get()

    @staticmethod
    def _parse() -> argparse.Namespace:
        class _RawDescriptionHelpFormatterWithNewlines(argparse.RawDescriptionHelpFormatter):
            def _split_lines(self, text, width):
                return list(chain.from_iterable([textwrap.wrap(t, width) for t in text.splitlines()]))

        default_help_message = "Show this help message and exit."
        parser = argparse.ArgumentParser(add_help=False, description="Windows to Linux path converter.", formatter_class=_RawDescriptionHelpFormatterWithNewlines)
        parser.add_argument("-h", "--help", action="help", help=default_help_message)
        parser.add_argument("-c", "--clipboard", type=int, required=False, default=True,
                            help="Take windows UNC path from clipboard. Otherwise it needs to get entered manually. 0=No, 1=Yes. Default: %(default)s.")
        parser.add_argument("-p", "--pause", type=int, required=False, default=True,
                            help="Pause before leaving the program to see the its output. 0=No, 1=Yes. Default: %(default)s.")
        return parser.parse_args()

    @staticmethod
    def run() -> None:
        args = WinLinPathConverter._parse()
        print("This tool converts Windows-UNC-paths to Linux-SMB-paths")
        print("")
        if args.clipboard:
            windows_path = WinLinPathConverter._get_clipboard_string()
        else:
            windows_path = input("Please enter a Windows-UNC-path: ")
        print(f"Trying to open entered path \"{windows_path}\"...")
        subprocess.run(["xdg-open", WinLinPathConverter._convert_win_to_lin_path(windows_path)])
        if args.pause:
            input("Press Enter to leave the program:")


def main() -> None:
    WinLinPathConverter.run()


if __name__ == "__main__":
    main()

