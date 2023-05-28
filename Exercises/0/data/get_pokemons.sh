while IFS= read -r line; do
    echo "Downloading: $line"

    curl https://pokeapi.co/api/v2/pokemon-species/voltorb > pokemons/"$line.json"
    sleep 1
done < pokemon_list.txt
