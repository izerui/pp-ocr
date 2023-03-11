from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Add framework_pb2.py to `hiddenimports` list.
hiddenimports = collect_submodules('paddle')

# Collect all data files
datas = collect_data_files('paddle')