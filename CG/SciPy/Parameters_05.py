# -*- coding: utf-8 -*-
import pygal

france_chart = pygal.FrenchMap_Regions(legend_at_bottom=True, legend_box_size=8, legend_font_size=8, truncate_legend=6)
france_chart.title = 'Sample Regions'
france_chart.add('Alsace', ['42']) 
france_chart.add('Aquitaine', ['72'])
france_chart.add('Auvergne', ['83'])
france_chart.add('Brittany', ['53'])
france_chart.add('Burgundy', ['26'])
france_chart.add('Centre', ['24'])
france_chart.add('Champagne-Ardenne', ['21'])
france_chart.add(unicode('Franche-Comt�', 'utf-8'), ['43'])
france_chart.add(unicode('�le-de-France', 'utf-8'), ['11'])
france_chart.add('Languedoc-Roussillon', ['91'])
france_chart.add('Limousin', ['74'])
france_chart.add('Lorraine', ['41'])
france_chart.add('Lower Normandy', ['25'])
france_chart.add(unicode('Midi-Pyr�n�es', 'utf-8'), ['73'])
france_chart.add('Nord-Pas-de-Calais', ['31'])
france_chart.add('Pays de la Loire', ['52'])
france_chart.add('Picardy', ['22'])
france_chart.add('Poitou-Charentes', ['54'])
france_chart.add(unicode('Provence-Alpes-C�te d\'Azur', 'utf-8'), ['93'])
france_chart.add(unicode('Rh�ne-Alpes', 'utf-8'), ['83'])
france_chart.add('Upper Normandy', ['23'])
france_chart.add('Corsica', ['94'])
france_chart.add('French Guiana', ['03'])
france_chart.add('Guadeloupe', ['01'])
france_chart.add('Mayotte', ['05']) 
france_chart.add('Reunion', ['04'])

france_chart.render_to_file('france_map.svg')

