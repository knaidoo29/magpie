import setuptools
from numpy.distutils.core import setup, Extension

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

exts = []
exts.append(Extension(name='magpie.src.pixel_utils', sources=['magpie/src/pixel_utils.f90']))
exts.append(Extension(name='magpie.src.pixel_1dto2d', sources=['magpie/src/pixel_1dto2d.f90']))
exts.append(Extension(name='magpie.src.pixel_1dto3d', sources=['magpie/src/pixel_1dto3d.f90']))
exts.append(Extension(name='magpie.src.pixel_polar_ea', sources=['magpie/src/pixel_polar_ea.f90']))
exts.append(Extension(name='magpie.src.pixel_binbyindex', sources=['magpie/src/pixel_binbyindex.f90']))
exts.append(Extension(name='magpie.src.remap_utils', sources=['magpie/src/remap_utils.f90']))
exts.append(Extension(name='magpie.src.remap_1d_grid2grid', sources=['magpie/src/remap_1d_grid2grid.f90']))
exts.append(Extension(name='magpie.src.remap_2d_grid2grid', sources=['magpie/src/remap_2d_grid2grid.f90']))
exts.append(Extension(name='magpie.src.remap_3d_grid2grid', sources=['magpie/src/remap_3d_grid2grid.f90']))
exts.append(Extension(name='magpie.src.rotate_2d', sources=['magpie/src/rotate_2d.f90']))
exts.append(Extension(name='magpie.src.math', sources=['magpie/src/math.f90']))
exts.append(Extension(name='magpie.src.rotate_3d', sources=['magpie/src/rotate_3d.f90']))

setup(name = 'magpie-pkg',
      version = "0.3.2",
      description       = "Monte cArlo weiGhted PIxel rEmapping",
      long_description  = long_description,
      long_description_content_type = 'text/markdown',
      url               = 'https://github.com/knaidoo29/magpie',
      author            = "Krishna Naidoo",
      author_email      = "krishna.naidoo.11@ucl.ac.uk",
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=['numpy', 'matplotlib', 'healpy'],
      ext_modules = exts,
      python_requires = '>=3',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Mathematics',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      )
