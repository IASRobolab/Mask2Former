from setuptools import setup, find_packages

setup(name='Mask2Former',
      version='1.0.0',
      description='Mask2Former for Panoptic Segmentation',
      author='Federico Rollo',
      author_email='rollo.f96@gmail.com',
      url='https://github.com/robolableonardo/Mask2Former',
      install_requires=['torch>=1.9.0', 'torchvision>=0.10.0','cython', 'scipy', 'shapely', 'timm', 'h5py', 'submitit', 'scikit-image'],
      packages=find_packages(),
      keywords=[
          'Instance Segmentation',
          'Semantic Segmentation',
          'Panoptic Segmentation'
          'Deep Learning',
      ])
      

