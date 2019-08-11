##
## Mifare NFC Python Module for Heiko
##
## Copyright (C) 2019 Christian Carlowitz <chca@cmesh.de>
##
##	This program is free software: you can redistribute it and/or modify it
##	under the terms of the GNU Lesser General Public License as published by the
##	Free Software Foundation, either version 3 of the License, or (at your
##	option) any later version.
##
##	This program is distributed in the hope that it will be useful, but WITHOUT
##	ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
##	FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
##	for more details.
##
##	You should have received a copy of the GNU Lesser General Public License
##	along with this program.  If not, see <http://www.gnu.org/licenses/>
##

all:
	-rm *.so
	python3 setup.py build_ext --inplace
	ln -s mnfc.*.so mnfc.so
