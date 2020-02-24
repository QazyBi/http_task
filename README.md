# http_task


## Anagrams that are valid
- ["foobar", "barfoo", "boofar"]
- ["живу", "вижу"]
- ["Abba", "BaBa"]

## Invalid Anagrams
- ["abba", "bba"] - во второй строке только одна буква "а"

## How to use:

### Add a dictionary
- curl localhost:8080/load -d '["foobar", "aabb", "baba", "boofar", "test"]'

### Find anagrams of a word
- curl 'localhost:8080/get?word=foobar' => ["foobar","boofar"]
- curl 'localhost:8080/get?word=raboof' => ["foobar","boofar"]
- curl 'localhost:8080/get?word=abba' => ["aabb","baba"]
- curl 'localhost:8080/get?word=test' => ["test"]
- curl 'localhost:8080/get?word=qwerty' => null
