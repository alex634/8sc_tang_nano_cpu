# How to Assemble a Program

*While this guide isn't going to be operating system specific, it was written with Linux in mind.*

## Setup

Make sure that Python 3.10 or newer is installed. In addition, make sure that [Jinja-Cli](https://pypi.org/project/jinja-cli/) is installed. You may want to use [Anaconda](https://www.anaconda.com/) or create a venv for installing Jinja-Cli.

## Assembling

The program assembler is located in the `scripts` directory. It is called `assembler.py`. To assemble a file run `python3 assembler.py <input_file_name> <output_file_name> --overwrite`. \<input_file_name\> should be the file to assemble. The input file's extension doesn't matter. Make sure that the output file has a `.json` file extension. The assembled code is represented in json.

Once we have created the `.json` file, we now have to convert it into a Verilog ROM file. If you installed Jinja-Cli in an environment, make sure to activate that environment now. Execute the following to convert the `.json` file to a Verilog file `jinja -d <output_file_name> instruction_rom.v.jinja >instruction_rom.v`. Notice that the \<output_file_name\> is the file from earlier.

Now, take the `instruction_rom.v` file that you generated and copy it into the `src` directory and overwrite the `instruction_rom.v` file that already exists in that directory.
