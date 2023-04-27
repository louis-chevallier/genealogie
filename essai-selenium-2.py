#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 09:16:29 2023

@author: pierre
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
options = FirefoxOptions()
options.add_argument('--headless')

#ouverture FireFox
browser = webdriver.Firefox(options=options)

#sur deuxieme ecran
browser.set_window_position(2000,1)
browser.maximize_window()

#ouverture page archive morbihan
browser.get('https://rechercher.patrimoines-archives.morbihan.fr/archive/resultats/etatcivil/n:6?RECH_acte%5B0%5D=bapt%C3%AAmes&RECH_unitdate_debut=1500&RECH_unitdate_fin=1800&type=etatcivil')
time.sleep(5) 

fin = False

#boucle à faire sur le multipage des communes
while not fin :
    # récupération des éléments clickable (les yeux)
    liste_doc = browser.find_elements(By.XPATH, "//a[@class='arc_img_visu']")
    for link in liste_doc :
        link.click()
        time.sleep(6)
        print("xxx")
        # switch à faire sur le deuxieme onglet où s'affiche les doc
        
        # insérer le traitement des pages cf A plus bas (au fait ! les fonctions ça existe ! j(avais oublié !!))

        
        # + test à faire si plus de page (click à prévoir sur page suivante)
    fin = True
    print("")
    #bug actuellement sur le passage à la la commune d'Ambon ...
        
    

# partie A : tirage des echantillons dans un doc

#   # nombre de pages du document
#   elem_total = browser.find_element(By.CLASS_NAME, "bn-gallery-counter-total")
#   npage = int(elem_total.text)
#   print(npage)
#   
#   # pour ne pas prendre les premieres pages
#   marge_debut = 6
#   # pour ne pas prendre les dernieres pages
#   marge_fin = 6
#
#   # un echantillon tous les delta    
#   delta = 20
#
#   # page courante
#   i = marge_debut
#
#   while i < npage -marge_fin :
#       print(i)
#
#       # récupération de l'élémént input du numero de page
#       elem = browser.find_element(By.CLASS_NAME, "bn-gallery-counter-current")
#
#       # effacement du champ
#       elem.clear()
#
#       # ecriture du numero de page voulu
#       elem.send_keys(str(i))
#       elem.send_keys(Keys.ENTER)
#       time.sleep(5)
#
#       # bouton download
#       elem = browser.find_element(By.CLASS_NAME, "bn-toolbox-button-download")
#       # lancement du download
#       elem.click()
#
#       # page suivante
#       i+=delta



browser.quit()
