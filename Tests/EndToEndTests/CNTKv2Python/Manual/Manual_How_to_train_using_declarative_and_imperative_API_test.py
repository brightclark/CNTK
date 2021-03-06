# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

import os
import re
import sys
import pytest

abs_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(abs_path, "..", "Tutorials"))

from nb_helper import get_output_stream_from_cell

notebook = os.path.join(abs_path, "..", "..", "..", "..", "Manual", "Manual_How_to_train_using_declarative_and_imperative_API.ipynb")

def test_cntk_how_to_train_no_errors(nb):
    if os.getenv("OS")=="Windows_NT" and sys.version_info[0] == 2:
        pytest.skip('tests with Python 2.7 on Windows are not stable in the CI environment. ')
    errors = [output for cell in nb.cells if 'outputs' in cell
              for output in cell['outputs'] if output.output_type == "error"]
    assert errors == []

expectedOutput = r'Minibatch\[ 191- 200\]: loss = '
def test_cntk_how_to_train_eval_correct(nb):
    if os.getenv("OS")=="Windows_NT" and sys.version_info[0] == 2:
        pytest.skip('tests with Python 2.7 on Windows are not stable in the CI environment. ')
    testCells = [cell for cell in nb.cells
                if cell.cell_type == 'code']
    assert len(testCells) == 5
    for c in testCells[1:]:
        text = get_output_stream_from_cell(c)
        print(text)
        assert re.search(expectedOutput, text)
