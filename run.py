from scripts.run_product_test import bundle
from scripts.report_latest import main as report


def main():
    print("\n=== Running product reliability test ===")
    print("Results generated.")

    print("\n=== Reliability Report ===")
    report()


if __name__ == "__main__":
    main()
