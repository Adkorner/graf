# graf
Dátová štruktúra Graph, ktorá implementuje neorientovaný neohodnotený graf reprezentovaný ako asociatívne pole množín susedov.
Vstupný súbor je binárny.<br />
Program binárny súbor spracuje a využije implementované metódy
* in_distance(v1, start, end=None) vráti množinu mien vrcholov, ktorých vzdialenosť od daného vrcholu v1 nie je menšia ako parameter start a nie je väčšia ako parameter end; ak má parameter end hodnotu None, označuje to, že end=start
* max(v1) vráti dvojicu (tuple): maximálnu vzdialenosť od vrcholu v1 k nejakému vrcholu v grafe a množinu všetkých vrcholov s touto vzdialenosťou; napríklad pre izolovaný vrchol (nemá susedov) metóda vráti 0 a jednoprvkovú množinu samotného vrcholu
* for_all(v1) vráti zoznam (list), v ktorom i-ty prvok obsahuje množinu všetkých tých vrcholov v grafe, ktoré majú vzdialenosť od vrcholu v1 práve i; napríklad pre izolovaný vrchol metóda vráti [{v1}]
* in_middle(v1, v2) vráti množinu všetkých tých vrcholov v grafe, ktoré majú rovnakú vzdialenosť od v1 ako od v2, t.j. vrcholy ležia presne medzi oboma danými vrcholmi; predpokladajte, že zadané vrcholy sú rôzne; môžete využiť volanie metód for_all(v1) a for_all(v2)
