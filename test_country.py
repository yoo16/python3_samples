from models.country import Country

country = Country()
country.all()

print(country.sql)
print(country.values)