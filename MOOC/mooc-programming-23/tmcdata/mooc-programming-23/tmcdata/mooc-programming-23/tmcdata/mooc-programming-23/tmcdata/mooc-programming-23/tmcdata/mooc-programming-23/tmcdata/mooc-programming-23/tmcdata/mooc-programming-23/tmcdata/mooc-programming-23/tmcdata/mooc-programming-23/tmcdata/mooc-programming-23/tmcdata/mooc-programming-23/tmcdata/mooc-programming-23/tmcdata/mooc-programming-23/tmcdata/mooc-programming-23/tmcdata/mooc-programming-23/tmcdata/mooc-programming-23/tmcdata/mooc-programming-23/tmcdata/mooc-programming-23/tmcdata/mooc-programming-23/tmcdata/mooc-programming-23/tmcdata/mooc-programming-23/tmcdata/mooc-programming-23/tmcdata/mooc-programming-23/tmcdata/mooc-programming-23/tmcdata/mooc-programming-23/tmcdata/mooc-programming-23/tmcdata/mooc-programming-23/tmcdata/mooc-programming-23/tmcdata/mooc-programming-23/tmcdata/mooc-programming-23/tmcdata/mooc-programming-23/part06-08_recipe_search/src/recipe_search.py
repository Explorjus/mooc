def search_by_name(filename: str, word: str):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    recipes = []
    current_recipe = []
    
    for line in lines:
        line = line.strip()
        
        if line == '':
            if current_recipe:
                recipes.append(current_recipe)
            current_recipe = []
        else:
            current_recipe.append(line)
    
    if current_recipe:
        recipes.append(current_recipe)
    
    found_recipes = []
    
    for recipe in recipes:
        name = recipe[0]
        if word.lower() in name.lower():
            found_recipes.append(name)
    
    return found_recipes

def search_by_time(filename: str, prep_time: int):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    recipes = []
    current_recipe = []
    
    for line in lines:
        line = line.strip()
        
        if line == '':
            if current_recipe:
                recipes.append(current_recipe)
            current_recipe = []
        else:
            current_recipe.append(line)
    
    if current_recipe:
        recipes.append(current_recipe)
    
    found_recipes = []
    
    for recipe in recipes:
        name = recipe[0]
        time = int(recipe[1])
        if time <= prep_time:
            found_recipes.append(f"{name}, preparation time {time} min")
    
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    recipes = []
    current_recipe = []
    
    for line in lines:
        line = line.strip()
        
        if line == '':
            if current_recipe:
                recipes.append(current_recipe)
            current_recipe = []
        else:
            current_recipe.append(line)
    
    if current_recipe:
        recipes.append(current_recipe)
    
    found_recipes = []
    
    for recipe in recipes:
        name = recipe[0]
        time = int(recipe[1])
        ingredients = recipe[2:]
        if any(ingredient.lower() in ingredient_line.lower() for ingredient_line in ingredients):
            found_recipes.append(f"{name}, preparation time {time} min")
    
    return found_recipes

if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_time("recipes1.txt", 20)
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_ingredient("recipes1.txt", "milk")
    for recipe in found_recipes:
        print(recipe)