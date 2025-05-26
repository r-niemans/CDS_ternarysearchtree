import pytest
from trees.ternary_tree import TernarySearchTree, TtreeNode
from trees.ternary_tree_B import TernarySearchTreeB
from trees.ternary_tree_recursive import TernarySearchTreeRecursive
from trees.ternary_tree_minimalistic import TernarySearchTreeSparse


@pytest.mark.parametrize("tree_class", [
    TernarySearchTree,
    TernarySearchTreeB,
    TernarySearchTreeRecursive,
    TernarySearchTreeSparse
])
@pytest.mark.parametrize("word_list", [
    (["pizza", "cars", "can", "doll", "dormroom"]),
    (["avocado", "arsenal", "apextwin"]),
])
def test_basic_insert_and_search(tree_class, word_list):
    """Check if inserted words can be found in the tree"""
    tst = tree_class()
    for word in word_list:
        tst.insert(word)
    for word in word_list:
        assert tst.search(word, exact=True), f"{word} not found"
    assert not tst.search('', exact=True), 'Empty string should not be found'


def load_not_insert_words():
    """Load words from 'data/not_insert_words.txt'."""
    with open("data/not_insert_words.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

@pytest.mark.parametrize("word_list", [
    ([
    "ramen", "chicken", "broccoli", "snowpeas", "scallions", "garlic", "ginger", "soy", "sesame", "oyster", "maple",
    "sriracha", "bouillon", "noodles", "vegetable", "oil", "salt", "pepper", "sesameoil", "oyster sauce", "maple syrup",
    "chicken thighs", "chicken breasts", "garlic cloves", "sesame seeds", "cabbage", "carrots", "babycorn",
    "bellpeppers", "mushrooms", "tofu", "bokchoy", "egg", "tomarashi", "prawn", "shrimp", "snappeas", "spinach",
    "edamame", "corn", "redpepper", "lime", "cilantro", "scallion", "snow peas", "broil", "bake", "roast", "stirfry",
    "sheetpan", "oven", "skillet", "boil", "sauté", "grill", "steam", "blanch", "simmer", "fry", "panfry", "microwave",
    "pressurecook", "airfry", "soy sauce", "sesame oil", "teriyaki", "hoisin", "fishsauce", "chili oil", "miso", "tahini",
    "peanut sauce", "vinegar", "ketchup", "mustard"]),
    (["mayonnaise", "hot sauce", "barbecue sauce", "ponzu", "gochujang",
    "sambal", "nuoc cham", "onion", "chives", "basil", "mint", "parsley", "thyme", "rosemary", "dill", "oregano",
    "cumin", "coriander", "paprika", "turmeric", "cinnamon", "nutmeg", "clove", "cardamom", "fennel", "anise", "bayleaf",
    "lemongrass", "kaffir lime", "curry", "chili", "sugar", "honey", "molasses", "brown sugar", "white sugar",
    "black pepper", "white pepper", "red pepper", "cayenne", "", "sesame seed", "poppy seed", "caraway",
    "celery seed", "crispy", "caramelized", "umami", "savory", "sweet", "spicy", "tangy", "zesty", "rich", "hearty",
    "light", "fresh", "aromatic", "fragrant", "bold", "mild", "fusion", "traditional", "authentic", "modern", "classic",
    "comfort", "gourmet", "homemade", "quick", "easy", "simple", "fast", "healthy", "nutritious", "balanced", "indulgent",
    "decadent", "budget", "affordable", "economical", "cost-effective", "value", "premium", "deluxe", "fancy", "elegant",
    "sophisticated", "rustic", "homestyle", "family-friendly", "kid-friendly", "vegetarian", "vegan", "gluten-free",
    "dairy-free", "low-carb", "high-protein", "low-fat", "low-sodium", "organic", "natural", "seasonal", "local",
    "sustainable", "eco-friendly", "farm-to-table", "artisanal", "handcrafted", "small-batch", "scratch-made"]),
    (["avocado", "arsenal", "apextwin"]),
])
def test_full_tree_functionality(word_list):
    tst = TernarySearchTree()

    for word in word_list:
        tst.insert(word)

    for word in word_list:
        assert tst.search(word, exact=True), f"Exact search failed for '{word}'"

    for word in word_list:
        for i in range(1, len(word)):
            word_part = word[:i]
            assert tst.search(word_part, exact=False), f"Prefix search failed for '{word_part}'"

    assert not tst.search("apextwin", exact=True), "Non-existent word found, should not be found"
    assert not tst.search('', exact=True), "Empty string should not be found"

    all_words = tst.all_strings()
    assert set(all_words) == set(word_list), f"Expected words {word_list}, got {all_words}"

    assert len(tst) == len(set(word_list)), f"Expected size of {tst} is {len(set(word_list))}, got {len(tst)}"

    assert isinstance(tst._root, TtreeNode), f"Root {tst._root} is not a node"

@pytest.mark.parametrize("tree_class", [
    TernarySearchTree,
    TernarySearchTreeB,
    TernarySearchTreeRecursive,
    TernarySearchTreeSparse
])
def test_words_not_inserted(tree_class):
    """Ensure words from 'not_insert_words.txt' are not found."""
    tst = tree_class()
    not_insert_words = load_not_insert_words()

    for word in not_insert_words:
        assert not tst.search(word, exact=True), f"{word} should not be found"
