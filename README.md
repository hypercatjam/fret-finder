# fret-finder

**fret-finder** is a Python tool designed to optimize Guitar Pro tabs by transposing notes to more ergonomic fret and string positions. It uses the highest fret in each beat as an anchor and shifts the other notes accordingly, aiming for easier, more natural fingerings. It's a feature I always wished GP had internally so I decided to try to make it.

---

## Features

- Analyzes GuitarPro files (.gp5) to find the best string and fret positions.  
- Uses the highest fret per beat as an anchor.  
- Transposes notes horizontally to minimize awkward stretches or slides.  
- Works using the [pyguitarpro](https://pypi.org/project/PyGuitarPro/) library.  
- Saves optimized tabs to new GuitarPro files.

## Warning

- This is just a prototype I'm messing around with for fun. I've tested it very miniamally with mixed, but acceptable results with editing. I aim to improve it. Would be cool to someday make a plugin for TuxGuitar with the logic.
- Currently only works with E Standard.

---

## Prerequisites
1. [Python](https://www.python.org/downloads/release/python-3136/)
2. [pyguitarpro](https://pypi.org/project/PyGuitarPro/)

## Installation

1. Install pyguitarpro:

    ```bash
    pip install pyguitarpro
    ```

2. Clone this repository:

    ```bash
    git clone https://github.com/hypercatjam/fret-finder.git
    cd fret-finder
    ```

    Or [click here to download](https://github.com/hypercatjam/fret-finder/archive/refs/heads/main.zip) and

   ```bash
   cd C:\Documents\fret-finder
   ```
   
4. Set up your folder:

   Place your .gp5 file (must be gp5 or older) into the same folder as the python script. **You must rename it to "input.gp5".**


6. Run the script:

    ```bash
    python tab_optimizer.py

7. Check results:

   Check the fret-finder folder for the output file. You will need to edit to your preference.

---


## Examples

Below is a before and after processing a tab with fret-finder. You can see how the tab before has unnecessary jumps while the after result is much more ergonomic.

[Before](https://imgur.com/7jDdPSg)

[After](https://imgur.com/re4BJ92)
