"""
Fake git history - A python script to create fake git history.
Created by: Katt Morgen (https://github.com/katt204/)
"""

import os

import rong  # type: ignore

from .cli import main


def new_main() -> None:
    log = rong.Log(debug=True)
    try:
        main()
    except KeyboardInterrupt:
        log.errormsg("[!] KeyboardInterrupt: Stopping the running process...")
    except Exception as e:
        log.errormsg(f"Error: {e}")

    log.waitmsg("Cleaning up...")

    # scan all .txt file with 20 digit alpha name in current dir and delete them
    for file in os.listdir():
        if file.endswith(".txt") and len(file) == 24:
            os.remove(file)

    log.okmsg("Cleaned up successfully!")

    print()
    # reminder to give a star to the repo
    log.yellow("😃 If you liked the script, please consider giving a star in GitHub repo.")
    log.okmsg("https://github.com/katt204/fake-git-history")
    log.success("❤️  Thank you for using the script! :)")


if __name__ == "__main__":
    new_main()
