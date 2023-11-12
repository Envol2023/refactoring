D'accord, voici un exemple simple de code Python 3.10 avec une fonction trop longue que vous pourriez refactoriser en extrayant des fonctions distinctes. Le code utilise des listes et des dictionnaires sans l'utilisation de classes. Les types hints sont également inclus, et des tests unitaires avec pytest sont fournis pour chaque phase.

**Code Initial :**

```python
def long_function(data: list, config: dict) -> list:
    result = []

    # Bloc 1
    for item in data:
        if item['status'] == 'active':
            result.append(item['name'].capitalize())

    # Bloc 2
    for item in result:
        if len(item) > config['max_length']:
            item = item[:config['max_length']]

    # Bloc 3
    for item in result:
        if config.get('prefix'):
            item = config['prefix'] + item

    return result
```

**Tests Unitaires Initiaux :**

```python
def test_long_function():
    data = [{'name': 'john', 'status': 'active'},
            {'name': 'jane', 'status': 'inactive'},
            {'name': 'bob', 'status': 'active'}]
    
    config = {'max_length': 5, 'prefix': 'user_'}

    result = long_function(data, config)

    assert result == ['User_john', 'User_bob']
```

**Code Refactorisé :**

```python
def extract_block_1(data: list) -> list:
    result = []
    for item in data:
        if item['status'] == 'active':
            result.append(item['name'].capitalize())
    return result


def extract_block_2(result: list, config: dict) -> list:
    for i, item in enumerate(result):
        if len(item) > config['max_length']:
            result[i] = item[:config['max_length']]
    return result


def extract_block_3(result: list, config: dict) -> list:
    for i, item in enumerate(result):
        if config.get('prefix'):
            result[i] = config['prefix'] + item
    return result


def refactor_function(data: list, config: dict) -> list:
    result = extract_block_1(data)
    result = extract_block_2(result, config)
    result = extract_block_3(result, config)
    return result
```

**Tests Unitaires Refactorisés :**

```python
def test_refactor_function():
    data = [{'name': 'john', 'status': 'active'},
            {'name': 'jane', 'status': 'inactive'},
            {'name': 'bob', 'status': 'active'}]

    config = {'max_length': 5, 'prefix': 'user_'}

    result = refactor_function(data, config)

    assert result == ['user_john', 'user_bob']
```

Dans cet exemple, les trois blocs distincts ont été extraits en trois fonctions distinctes, et la fonction principale `refactor_function` utilise ces fonctions pour obtenir le même résultat. Les tests unitaires ont également été ajustés en conséquence.