# Chaste code generation from SBML

`chaste_codegen_sbml` takes [SBML](https://synonym.caltech.edu/) models as input and uses [libSBML](https://synonym.caltech.edu/software/libsbml/) to parse the models and output C++ code for Chaste.

## Installation
We recommend installing in a virtual environment e.g.
```
python -m venv /path/to/new/virtual/environment
source /path/to/new/virtual/environment/bin/activate
```

User installation:
```
cd /path/to/chaste_codegen_sbml
pip install .
```

Developer installation. This adds additional dependencies for development and testing (e.g. `pytest`) and makes the installation editable:
```
pip install -e .[dev]
```

## Usage
```
chaste_codegen_sbml [-h] sbml_file
```

## Testing
