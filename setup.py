from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1',
      description='Clean',
      url='https://github.com/OShcherbatiuk/sort',
      author='Oleksii Shcherbatiuk',
      author_email='oleksii.shcherbatiuk@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean_folder:main']}
      )
