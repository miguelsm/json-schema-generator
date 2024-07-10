#!/usr/bin/env python3

import json
from genson import SchemaBuilder

# Read the JSON document from a file
with open('input.json', 'r') as file:
    data = json.load(file)

# Initialize SchemaBuilder
builder = SchemaBuilder()
builder.add_object(data)

# Get the JSON schema
schema = builder.to_schema()

# Print the schema
print(json.dumps(schema, indent=4))
