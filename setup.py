from setuptools import setup

setup(
    name='DailyProphet',
    version='0.8',
    author='Schrotty',
    long_description=__doc__,
    packages=['DailyProphet'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'Werkzeug']
)
