from pyspark.sql.types import size

print("Hello world")

# if-else condition:
score = 72

if score >=90 and score < 100:
    grade = "A"
elif score >= 70 and score < 90:
    grade = "B"
elif score >=50 and score >70:
    grade = "c"
else:
    grade = "d"

print (f"score is {score} -> grade you got is {grade}")

#
price  = 205.21
stock  = 1
rating = 3

is_in_stock = stock > 0
is_recomended = rating >= 4
is_affordable = price < 300

if is_in_stock and is_recomended:
    recomendation = "Great choice - stock is highly rated"
elif is_in_stock and not is_recomended:
    recomendation = "stock is available but ratings are mixed"
else:
    recomendation = "out of stock"

print("------")
print(recomendation)
print(type(is_in_stock),type(is_recomended),type(is_affordable))

#=========================================================================================

# Assigning to agents based on the user message:

customer_query = "Where is my order? ORD3024"
q = customer_query.lower()

if "cancel" in q or 'refund' in q:
    agent,urgency = 'human agent','high'
elif "where" in q or 'Delivery' in q or 'track' in q:
    agent,urgency = 'order_agent','Normal'
elif "product" in q or "discount" in q:
    agent, urgency = 'promotion_agent', 'Normal'
else:
    agent,urgency = 'general_agent','Normal'

print(f"customer_query: {customer_query} call_agent {agent} and the urgency is {urgency}")

#=====================================================================================


statues = ["Delivered","In Transit","cancelled","Refunded","Unknown"]

for status in statues:
    if status == "Delivered":
        msg = "your order is delivered"
    elif status == "In Transit":
        msg = "On the way"
    elif status == "cancelled":
        msg = "Your order has been cancelled"
    else:
        msg = (f"status : {status} -> please contact support")

    print(f"{status:12s} --> {msg}")

#==============================================================================

fruits = ["apple", "banana", "cherry"]

for key,value in enumerate(fruits):
    print(f"{[key]} {value}")
#===========================================================================================

test_queries = [
    "Where is my order #3042?",
    "I want to cancel my purchase",
    "Do you have a discount code?",
    "What are the specs of the Classic Monitor?",
]

results = []

for index,query in enumerate(test_queries):
    print(f"iter : {index}, query : {query}")

    q = query.lower()
    if "cancel" in q or "refund" in q:
        agent = "human_agent"
    elif "where" in q or "track" in q:
        agent = "order_agent"
    elif "discount" in q or "price" in q:
        agent = "promotions_agent"
    elif "spec" in q or "product" in q:
        agent = "catalog_agent"
    else:
        agent = "general_agent"

    results.append({'index' : index,'query' : query,'agent' : agent})

for r in results:

    print(f"([{r['index']}]  {r['query']:45s} -> {r['agent']}")

#============================================================================================

# Batch processing — split 9 queries into batches of 3
total_queries = 9
batch_size    = 3
result = total_queries // batch_size
print(result)
batches = range(result)
print(batches)

for batch_num in batches:
    start = batch_num * batch_size
    end   = start + batch_size - 1
    print(f"Batch {batch_num + 1}: queries {start} to {end}")

#=====================================================================================

count = 0

while count<5:
    print(count)
    count += 1

print(count)

#=======================================================================
odds = []

for n in range(1,10):
    if n % 2 == 0:
        continue
    print(n)
    odds.append(n)

print(f"odd numbers : {odds}")

for n in range(1,10):
    if n>5:
        break
print (f"numbers stopped at {n}")

#==============================================================================

all_reviews = [
    {"review_id": 5001, "rating": 3, "title": "Its fine"},
    {"review_id": 5002, "rating": 5, "title": "Excellent!"},
    {"review_id": 5003, "rating": 4, "title": "Really good"},
    {"review_id": 5004, "rating": 2, "title": "Disappointed"},
    {"review_id": 5005, "rating": 5, "title": "Perfect product"},
    {"review_id": 5006, "rating": 4, "title": "Solid choice"},
]

good_reviews = []

max_to_collect = 3

for review in all_reviews:
    if review['rating'] < 4:
        continue

    good_reviews.append(review)
    if len(good_reviews)>=max_to_collect:
        break

for r in good_reviews:
    print(f"Reviewed by {r['review_id']}, {'*' * r['rating']} and tile is {r['title']}")

#=======================================================================

products = [
    {"name": "Classic Monitor",   "price": 205.21, "stock": 238},
    {"name": "Ultimate Perfume",  "price": 568.17, "stock": 10},
    {"name": "Budget Headphones", "price": 29.99,  "stock": 0},
    {"name": "Yoga Mat Pro",      "price": 45.00,  "stock": 150},
    {"name": "Luxury Cream",      "price": 89.00,  "stock": 0},
]

# check the stocks are available

In_stock =[p for p in products if p['stock'] > 0]

prompt_lines = [
    f"{p['name']} and (${p['price']:.2f}"
    for p in In_stock if p['price'] < 300
]

for line in prompt_lines:
    print(" ",line)
# check affordability of stock where stock < 300
# give all the affordable stocks and their price.









