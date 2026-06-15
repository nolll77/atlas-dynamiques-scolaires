# Sources de données

| Source | URL | Format | Licence | Variables clés |
|---|---|---|---|---|
| IPS historiques | data.education.gouv.fr | CSV | Licence Ouverte 2.0 | ips, sigma_ips |
| Résultats bac (IVAL) | data.education.gouv.fr | CSV | Licence Ouverte 2.0 | taux_reussite, valeur_ajoutee |
| IRIS INSEE | insee.fr | CSV | Libre réutilisation | revenu_median, CSP |
| DVF Etalab | data.gouv.fr | CSV | Étalab Open Licence | valeur_fonciere |
| Géolocalisation établissements | data.education.gouv.fr | GeoJSON | Licence Ouverte 2.0 | latitude, longitude |
| Accessibilité transport | data.iledefrance-mobilites.fr | GTFS | ODbL | temps_acces_gare |
| Contours IRIS | geoservices.ign.fr | Shapefile | Licence IGN | geometry |

⚠️ **Note révision IPS 2021** : La méthodologie de calcul de l'IPS a été révisée en 2021.
Les comparaisons avant/après cette date doivent tenir compte de cette discontinuité.

## Objectif de profondeur historique

Afin de permettre la viabilité et l'exécution des analyses longitudinales du Tome III (notamment les modèles temporels et la détection de ruptures), l'architecture mathématique du projet exprime un besoin de profondeur historique. 

Pour garantir la robustesse de ces modèles spatio-temporels, la constitution du jeu de données idéal intégrerait l'historique des variables dynamiques (IPS, Valeurs Foncières, Résultats du Bac) en remontant jusqu'à l'année 2018.
