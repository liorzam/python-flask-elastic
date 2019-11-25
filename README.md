### Installation
clone the repository

    cd python-flask-elastic
    docker-compose up -d

Run the migrations for elasticsearch

    cd migrations
    python3 migration_runner.py    

### Usage
To add a pokemon to the database:
```
curl --header "Content-Type: application/json" -d "{
   \"pokadex_id\": 25,
   \"name\": \"Stam\",   
   \"nickname\": \"Lior Ha Gever\", 
   \"level\": 60,
   \"type\": \"ELECTRIC\",
   \"skills\": [
       \"Tail Whip\"
   ]
}" localhost:5000/new_pokemon
```
To search (autocomplete) for a pokemon, browse to 
http://localhost:5000/autocomplete/<search_term>
### Requirements
* docker-compose
* python3.6+

``` 


curl --header "Content-Type: application/json" -d "{                                         
   \"pokadex_id\": 26,
   \"name\": \"Pikachu\",
   \"nickname\": \"Baruh Ha Gever\",
   \"level\": 60,
   \"type\": \"ELECTRIC\",
   \"skills\": [
       \"Tail Whip\"
   ]
}"
```

### Notes
The migration script should wait until the elasticsearch 
warms up (estimated: 25 seconds)
