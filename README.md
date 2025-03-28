# Einleitung
Basic idea: Use positiondata of exisiting grocery chains to find new spots to open a store.

Hypthesis: The output would be a decent starting point for the analysis for the opening of a new store. But there would be many points lacking that should be added to the analysis. Like costs, proximity to customers, proximity to competitors, or if there is room to open a store.

# Methodik
Data can be gathered from Migros directly.
They provide a map with all their stores (https://filialen.migros.ch/) 
The data can't be download but could be scraped, and used in visually since the location is in a nice json format:  
"location": {
                "city": "Zürich",
                "address2": "",
                "geo": {
                    "lon": 8.535889,
                    "lat": 47.3786818
                },
                "address": "Sihlquai",
                "country": "CH",
                "zip": "8001"
            }

Once a map with stores in an area for example has been created there are multiple approaches to find new spots
Method 1) draw circles around the existings stores. Depending on the type and size of the store (also part of the data that is provided by migros) the radius of the circle could be larger or smaller, assuming that larger stores are able to satisfy larger areas of the population.

Method 2) Using routing the travel time/distance could be used to create the areas where a store is able to provide their service, again larger stores might be able to provide larger areas.

Regardless of which method is selected, the negative area would be the no-service area, where opening new stores could be considered.
