# sexpressionToJSON
Convert s-expressions to json

### Usage

json_data = getSet("(:qty '1' :item 'A thing') (:qty '1' :item 'Another thing')")

print(json_data)



[{"item" : "A thing", "qty": "1"},{"item" : "Another thing", "qty": "1"}]


