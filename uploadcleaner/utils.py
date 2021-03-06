'''
Copyright PuzzleDev s.n.c.
Created on Jul 14, 2012

@author: Michele Sama (m.sama@puzzledev.com)
'''
import os

from django.db import models
from django.db.models.fields.files import FileField
from django.db.models import loading

def ensure_dir(filename):
    """ Creates the given folder if it does not exist.
    """
    dirname = os.path.dirname(filename)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)


def files_at_path(media_folder):
    """ List all the files in the given path and in all
        of its subfolders.
    """
    found_files = []
    for root, dirnames, filenames in os.walk(media_folder):
        filenames = [os.path.join(root, x) for x in filenames]
        filenames = [x for x in filenames if os.path.isfile(x)]
        for filename in filenames:
            found_files.append(os.path.abspath(unicode(filename)))
    return found_files


def filefields_in_model(model_class):
    """ Creates a list with all the FileField
        of a given model.
    """
    if not issubclass(model_class, models.Model):
        raise AssertionError(
                "Given class %s does not extend from Model."
                % model_class)

    fields = [x
            for x in model_class._meta.fields
            if isinstance(x, FileField)]
    return fields


def linked_files_from_model(model_class):
    """ List all the files linked by all the instances
        of the given model.
    """
    files = []
    # Get all the file fields
    fields = filefields_in_model(model_class)
    instances = model_class.objects.all()
    for instance in instances:
        for field in fields:
            file_field_instance = getattr(instance, field.name)
            if file_field_instance.name:
                # the file name is set -> this instance links a file
                files.append(os.path.abspath(file_field_instance.path))
    return files


def linked_files_from_all_models():
    """ List all the files linked by all the
        registered models.
    """
    model_classes = loading.get_models()
    files = []

    for model_class in model_classes:
        for f in linked_files_from_model(model_class):
            files.append(f)
    return files