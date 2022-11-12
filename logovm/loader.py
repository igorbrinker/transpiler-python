# This file is part of LogoVM
#
# Copyright (C) 2022 Rafael Guterres Jeffman
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <https://www.gnu.org/licenses/>.

"""Loader for LogoVM programs."""

import logging

from logoasm.symtable import get_symbols_by_class, set_symbol
from logovm.errors import UndefinedReference


def loader():
    """Adjust addresses to rum program."""
    # Uses global symtable.
    for symbol, data in get_symbols_by_class("FUNC").items():
        code = data.get("code")
        if code is None:
            logging.error("Undefined function: %s", symbol)
            raise UndefinedReference("FUNCTION", symbol)
        for addr, cmd in enumerate(code):
            if cmd.startswith("LABEL"):
                _, name = cmd.split(" ", 1)
                set_symbol(name, pc=addr)
