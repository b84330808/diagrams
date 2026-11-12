"""
Custom provides the possibility of load an image to be presented as a node.
"""

import os

from diagrams import Node


class Custom(Node):
    _provider = "custom"
    _type = "custom"
    _icon_dir = None

    fontcolor = "#ffffff"

    def _load_icon(self):
        return self._icon

    def __init__(self, label, icon_path, *args, **kwargs):
        # Graphviz resolves a relative image path from the output directory, so
        # the icon goes missing when the diagram filename includes a directory.
        # Resolve an icon found from the working directory to an absolute path.
        if not os.path.isabs(icon_path) and os.path.isfile(icon_path):
            icon_path = os.path.abspath(icon_path)
        self._icon = icon_path
        super().__init__(label, *args, **kwargs)
