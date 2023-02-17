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
     *Borderless Template by PsilosX
     *Created by JohnPrime
    """
    template_file_name = "JohnPrime/WomansdayShort"
    template_suffix = "Womansday Short"


"""
MDFC TEMPLATES
"""


class BorderlessMDFCBackTemplate (temp.MDFCBackTemplate):
    """
    Borderless version of the MDFC Back template
     *Standard MDFC Template by SilvanMTG
     *Borderless MDFC Template by PsilosX
     *Created by JohnPrime
    """
    template_file_name = "JohnPrime/BorderlessMDFCBack"
    dfc_layer_group = con.layers.MDFC_BACK
    template_suffix = "Borderless MDFC"

    def __init__(self, layout):
        cfg.remove_reminder = True
        super().__init__(layout)

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill
        psd.content_fill_empty_area(self.art_layer)


class BorderlessMDFCFrontTemplate (temp.MDFCFrontTemplate):
    """
    Borderless version of the MDFC Front template
     *Standard MDFC Template by SilvanMTG
     *Borderless MDFC Template by PsilosX
     *Created by JohnPrime
    """
    template_file_name = "JohnPrime/BorderlessMDFCFront"
    dfc_layer_group = con.layers.MDFC_FRONT
    template_suffix = "Borderless MDFC"
 
 
"""
Borderless Transform TEMPLATES
"""
class BorderlessTransformFrontTemplate (temp.BorderlessTransformFrontTemplate):
    """
     *Borderless Transform Template by PsilosX
     *Created by JohnPrime
    """
    template_file_name = "JohnPrime/BorderlessTransformFront"
    template_suffix = "Borderless Transform"


class BorderlessTransformBackTemplate (temp.BorderlessTransformBackTemplate):
    """
     *Borderless Transform Template by PsilosX
     *Created by JohnPrime
    """
    template_file_name = "JohnPrime/BorderlessTransformBack"
    template_suffix = "Borderless Transform"