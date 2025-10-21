#!/usr/bin/env python3
"""
Test runner script for the Company Reference API.
"""
import subprocess
import sys
import argparse


def run_tests(test_type="all", verbose=False, coverage=False, watch=False):
    """Run tests with specified options."""
    cmd = ["uv", "run", "pytest"]
    
    if verbose:
        cmd.append("-v")
    
    if coverage:
        cmd.extend(["--cov=app", "--cov-report=html", "--cov-report=term-missing"])
    
    if watch:
        cmd.append("--watch")
    
    if test_type == "unit":
        cmd.extend(["-m", "unit"])
    elif test_type == "integration":
        cmd.extend(["-m", "integration"])
    elif test_type == "fast":
        cmd.extend(["-m", "not slow"])
    
    print(f"Running: {' '.join(cmd)}")
    return subprocess.run(cmd)


def main():
    """Main test runner function."""
    parser = argparse.ArgumentParser(description="Run tests for Company Reference API")
    parser.add_argument(
        "--type", 
        choices=["all", "unit", "integration", "fast"], 
        default="all",
        help="Type of tests to run"
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("-c", "--coverage", action="store_true", help="Generate coverage report")
    parser.add_argument("-w", "--watch", action="store_true", help="Watch for file changes")
    
    args = parser.parse_args()
    
    result = run_tests(
        test_type=args.type,
        verbose=args.verbose,
        coverage=args.coverage,
        watch=args.watch
    )
    
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()