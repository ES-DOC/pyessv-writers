# -*- coding: utf-8 -*-

"""
.. module:: map_cmip6.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Maps CMIP5 ESGF publisher ini file to normalized pyessv format.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
from utils import yield_comma_delimited_options
from utils import yield_pipe_delimited_options


# TODO process map: institute_map = map(model : institute)
# TODO process map: las_time_delta_map = map(time_frequency : las_time_delta)

# Vocabulary collections extracted from ini file.
COLLECTIONS = {
	('cmor_table', yield_comma_delimited_options),
	('ensemble', r'r[0-9]+i[0-9]+p[0-9]+'),
	('experiment', yield_pipe_delimited_options),
	('institute', lambda: yield_institute),
	('las_time_delta', lambda: yield_las_time_delta),
	('model', yield_comma_delimited_options),
	('time_frequency', yield_comma_delimited_options),
	('product', yield_comma_delimited_options),
	('realm', yield_comma_delimited_options),
	('thredds_exclude_variables', yield_comma_delimited_options),
	('variable', yield_comma_delimited_options),
	('version', r'^v[0-9]*$')
}


# Arbitrary data associated with a collection.
COLLECTION_DATA = {
	'experiment': {
		'cim_document_type': 'cim.1.activity.NumericalExperiment',
		'cim_document_type_alternative_name': 'experiment'
	},
	'model': {
		'cim_document_type': 'cim.1.software.ModelComponent',
		'cim_document_type_alternative_name': 'model'
	}
}

# Fields extracted from ini file & appended as data to the scope.
SCOPE_DATA = {
	'filename_format',
	'directory_format',
	'dataset_id'
}


def yield_institute(ctx):
	"""Yields institute information to be converted to pyessv terms.

	"""
	for _, institute in ctx.ini_section.get_option('institute_map', '\n', '|'):
		yield institute


def yield_las_time_delta(ctx):
	"""Yields las time delta information to be converted to pyessv terms.

	"""
	for _, las_time_delta in ctx.ini_section.get_option('las_time_delta_map', '\n', '|'):
		yield las_time_delta
