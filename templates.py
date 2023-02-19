"""
JOHNPRIME TEMPLATES
"""
import os
from functools import cached_property

import proxyshop.text_layers as text_classes
from proxyshop.__console__ import console
from proxyshop import templates as temp
from proxyshop import format_text as ft
from proxyshop.constants import con
from proxyshop.settings import cfg
import proxyshop.helpers as psd


class WomansdayShortTemplate (temp.NormalTemplate):
    """
     * Womansday Short Template
     * Created by JohnPrime
    """
    template_file_name = "JohnPrime/WomansdayShort"
    template_suffix = "Showcase Short"


"""
MDFC TEMPLATES
"""


class BorderlessMDFCBackTemplate (temp.MDFCBackTemplate):
    """
    Borderless version of the MDFC Back template
    """
    template_file_name = "JohnPrime/BorderlessMDFCBack"
    dfc_layer_group = con.layers.MDFC_BACK
    template_suffix = "Showcase"

    def __init__(self, layout):
        cfg.remove_reminder = True
        super().__init__(layout)

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill
        psd.content_fill_empty_area(self.art_layer)


class BorderlessMDFCFrontTemplate (BorderlessMDFCBackTemplate):
    """
    Borderless version of the MDFC Front template
    """
    template_file_name = "JohnPrime/BorderlessMDFCFront"
    dfc_layer_group = con.layers.MDFC_FRONT
    template_suffix = "Showcase"


"""
Double faced card templates
"""


class BorderlessTFBackTemplate (temp.NormalTemplate):
    """
    Template for the back faces of transform cards.
    """
    template_file_name = "JohnPrime/BorderlessTFBack"
    dfc_layer_group = con.layers.TF_BACK
    template_suffix = "Borderless"

    def __init__(self, layout):
        cfg.remove_reminder = True
        super().__init__(layout)

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill
        psd.content_fill_empty_area(self.art_layer)
        



class BorderlessTFFrontTemplate (BorderlessTFBackTemplate):
    """
    Template for the front faces of transform cards.
    """
    template_file_name = "JohnPrime/BorderlessTFFront"
    dfc_layer_group = con.layers.TF_FRONT
    template_suffix = "Borderless"