import pylons.config as config
import ckan.plugins.toolkit as toolkit
from ckan.logic.action import create
from . import change_pkg_dict_for_import_deployment


def package_create(context, data_dict):
    if '_ckanapi' in data_dict: # ckanapi call
        data_dict = change_pkg_dict_for_import_deployment(data_dict, 'create')
        if data_dict['type'] in ['publications', 'opendata']:
            context['defer_commit'] = True 
        c._ckanapi = '_ckanapi'
        del data_dict['_ckanapi']
    return create.package_create(context, data_dict)


