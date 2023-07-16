### Installation:

#### MacOS/Linux:
1. Download this repository either by `git clone`ing it or downloading a zipped version in the "Code" dropdown:
   <img width="300" alt="image" src="https://github.com/Ben-Drucker/PDF-Resize/assets/66132763/79a55f29-d450-4221-b26b-ecde16030004">
1. Install the latest version of Python here: https://www.python.org/downloads/.
2. Make sure the `PATH` environment variable is setup so that — when running `python3 --version` — the version is the most up-to-date release. (As of 7/15/2023, it is 3.11.4.).
3. Install the dependencies by running `pip3 install -r requirements.txt` (while in this directory)
4. While in this, directory, run `sudo cp pdf_resize.py /Applications`, which will place the script in a convenient location (Applications)
5. Add `/Applications` to the `PATH` by opening a text editor (e.g., `open -a textedit ~/.zshrc`) and adding `export PATH=/Applications:$PATH`. Make sure to edit the `rc` file corresponding to your terminal's default shell. (Determine this using `echo $0`.)
6. Restart your terminal.

#### Windows:
TBD

### Usage
To use, run 

```bash
python3 pdf_resize.py -w output_width_in_inches -h output_height_in_inches path/to/input.pdf path/to/output.pdf
```

(If you forget, you can run `python3 pdf_resize.py --help)

If the user does not provide `-w` or `-h` arguments, the program will use a default of 8.5" and 11", respectively.

Here are some example runs:

```bash
python3 pdf_resize.py my_input.pdf resized_output.pdf
```

```bash
python3 pdf_resize.py -w 8.5 -h 11 my_input.pdf resized_output.pdf
```

```bash
python3 pdf_resize.py -h 8.5 -w 11 my_input.pdf resized_output.pdf
```
