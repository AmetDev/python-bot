import requests

# Get all items
response = requests.get("http://45.130.43.65/items/")
if response.status_code == 200:
    items = response.json()
    print("All items:", items)
else:
    print("Failed to retrieve items")

# Get item with id 1
response = requests.get("http://45.130.43.65/items/1")
if response.status_code == 200:
    item = response.json()
    print("Item with id 1:", item)
else:
    print("Failed to retrieve item with id 1")

# Create a new item
new_item = {"field1": "value1", "field2": "value2"}
response = requests.post("http://45.130.43.65/items/", json=new_item)
if response.status_code == 201:
    print("Successfully created new item")
else:
    print("Failed to create new item")

# Update item with id 1
updated_item = {"field1": "updated_value1", "field2": "updated_value2"}
response = requests.put("http://45.130.43.65/items/", json=updated_item)
if response.status_code == 200:
    print("Successfully updated item with id 1")
else:
    print("Failed to update item with id 1")

# Delete item with id 1
response = requests.delete("http://45.130.43.65/items/")
if response.status_code == 204:
    print("Successfully deleted item with id 1")
else:
    print("Failed to delete item with id 1")
