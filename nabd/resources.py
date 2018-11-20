import os
import random
from nabweb import settings
from pathlib import Path

class Resources(object):
  @staticmethod
  def find(type, resources):
    """
    Find a resource from its type and its name.
    Return the first found resource, resources being delimited by semi-colons
    Perform localization and random lookups with specific tag.
    Files are first searched in <app>/<type>/<locale>/ then <app>/<type>/
    Random lookup is performed when component is * or *.suffix
    """
    for filename in resources.split(';'):
      path0 = Path(resources)
      if path0.is_absolute():
        if path0.is_file():
          return path0 # Already found
        raise ValueError('find_resource expects a relative path, got {path}'.format(path = filename))
      if "/" in type:
        raise ValueError('find_resource expects a directory name for type, got {type}'.format(type = type))
      is_random = path0.name.startswith('*')
      if is_random:
        result = Resources._find_random(type, path0.parent.as_posix(), path0.name)
      else:
        result = Resources._find_file(type, filename)
      if result != None:
        return result
    return None

  @staticmethod
  def _find_file(type, filename):
    from .i18n import get_locale
    all_apps = settings.INSTALLED_APPS
    basepath = Path(settings.BASE_DIR)
    locale = get_locale()
    for app in all_apps:
      for path in [basepath.joinpath(app, type, locale, filename), basepath.joinpath(app, type, filename)]:
        if path.is_file():
          return path
    return None

  @staticmethod
  def _find_random(type, parent, pattern):
    from .i18n import get_locale
    all_apps = settings.INSTALLED_APPS
    basepath = Path(settings.BASE_DIR)
    locale = get_locale()
    for app in all_apps:
      for path in [basepath.joinpath(app, type, locale, parent), basepath.joinpath(app, type, parent)]:
        if path.is_dir():
          list = path.glob(pattern)
          if list != []:
            return random.choice(sorted(list))
    return None