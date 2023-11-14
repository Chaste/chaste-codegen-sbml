import sys
import os
from os.path import basename
from libsbml import SBMLReader
from . import translator
from . import filewriters

def IsSrnModel(path_to_file):
    """ Function to be used in another pipeline (inherits from translator)."""
    reader = SBMLReader()
    document = reader.readSBMLFromFile(path_to_file)
    model = document.getModel()

    return translator.IsSrnModel(model)

def GetOutputFilenames(path_to_file, filename):
    """ Function to get the names of the translated files that need to be moved. Returns in order
    [header file, source file]. """
    outputfiles = []

    #Get the model from the file
    reader = SBMLReader()
    document = reader.readSBMLFromFile(path_to_file)
    model = document.getModel()

    if( translator.IsSrnModel(model) ):
        header_file = filename + "SrnModel.hpp"
        source_file = filename + "SrnModel.cpp"

        outputfiles.append(header_file)
        outputfiles.append(source_file)
    else:
        header_file = filename + "CellCycleModel.hpp"
        source_file = filename + "CellCycleModel.cpp"

        outputfiles.append(header_file)
        outputfiles.append(source_file)

    return outputfiles

def MoveFilesToDirectory(files, new_path):
    """ Moves output files to specified directory. """
    #Get current path
    current_path = os.getcwd()

    for i in range(len(files)):
        os.rename(current_path + "/" + files[i], new_path + "/" + files[i])

def Generate(sbml_file, output_filename=None, output_directory=None):
    """ Main function. Arguments are:
    Input, Output Filename, Output Directory. """

    #Get the model from the file
    reader = SBMLReader()
    document = reader.readSBMLFromFile(sbml_file)
    model = document.getModel()

    #Get Name of file
    if not output_filename:
        output_filename = basename(sbml_file).split('.')[0]

    # If there are events in the model, we define the class as a cell cycle model.
    # Otherwise, the model is assumed to be a subcellular reaction network model.
    if translator.IsSrnModel(model):
        filewriters.WriteSrnModelToFile(output_filename, model)
    else:
        filewriters.WriteCcmModelToFile(output_filename, model)

    if not output_directory:
        output_directory = "."

    output_files = GetOutputFilenames(sbml_file, output_filename)

    #Move created files if output directory has been specified.
    MoveFilesToDirectory(output_files, output_directory)
