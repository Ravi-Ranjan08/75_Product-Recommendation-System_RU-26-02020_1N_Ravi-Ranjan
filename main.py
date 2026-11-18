#Name: Ravi Ranjan
#ERP: RU-26-02020
#Section: 1-N

#stores each customer's purchased products

purchases = {
    "Amit": ["Laptop", "Mouse", "Keyboard"],
    "Bina": ["Laptop", "Mouse", "Headphones"],
    "Chetan": ["Phone", "Charger"],
    "Divya": ["Laptop", "Keyboard", "Monitor", "Webcam"],
}

#calculates similarity between two customers using jaccard similarity
def jaccard_similarity(set_a, set_b):
    union = set_a | set_b  #all unique produts
    if len(union) == 0:
        return 0.0
    return len(set_a & set_b) / len(union)  #common products / Total products
    

#find the customers by names (ignores uppercase and lowercase)
def find_customer(name):
    for customer in purchases:
        if customer.lower() == name.lower():
            return customer
    return None  #Returns none if customer is not found 
    

#Returns the similarity score from a pair
def get_score(pair):
    return pair[1]
    

#calculates similarity scores with all other customers
def calculate_scores(customer):
    my_products = set(purchases[customer]) # selectd customers products
    scores = []
    for other, products in purchases.items():
        if other != customer: # skips the same customer
            score = jaccard_similarity(my_products, set(products))
            scores.append((other, score))
    scores.sort(key=get_score, reverse=True) # Highest score first 
    return scores
    

# find the most popular product among all customers
def most_popular_product():
    counts = {}
    for products in purchases.values():
        for product in products:
            counts[product] = counts.get(product, 0) + 1
    best_product = max(counts, key=counts.get)
    return best_product, counts[best_product]
    

# Recommends products based on the most similar customer
def recommend(customer):
    scores = calculate_scores(customer)
    best_customer, best_score = scores[0]
    
    
# if no similar customer is found, show the popular product
    if best_score == 0:
        product, count = most_popular_product()
        print("No similar customers found.")
        print(f"Popular product: {product} (bought by {count} customers)")
        return

# Displays similarity scores of other customers     
    print("Similarity scores:")
    for other, score in scores:
        print(f"{other} : {score:.2f}")
    print(f"Most similar customer: {best_customer}")
    
#find products the selected customer has not purchased
    new_products = []
    for product in purchases[best_customer]:
        if product not in purchases[customer]:
            new_products.append(product)

# displays recommended products
    if new_products:
        print("Recommended:", ", ".join(new_products))
    else:
        print("No new products to recommend.")
        

# main function starts the program
def main():
    name = input("Recommend for: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    customer = find_customer(name)
    if customer is None:
        print(f"Customer '{name}' not found.")
        return

    recommend(customer)
    

#calls the main function
main()
