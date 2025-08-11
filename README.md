# fret-finder

**fret-finder** is a Python tool designed to optimize Guitar Pro tabs by transposing notes to more ergonomic fret and string positions. It uses the highest fret in each beat as an anchor and shifts the other notes accordingly, aiming for easier, more natural fingerings. It's a feature I always wished GP had internally. Would be great to just right click highlighted notes and select "Optimize".

This is especially useful for transposing tabs that have unnecessary vertical stretches as opposed to skips, making them easier to play and cleaner to read.
---

## Features

- Analyzes GuitarPro files (.gp5) to find the best string and fret positions.  
- Uses the highest fret per beat as an anchor.  
- Transposes notes horizontally to minimize awkward stretches or slides.  
- Works using the [pyguitarpro](https://github.com/Thiht/py-guitarpro) library.  
- Saves optimized tabs to new GuitarPro files.

## Warning

- This is just a prototype I'm messing aroun with for fun. I've only tested it with a couple bars with mixed, but acceptable results with editing. I am to improve it.

---

## Prerequisites
1. [Python](https://www.python.org/downloads/release/python-3136/)
2. [pyguitarpro](https://github.com/Thiht/py-guitarpro)

## Installation

1. Install pyguitarpro:

    ```bash
    pip install pyguitarpro
    ```

2. Download this repository:

    ```bash
    git clone https://github.com/yourusername/fret-finder.git
    cd fret-finder
    ```

    Or [click here](https://github.com/hypercatjam/fret-finder/archive/refs/heads/main.zip).
   
4. Set up your folder:

   Place your .gp5 file (must be gp5 or older!) into the same folder as the python script. **You must rename it to "input.gp5".**

   If you didn't clone the repository, CD to the folder:

   ```bash
   cd C:\Documents\fret-finder
   ```

6. Run the script:

    ```bash
    python tab_optimizer.py

7. Check results:

   Check the fret-finder folder for the output file.

---

## Usage

Run the optimizer script:

```bash
python tab_optimizer.py
```

## Examples

![Before](https://imgur.com/7jDdPSg)

![After](https://imgur.com/re4BJ92)
