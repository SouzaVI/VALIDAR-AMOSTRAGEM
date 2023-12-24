# -*- coding: utf-8 -*-
"""
/***************************************************************************
 gerar_etapa
                                 A QGIS plugin
 Este plugin ira gerar a etapa feito e a proxima etapa caso necessario
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-14
        copyright            : (C) 2023 by Helio Antonio de Olivera Junior \ TERRAM
        email                : helio.engflorestal@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load gerar_etapa class from file gerar_etapa.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gerar_etapa import gerar_etapa
    return gerar_etapa(iface)
