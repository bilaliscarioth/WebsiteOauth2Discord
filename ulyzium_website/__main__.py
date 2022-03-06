import sys

def main() -> None:
    from .__run__ import run  # pylint: disable=import-outside-toplevel
    run()

if __name__ == "__main__":
    main()
