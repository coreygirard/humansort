# Sorting for humans

[![Build Status](https://travis-ci.org/coreygirard/humansort.svg?branch=master)](https://travis-ci.org/coreygirard/humansort) <br>
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Sorts filenames and similar strings the way you actually want them sorted. Instead of:

```
1_data.json
1_thing.json
2_data.json
2_thing.json
filename_1.py
filename_10.py
filename_11.py
filename_2.py
filename_20.py
filename_21.py
```

We get:

```
1_data.json
2_data.json
1_thing.json
2_thing.json
filename_1.py
filename_2.py
filename_10.py
filename_11.py
filename_20.py
filename_21.py
```

## Installation

```
pip install humansort
```

## Usage

```python
import humansort

list_of_strings = humansort.sort(list_of_strings)
```

Many thanks to [Ross Reisman](https://github.com/RossReisman) for ~bitching about~ questioning the status quo and inspiring this
