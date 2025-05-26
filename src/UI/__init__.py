# import PyQt6
# import os

# # Caminho para o diretório de instalação do PyQt6 (geralmente dentro do site-packages)
# pyqt6_path = os.path.dirname(PyQt6.__file__)
# print(f"Diretório de instalação do PyQt6: {pyqt6_path}")

# # O diretório do Qt para o PyQt6 estará tipicamente em uma subpasta 'Qt6' dentro deste.
# qt_bin_path = os.path.join(pyqt6_path, 'Qt6', 'bin')
# qt_plugins_path = os.path.join(pyqt6_path, 'Qt6', 'plugins', 'sqldrivers')

# print(f"Caminho potencial para binários Qt (qmake, designer, etc.): {qt_bin_path}")
# print(f"Caminho potencial para plugins SQL do Qt: {qt_plugins_path}")

# # Você pode verificar se esses diretórios existem
# print(f"O diretório de plugins SQL existe? {os.path.exists(qt_plugins_path)}")