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
