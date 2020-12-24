import inspect
import glob
import os
import importlib


def _iter_package_module_names(package_root):
    init_filename = os.path.join(package_root, '__init__.py')
    for py_filename in sorted(glob.glob(os.path.join(package_root, '*.py'))):
        if py_filename != init_filename:
            filename_root, _ = os.path.splitext(py_filename)
            module_name = os.path.basename(filename_root)
            yield module_name


def _iter_module_subclasses(package, module_name, base_cls):
    module = importlib.import_module('.' + module_name, package)
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, base_cls):
            yield obj


def iter_subclasses(package_root, base_cls, is_abstract):
    package = 'desensitize.' + os.path.basename(package_root)
    for module_name in _iter_package_module_names(package_root):
        for cls in _iter_module_subclasses(package, module_name, base_cls):
            if not is_abstract(cls):
                yield cls


def update_locals(locals_instance, instance_iterator, *args, **kwargs):
    for instance in instance_iterator():
        locals_instance.update({type(instance).__name__: instance.__class__})
