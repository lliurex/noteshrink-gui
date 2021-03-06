#!/usr/bin/env python
#
# $Id: setup.py,v 1.32 2010/10/17 15:47:21 ghantoos Exp $
#
#    Copyright (C) 2008-2009  Ignace Mouzannar (ghantoos) <ghantoos@ghantoos.org>
#
#    This file is part of lshell
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup
import os

if __name__ == '__main__':

	setup(name='noteshrink-gui',
		version='0.1',
		description='Graphic user interface for noteshrink',
		long_description="""""",
		author='Lliurex Team',
		author_email='raurodse@gmail.com',
		maintainer='Raul Rodrigo Segura',
		maintainer_email='raurodse@gmail.com',
		keywords=['software',''],
		url='https://github.com/lliurex/noteshrink',
		license='GPL',
		platforms='UNIX',
#        scripts = [''],
		packages = ['noteshrinkgui'],
		package_dir = {'noteshrinkgui':'app'},
		package_data = {'noteshrinkgui':['rsrc/*']},
		scripts = ['noteshrink-gui'],
		classifiers=[
				'Development Status :: 4 - Beta',
				'Environment :: Console'
				'Intended Audience :: End Users',
				'License :: OSI Approved :: GNU General Public License v3',
				'Operating System :: POSIX',
				'Programming Language :: Python',
				'Topic :: Software store',
				'Topic :: Install apps',
				],
	)
