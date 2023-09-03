"""
A self-replicating file.
Not technically a quine.
"""


import datetime
import subprocess

from argparse import ArgumentParser


# Parse args.
parser = ArgumentParser()
parser.add_argument(
    "-r", "--reps",
    default=1, type=int,
    help="remaining replications"
)

args = parser.parse_args()

# Read file contents.
# NOTE: __file__ is the path to the curr file.
with open(__file__, mode="r") as f:
    contents = f.read()

# Write contents to new file.
curr_date = datetime.datetime.now()
formatted_date = curr_date.strftime("%Y_%m_%d_%H_%M_%S")
new_file = f"gene_{formatted_date}_{args.reps}.py"

with open(new_file, mode="w") as f:
    f.write(contents)

# Run new file.
if args.reps > 1:
    subprocess.run([
        "py", new_file,
        "-r", str(args.reps - 1)
    ])
