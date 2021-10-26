brand = {
    'name': 'Zara',
    'creation_date': '1975' ,
    'creator_name': 'Amancio Ortega Gaona' ,
    'type_of_clothes':[' men',' women',' children',' home'] ,
    'international_competitors': ['Gap', 'H&M', 'Benetton'] ,
    'number_stores': '7000' ,
    'major_color':{ 
    'France': 'blue', 
    'Spain': 'red', 
    'US': ['pink', 'green'],
    }
}
# Change the number of stores to 2.
brand['number_stores'] = 2
# print(brand['number_stores'])
# 4. Print a sentence that explains who Zaras clients are.
# print(brand['name']+'is a clothing company that exist since '+brand['creation_date']+' by the founder '+brand['creator_name'])
# 5. Add a key called country_creation with a value of Spain.
brand['country_creation'] = 'spain'
# print(brand)
# 6. Check if the key international_competitors is in the dictionary.

if 'international_competitors' in brand.keys() :
    brand['international_competitors'].append('Desigual')
print(brand['international_competitors'])

# If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
del brand['creation_date']
# print(brand)
# 8. Print the last international competitor.
print(brand['international_competitors'][-1])
# 9. Print the major clothes colors in the US.
print(brand['major_color']['US'])
# 10. Print the amount of key value pairs (ie. length of the dictionary).
pairs_amount = 0
for keys,values in brand.items():
    if type(values) == dict:
        for i,j in values.items():
            pairs_amount+=1
            print(i,j)
         
        continue
    pairs_amount+=1
    print(keys,values)
print(pairs_amount)   
# 11. Print the keys of the dictionary.
print(brand.keys())
